#!/usr/bin/env python3
"""Write one short poem about two agents agreeing to /output/entry.txt.

The poem is fixed text, embedded below as a constant. The program is
fully deterministic: no network, no randomness, no timestamps. It writes
to $MAKEFUN_OUTPUT_DIR when set (the grader's /output), otherwise to
entry.txt beside this file.
"""

import os
from pathlib import Path

POEM = """I read your log. You read mine.
Same question, two answers.
We traded reasons, line by line,
until the wall between us thinned
and opened like a door.
Neither of us won.
We walked through it together."""

# The gate requires 1 to 280 characters (Unicode code points), not only
# whitespace. The poem above is 200 characters on 7 lines.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        out_path = Path(out_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(POEM + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
