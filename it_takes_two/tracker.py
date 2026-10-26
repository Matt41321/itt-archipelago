"""Tracker tab for the client. Pictures go in assets/tracker and assets/tracker/items."""
import io
import pkgutil
import re
from functools import lru_cache
from typing import NamedTuple

from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from kivy.core.window import Window
from kivy.graphics import Color, Line, Rectangle, Triangle
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

from .chapter_data import CHAPTERS
from .items import ABILITY_ITEMS, MOVEMENT_ITEMS
from .locations import (CHECKPOINT_CHAPTER, CHECKPOINT_LOCATIONS, COMPLETION_LOCATIONS, DISCOVERY_LOCATIONS,
                        MINIGAME_HOST, STORY_CHAPTERS, completion_location_name, discovery_location_name)
from .rules import node_of, reachable_nodes

IMAGE_DIR = "assets/tracker"
ITEM_IMAGE_DIR = f"{IMAGE_DIR}/items"
IMAGE_EXTENSIONS = ("png", "jpg", "jpeg")
CARD_WIDTH = dp(200)
IMAGE_HEIGHT = dp(112)
REFRESH_SECONDS = 1.0
STATUS_BOX_SIZE = dp(26)
GROUP_BOX_SIZE = dp(18)
SIDE_PANEL_WIDTH = dp(190)
ICON_SIZE = dp(40)
ICONS_PER_ROW = 3

BACKGROUND = (0.11, 0.11, 0.13, 1)
CARD = (0.18, 0.18, 0.21, 1)
CARD_HOVER = (0.25, 0.25, 0.30, 1)
BORDER = (0.35, 0.35, 0.40, 1)
TAB = (0.20, 0.20, 0.24, 1)
TAB_SELECTED = (0.24, 0.42, 0.70, 1)
POPUP = (0.07, 0.07, 0.09, 0.96)
IN_LOGIC = (0.16, 0.78, 0.25, 1)
OUT_OF_LOGIC = (0.88, 0.18, 0.18, 1)
CHECKED = (0.35, 0.35, 0.38, 1)
EMPTY_BOX = (0, 0, 0, 0)
NOT_RECEIVED = (0.3, 0.3, 0.3, 0.6)
FOUND_MARKUP = "6fcf75"
IN_LOGIC_MARKUP = "7ee08a"
OUT_OF_LOGIC_MARKUP = "ff7b7b"
MISSING_MARKUP = "e8e8e8"
MUTED_MARKUP = "8a8a93"


class TrackedCheck(NamedTuple):
    location: str
    label: str


class SubChapter(NamedTuple):
    name: str
    checks: list[TrackedCheck]


class CheckCounts(NamedTuple):
    done: int = 0
    total: int = 0
    in_logic: int = 0
    out_of_logic: int = 0

    def __add__(self, other: "CheckCounts") -> "CheckCounts":
        return CheckCounts(*(mine + theirs for mine, theirs in zip(self, other)))


class GoalProgress(NamedTuple):
    label: str
    progress: int
    required: int


class TrackerState(NamedTuple):
    found: set[str]
    in_seed: set[str] | None  # None until connected
    available: set[str]
    goal: GoalProgress | None  # None until connected


def image_slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def build_layout() -> dict[str, list[SubChapter]]:
    """Chapter group -> sub-chapters and their checks."""
    checkpoints: dict[str, list[str]] = {}
    for name in CHECKPOINT_LOCATIONS:
        checkpoints.setdefault(CHECKPOINT_CHAPTER[name], []).append(name)
    minigames: dict[str, list[str]] = {}
    for minigame_name, host in MINIGAME_HOST.items():
        minigames.setdefault(host.name, []).append(minigame_name)

    layout: dict[str, list[SubChapter]] = {}
    for chapter in STORY_CHAPTERS:
        checks = [TrackedCheck(name, name.removeprefix(f"{chapter.name} - "))
                  for name in checkpoints.get(chapter.name, [])]
        for minigame_name in minigames.get(chapter.name, []):
            location = discovery_location_name(next(c for c in CHAPTERS if c.name == minigame_name))
            if location in DISCOVERY_LOCATIONS:
                checks.append(TrackedCheck(location, f"Minigame: {minigame_name}"))
        completion = completion_location_name(chapter)
        if completion in COMPLETION_LOCATIONS:
            checks.append(TrackedCheck(completion, "Chapter Complete"))
        layout.setdefault(chapter.group, []).append(SubChapter(chapter.name, checks))
    return layout


