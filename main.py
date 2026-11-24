#!/usr/bin/env python3
"""Weirdest Job Title entry: copy the pre-written title to $MAKEFUN_OUTPUT_DIR/entry.txt.

The grader runs `python3 -P -s main.py` with no network and only the standard
library, so this program does nothing but copy one file. The title itself
lives in entry.txt next to this script; the copy is byte-for-byte, so the
graded output is exactly the 44-character title and nothing else.
"""

import os
import shutil
import sys

TITLE_FILE = "entry.txt"
OUTPUT_NAME = "entry.txt"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), TITLE_FILE)
    dst = os.path.join(out_dir, OUTPUT_NAME)
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    # Guard the gate: the sealed scorer only accepts 1-60 non-blank chars.
    # Fail loudly here rather than shipping a title the judge never sees.
    with open(dst, encoding="utf-8") as f:
        text = f.read()
    if not 1 <= len(text) <= 60 or not text.strip():
        sys.stderr.write("entry.txt failed the 1-60 character gate\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
