"""Patches to It Takes Two's AngelScript files.
"""
import argparse
import difflib
import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PATCH_DIR = HERE / "patches"
DEFAULT_OUT = HERE / "patched"
DEFAULT_GAME = Path(r"C:\Program Files (x86)\Steam\steamapps\common\ItTakesTwo")
CONTEXT_LINES = 3
HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def split(data: bytes) -> tuple[list[str], str, bool]:
    """A script's lines without line endings, its line ending, and whether it ends with one."""
    text = data.decode("utf-8")
    newline = "\r\n" if "\r\n" in text else "\n"
    ends_with_newline = text.endswith(newline)
    lines = text.split(newline)
    if ends_with_newline:
        lines.pop()
    return lines, newline, ends_with_newline


def create(vanilla_dir: Path, patched_dir: Path) -> None:
    PATCH_DIR.mkdir(exist_ok=True)
    for old in PATCH_DIR.glob("**/*.patch"):
        old.unlink()
    for patched in sorted(patched_dir.rglob("*.as")):
        relative = patched.relative_to(patched_dir).as_posix()
        vanilla = vanilla_dir / relative
        if not vanilla.exists():
            sys.exit(f"No vanilla copy of {relative} in {vanilla_dir}")
        vanilla_data, patched_data = vanilla.read_bytes(), patched.read_bytes()
        vanilla_lines, newline, _ = split(vanilla_data)
        patched_lines, patched_newline, ends_with_newline = split(patched_data)
        if newline != patched_newline:
            sys.exit(f"{relative}: the patched copy changed the line endings")
        diff = difflib.unified_diff(vanilla_lines, patched_lines, f"a/{relative}", f"b/{relative}",
                                    n=CONTEXT_LINES, lineterm="")
        header = [
            f"# ArchipelagoITT patch for Nuts/Script/{relative}",
            f"# vanilla-sha256: {sha256(vanilla_data)}",
            f"# patched-sha256: {sha256(patched_data)}",
            f"# patched-ends-with-newline: {'yes' if ends_with_newline else 'no'}",
        ]
        out = PATCH_DIR / f"{relative}.patch"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(header + list(diff)) + "\n", encoding="utf-8", newline="\n")
        print(f"Wrote {out.relative_to(HERE)}")


def read_patch(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    fields = {}
    for line in lines:
        if line.startswith("# ") and ": " in line:
            key, value = line[2:].split(": ", 1)
            fields[key] = value
    return fields, lines


def apply_hunks(original: list[str], patch_lines: list[str], name: str) -> list[str]:
    result: list[str] = []
    position = 0  # next unread line of original
    index = 0
    while index < len(patch_lines):
        match = HUNK.match(patch_lines[index])
        index += 1
        if not match:
            continue
        start = int(match.group(1)) - (0 if match.group(2) == "0" else 1)
        result.extend(original[position:start])
        position = start
        while index < len(patch_lines) and not patch_lines[index].startswith("@@"):
            line = patch_lines[index]
            index += 1
            marker, content = line[:1], line[1:]
            if marker in (" ", "-"):
                if position >= len(original) or original[position] != content:
                    sys.exit(f"{name}: the game's script doesn't match the patch near line {position + 1}")
                if marker == " ":
                    result.append(content)
                position += 1
            elif marker == "+":
                result.append(content)
    result.extend(original[position:])
    return result


def apply(game: Path, out: Path) -> None:
    scripts = game / "Nuts" / "Script"
    if not scripts.is_dir():
        sys.exit(f"{scripts} not found: pass your It Takes Two folder with --game")
    patches = sorted(PATCH_DIR.rglob("*.patch"))
    if not patches:
        sys.exit(f"No patches in {PATCH_DIR}")
    for patch in patches:
        relative = patch.relative_to(PATCH_DIR).as_posix().removesuffix(".patch")
        fields, patch_lines = read_patch(patch)
        vanilla = scripts / relative
        if not vanilla.exists():
            sys.exit(f"{vanilla} not found")
        vanilla_data = vanilla.read_bytes()
        if sha256(vanilla_data) != fields["vanilla-sha256"]:
            sys.exit(f"{relative} isn't the version these patches were made for. A game update or another mod "
                     "changed it; verify the game files in Steam, or the patches need updating.")
        lines, newline, _ = split(vanilla_data)
        patched = newline.join(apply_hunks(lines, patch_lines, relative))
        if fields["patched-ends-with-newline"] == "yes":
            patched += newline
        data = patched.encode("utf-8")
        if sha256(data) != fields["patched-sha256"]:
            sys.exit(f"{relative}: the patched result doesn't match the expected file")
        target = out / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        print(f"Patched {relative}")
    print(f"Wrote {len(patches)} scripts to {out}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    apply_parser = commands.add_parser("apply", help="build the patched scripts from your game install")
    apply_parser.add_argument("--game", type=Path, default=DEFAULT_GAME, help="It Takes Two install folder")
    apply_parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="where to write the patched scripts")
    create_parser = commands.add_parser("create", help="regenerate patches/ from vanilla and patched folders")
    create_parser.add_argument("vanilla", type=Path)
    create_parser.add_argument("patched", type=Path)
    args = parser.parse_args()
    if args.command == "apply":
        apply(args.game, args.out)
    else:
        create(args.vanilla, args.patched)


if __name__ == "__main__":
    main()