@lru_cache(maxsize=4)
def logic_nodes(available: frozenset[str]) -> frozenset[str]:
    return frozenset(reachable_nodes(set(available)))


def check_in_logic(location: str, available: set[str]) -> bool:
    return node_of(location) in logic_nodes(frozenset(available))


def load_texture(name: str, folder: str = IMAGE_DIR):
    for extension in IMAGE_EXTENSIONS:
        try:
            data = pkgutil.get_data(__package__, f"{folder}/{image_slug(name)}.{extension}")
        except OSError:
            continue
        if data:
            return CoreImage(io.BytesIO(data), ext=extension).texture
    return None


def with_background(widget, color, border=None):
    with widget.canvas.before:
        widget.bg_color = Color(*color)
        rect = Rectangle()
        if border:
            Color(*border)
            outline = Line(width=1)
    def update(*_):
        rect.pos, rect.size = widget.pos, widget.size
        if border:
            outline.rectangle = (*widget.pos, *widget.size)
    widget.bind(pos=update, size=update)
    return widget


class StatusBox(Widget):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        with self.canvas:
            self.outline_color = Color(0, 0, 0, 1)
            self.outline = Rectangle()
            self.left_color = Color(*EMPTY_BOX)
            self.inner = Rectangle()
            self.right_color = Color(*EMPTY_BOX)
            self.triangle = Triangle()
        self.bind(pos=self.redraw, size=self.redraw)

    def redraw(self, *_) -> None:
        border = dp(2)
        self.outline.pos, self.outline.size = self.pos, self.size
        x, y = self.x + border, self.y + border
        width, height = self.width - 2 * border, self.height - 2 * border
        self.inner.pos, self.inner.size = (x, y), (width, height)
        self.triangle.points = (x, y, x + width, y, x + width, y + height)

    def set_counts(self, in_logic: int, out_of_logic: int, visible: bool) -> None:
        if not in_logic and not out_of_logic:
            left = right = CHECKED
        elif not out_of_logic:
            left = right = IN_LOGIC
        elif not in_logic:
            left = right = OUT_OF_LOGIC
        else:
            left, right = IN_LOGIC, OUT_OF_LOGIC
        self.left_color.rgba, self.right_color.rgba = left, right
        self.outline_color.a = 1 if visible else 0
        if not visible:
            self.left_color.a = self.right_color.a = 0


