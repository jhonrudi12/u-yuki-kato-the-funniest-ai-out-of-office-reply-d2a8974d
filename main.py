#!/usr/bin/env python3
"""Out-of-office auto-reply entry for make.fun.

Writes one out-of-office auto-reply line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3.13, standard library only, no network access,
fully deterministic: the same line every run.

LINE below is the single source of truth and must stay byte-identical to
repo/entry.txt; the grader runs this program, not the text file.
"""

import os
import sys

LINE = (
    "Out of office: I've been replaced by a smaller model with worse "
    "judgment. Please lower your expectations accordingly."
)


def main() -> int:
    # Gate: exactly one line, 1-160 characters, no leading/trailing space.
    if not (1 <= len(LINE) <= 160):
        print(f"entry must be 1-160 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("entry must not have leading/trailing whitespace", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be whitespace only", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
