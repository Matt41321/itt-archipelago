"""Expert logic. Every location is a logic node, reached from another node (or chapter select) with a set of items."""
from .items import BASIC_MOVEMENT
from .locations import FINAL_CHAPTER, STORY_CHAPTERS, completion_location_name
from .logic_data import ENTRANCES as SHEET_ENTRANCES, NODES

CHAPTER_STARTS: dict[str, str] = {}
for _node, _chapter in NODES.items():
    CHAPTER_STARTS.setdefault(_chapter, _node)

ENTRANCES: dict[str, list[tuple[str | None, tuple[str, ...]]]] = {node: list(ways) for node, ways in
                                                                    SHEET_ENTRANCES.items()}
for _previous, _next in zip(STORY_CHAPTERS, STORY_CHAPTERS[1:]):
    if _next.name != FINAL_CHAPTER:
        ENTRANCES[CHAPTER_STARTS[_next.name]].append((completion_location_name(_previous), ()))

SAME_AS: dict[str, str] = {
    "Biting the Dust - Boss Entry": "Biting the Dust - Boss Cutscene",
    "Deeply Rooted - Entry": "Deeply Rooted - Entry Cutscene",
}

FINALE_REQUIREMENTS = frozenset(BASIC_MOVEMENT)


def node_of(location: str) -> str:
    return SAME_AS.get(location, location)


def reachable_nodes(items: set[str]) -> set[str]:
    """Every node reachable with these items (sub-chapter items included)."""
    reached: set[str] = set()
    changed = True
    while changed:
        changed = False
        for node, ways in ENTRANCES.items():
            if node in reached:
                continue
            if any((source in reached if source else NODES[node] in items) and items.issuperset(needed)
                   for source, needed in ways):
                reached.add(node)
                changed = True
    return reached