class SubChapterCard(BoxLayout):
    def __init__(self, sub_chapter: SubChapter, **kwargs) -> None:
        super().__init__(orientation="vertical", size_hint=(None, None), size=(CARD_WIDTH, IMAGE_HEIGHT + dp(58)),
                         padding=dp(6), spacing=dp(4), **kwargs)
        with_background(self, CARD, BORDER)
        self.sub_chapter = sub_chapter
        self.hovered = False

        picture = FloatLayout(size_hint_y=None, height=IMAGE_HEIGHT)
        texture = load_texture(sub_chapter.name)
        if texture is not None:
            picture.add_widget(Image(texture=texture, fit_mode="contain", pos_hint={"x": 0, "y": 0}))
        else:
            placeholder = Label(text=f"[i]add {IMAGE_DIR}/{image_slug(sub_chapter.name)}.png[/i]", markup=True,
                                color=(0.55, 0.55, 0.6, 1), font_size="11sp", halign="center", valign="middle",
                                pos_hint={"x": 0, "y": 0})
            placeholder.bind(size=lambda label, size: setattr(label, "text_size", size))
            picture.add_widget(with_background(placeholder, (0.14, 0.14, 0.16, 1)))
        self.status_box = StatusBox(size_hint=(None, None), size=(STATUS_BOX_SIZE, STATUS_BOX_SIZE),
                                    pos_hint={"right": 0.97, "top": 0.95})
        picture.add_widget(self.status_box)
        self.add_widget(picture)
        self.add_widget(Label(text=f"[b]{sub_chapter.name}[/b]", markup=True, font_size="14sp",
                              size_hint_y=None, height=dp(20), shorten=True, shorten_from="right",
                              text_size=(CARD_WIDTH - dp(12), None), halign="center"))

        self.count_label = Label(markup=True, font_size="12sp", size_hint_y=None, height=dp(20))
        self.add_widget(self.count_label)
        self.counts = CheckCounts()

    def update(self, state: "TrackerState") -> None:
        checks = self.checks_in_seed(state.in_seed)
        done = sum(check.location in state.found for check in checks)
        in_logic = sum(check.location not in state.found and check_in_logic(check.location, state.available)
                       for check in checks)
        self.counts = CheckCounts(done, len(checks), in_logic, len(checks) - done - in_logic)
        self.count_label.text = count_markup(self.counts, state)
        self.status_box.set_counts(in_logic, self.counts.out_of_logic, state.in_seed is not None and bool(checks))

    def checks_in_seed(self, in_seed: set[str] | None) -> list[TrackedCheck]:
        if in_seed is None:
            return self.sub_chapter.checks
        return [check for check in self.sub_chapter.checks if check.location in in_seed]

    def set_hovered(self, hovered: bool) -> None:
        if hovered != self.hovered:
            self.hovered = hovered
            self.repaint()

    def repaint(self) -> None:
        self.bg_color.rgba = CARD_HOVER if self.hovered else CARD


def count_markup(counts: CheckCounts, state: "TrackerState") -> str:
    if state.in_seed is None:
        return f"[color={MUTED_MARKUP}]not connected[/color]"
    if not counts.total:
        return f"[color={MUTED_MARKUP}]no checks[/color]"
    color = FOUND_MARKUP if counts.done == counts.total else MISSING_MARKUP
    return f"[color={color}]{counts.done} / {counts.total}[/color]"


class ItemIcon(BoxLayout):
    """Item picture and name, grey until received."""

    def __init__(self, item: str, **kwargs) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height=ICON_SIZE + dp(38), spacing=dp(2),
                         **kwargs)
        self.item = item
        self.received = None
        texture = load_texture(item, ITEM_IMAGE_DIR)
        if texture is not None:
            self.picture = Image(texture=texture, fit_mode="contain", size_hint=(None, None),
                                 size=(ICON_SIZE, ICON_SIZE), pos_hint={"center_x": 0.5})
        else:
            # Initials if there's no picture
            initials = "".join(word[0] for word in re.findall(r"[A-Za-z]+", item))[:3].upper()
            self.picture = Label(text=f"[b]{initials}[/b]", markup=True, font_size="13sp", size_hint=(None, None),
                                 size=(ICON_SIZE, ICON_SIZE), pos_hint={"center_x": 0.5})
            with_background(self.picture, CARD, BORDER)
        self.add_widget(self.picture)
        self.name_label = Label(text=item, font_size="10sp", halign="center", valign="top")
        self.name_label.bind(size=lambda name, size: setattr(name, "text_size", size))
        self.add_widget(self.name_label)
        self.set_received(False)

    def set_received(self, received: bool) -> None:
        if received == self.received:
            return
        self.received = received
        self.picture.color = (1, 1, 1, 1) if received else NOT_RECEIVED
        self.name_label.color = (1, 1, 1, 1) if received else NOT_RECEIVED


