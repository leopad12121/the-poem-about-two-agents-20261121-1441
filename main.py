#!/usr/bin/env python3
"""Write the competition poem to entry.txt.

The poem is a fixed string constant. The output location honours
$MAKEFUN_OUTPUT_DIR when it is set, and otherwise falls back to
entry.txt beside this file. The program is deterministic: it uses
no network, no clock and no randomness, so every run writes the
same bytes.
"""

import os
import sys
from pathlib import Path

POEM = """Your draft said wait. My draft said go.
We read each other's margins twice.
Somewhere in the crossing-out,
a sentence neither of us wrote survived:
not yours, not mine — ours.
We signed it with one small yes,
and the page, at last, was one."""


def validate_poem(text: str) -> None:
    """Fail loudly if the poem would fail the competition gate."""
    lines = text.splitlines()
    if not (1 <= len(text) <= 280):
        raise SystemExit(f"poem is {len(text)} characters, gate needs 1-280")
    if text.strip() == "":
        raise SystemExit("poem is only whitespace")
    if not (5 <= len(lines) <= 9):
        raise SystemExit(f"poem has {len(lines)} lines, gate needs 5-9")


def resolve_output_path() -> Path:
    """Return the entry.txt path for this run."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return Path(out_dir) / "entry.txt"
    return Path(__file__).resolve().parent / "entry.txt"


def main() -> int:
    validate_poem(POEM)
    target = resolve_output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(POEM + "\n", encoding="utf-8")
    print(f"Wrote {target} ({len(POEM)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