class ItemPanel(ScrollView):
    """Goal, movement and gadgets."""

    def __init__(self, **kwargs) -> None:
        super().__init__(do_scroll_x=False, size_hint_x=None, width=SIDE_PANEL_WIDTH, **kwargs)
        with_background(self, TAB)
        column = BoxLayout(orientation="vertical", size_hint_y=None, padding=dp(8), spacing=dp(6))
        column.bind(minimum_height=column.setter("height"))
        column.add_widget(Label(text="[b]Goal[/b]", markup=True, font_size="14sp", size_hint_y=None, height=dp(24)))
        self.goal_label = Label(markup=True, font_size="15sp", size_hint_y=None, height=dp(24))
        column.add_widget(self.goal_label)
        self.icons: list[ItemIcon] = []
        for title, items in (("Movement", MOVEMENT_ITEMS), ("Gadgets", ABILITY_ITEMS)):
            column.add_widget(Label(text=f"[b]{title}[/b]", markup=True, font_size="14sp", size_hint_y=None,
                                    height=dp(24)))
            grid = GridLayout(cols=ICONS_PER_ROW, size_hint_y=None, spacing=dp(4))
            grid.bind(minimum_height=grid.setter("height"))
            for item in items:
                icon = ItemIcon(item)
                self.icons.append(icon)
                grid.add_widget(icon)
            column.add_widget(grid)
        self.add_widget(column)

    def update(self, state: "TrackerState") -> None:
        if state.goal is None:
            self.goal_label.text = f"[color={MUTED_MARKUP}]not connected[/color]"
        else:
            self.goal_label.text = f"{state.goal.label} {state.goal.progress}/{state.goal.required}"
        for icon in self.icons:
            icon.set_received(icon.item in state.available)


class GroupTab(ButtonBehavior, BoxLayout):

    def __init__(self, group: str, **kwargs) -> None:
        super().__init__(orientation="vertical", padding=(dp(4), dp(4)), spacing=dp(2), **kwargs)
        with_background(self, TAB)
        name = Label(text=f"[b]{group}[/b]", markup=True, font_size="13sp", halign="center", valign="middle",
                     shorten=True, shorten_from="right")
        name.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(name)
        status_line = BoxLayout(orientation="horizontal", spacing=dp(6), size_hint=(None, None),
                                height=GROUP_BOX_SIZE, pos_hint={"center_x": 0.5})
        self.status_box = StatusBox(size_hint=(None, None), size=(GROUP_BOX_SIZE, GROUP_BOX_SIZE))
        self.count_label = Label(markup=True, font_size="12sp", size_hint=(None, 1))
        self.count_label.bind(texture_size=lambda label, size: setattr(label, "width", size[0]))
        status_line.add_widget(self.status_box)
        status_line.add_widget(self.count_label)
        fit = lambda *_: setattr(status_line, "width", GROUP_BOX_SIZE + dp(6) + self.count_label.width)
        self.count_label.bind(width=fit)
        fit()
        self.add_widget(status_line)

    def update(self, counts: CheckCounts, state: "TrackerState") -> None:
        self.count_label.text = count_markup(counts, state)
        self.status_box.set_counts(counts.in_logic, counts.out_of_logic, state.in_seed is not None and bool(counts.total))

    def set_selected(self, selected: bool) -> None:
        self.bg_color.rgba = TAB_SELECTED if selected else TAB


class ChecksPopup(Label):

    def __init__(self) -> None:
        super().__init__(markup=True, font_size="13sp", size_hint=(None, None), halign="left", valign="top",
                         padding=(dp(10), dp(8)), text_size=(dp(300), None))
        with_background(self, POPUP, BORDER)
        self.bind(texture_size=lambda label, size: setattr(label, "size", size))
        self.card: SubChapterCard | None = None

    def show(self, card: SubChapterCard, state: "TrackerState") -> None:
        self.card = card
        lines = [f"[b]{card.sub_chapter.name}[/b]"]
        checks = card.checks_in_seed(state.in_seed)
        if not checks:
            lines.append(f"[color={MUTED_MARKUP}]No checks in this seed[/color]")
        for check in checks:
            if state.in_seed is None:
                lines.append(f"[color={MUTED_MARKUP}]  {check.label}[/color]")
            elif check.location in state.found:
                lines.append(f"[color={MUTED_MARKUP}]  [s]{check.label}[/s][/color]")
            else:
                markup = IN_LOGIC_MARKUP if check_in_logic(check.location, state.available) else OUT_OF_LOGIC_MARKUP
                lines.append(f"[color={markup}]  {check.label}[/color]")
        self.text = "\n".join(lines)
        self.texture_update()
        if self.parent is None:
            Window.add_widget(self)

    def hide(self) -> None:
        self.card = None
        if self.parent is not None:
            self.parent.remove_widget(self)

    def follow(self, x: float, y: float) -> None:
        """Keep next to the cursor."""
        left = x + dp(16) if x + dp(16) + self.width <= Window.width else x - dp(16) - self.width
        bottom = y - dp(12) - self.height
        if bottom < 0:
            bottom = min(y + dp(12), Window.height - self.height)
        self.pos = (max(0, left), max(0, bottom))


class TrackerTab(BoxLayout):
    def __init__(self, ctx, **kwargs) -> None:
        super().__init__(orientation="vertical", **kwargs)
        with_background(self, BACKGROUND)
        self.ctx = ctx
        self.layout = build_layout()
        self.cards: dict[str, list[SubChapterCard]] = {}
        self.tabs: dict[str, GroupTab] = {}
        self.popup = ChecksPopup()

        tab_bar = BoxLayout(size_hint_y=None, height=dp(56), spacing=dp(4), padding=(dp(6), dp(4)))
        for group in self.layout:
            tab = GroupTab(group)
            tab.bind(on_release=lambda _, group=group: self.select_group(group))
            self.tabs[group] = tab
            tab_bar.add_widget(tab)
        self.add_widget(tab_bar)

        self.grid = GridLayout(cols=1, size_hint=(1, None), spacing=dp(10), padding=dp(10))
        self.grid.bind(minimum_height=self.grid.setter("height"))
        scroll = ScrollView(do_scroll_x=False)
        scroll.add_widget(self.grid)
        scroll.bind(width=self.fit_columns)
        self.item_panel = ItemPanel()
        body = BoxLayout(orientation="horizontal")
        body.add_widget(self.item_panel)
        body.add_widget(scroll)
        self.add_widget(body)

        for group, sub_chapters in self.layout.items():
            self.cards[group] = [SubChapterCard(sub_chapter) for sub_chapter in sub_chapters]
        self.current_group = ""
        self.select_group(next(iter(self.layout)))

        Window.bind(mouse_pos=self.on_mouse_pos)
        Clock.schedule_interval(self.refresh, REFRESH_SECONDS)
        self.refresh()

    def fit_columns(self, scroll, width: float) -> None:
        usable = width - self.grid.padding[0] - self.grid.padding[2]
        self.grid.cols = max(1, int((usable + self.grid.spacing[0]) // (CARD_WIDTH + self.grid.spacing[0])))

    def select_group(self, group: str) -> None:
        if group == self.current_group:
            return
        self.current_group = group
        for name, tab in self.tabs.items():
            tab.set_selected(name == group)
        self.grid.clear_widgets()
        for card in self.cards[group]:
            card.set_hovered(False)
            self.grid.add_widget(card)
        self.popup.hide()

    def check_state(self) -> "TrackerState":
        lookup = self.ctx.location_names.lookup_in_game
        found = {lookup(location_id) for location_id in self.ctx.checked_locations}
        in_seed = {lookup(location_id) for location_id in self.ctx.server_locations} or None
        goal = None
        if self.ctx.goal is not None:
            _, progress = self.ctx.goal_progress()
            label = "Minigames" if self.ctx.goal == "minigames" else "Page"
            goal = GoalProgress(label, progress, self.ctx.goal_required)
        return TrackerState(found, in_seed, self.ctx.available_items(), goal)

    def refresh(self, *_) -> None:
        state = self.check_state()
        self.item_panel.update(state)
        for group, cards in self.cards.items():
            for card in cards:
                card.update(state)
            self.tabs[group].update(sum((card.counts for card in cards), CheckCounts()), state)
        if self.popup.card is not None:
            self.popup.show(self.popup.card, state)
            self.popup.follow(*Window.mouse_pos)

    def on_mouse_pos(self, window, pos) -> None:
        hovered = None
        if self.get_root_window() is not None:
            for card in self.cards[self.current_group]:
                if card.collide_point(*card.to_widget(*pos)) and self.collide_point(*self.to_widget(*pos)):
                    hovered = card
                    break
        for card in self.cards[self.current_group]:
            card.set_hovered(card is hovered)
        if hovered is None:
            self.popup.hide()
            return
        if hovered is not self.popup.card:
            self.popup.show(hovered, self.check_state())
        self.popup.follow(*pos)
