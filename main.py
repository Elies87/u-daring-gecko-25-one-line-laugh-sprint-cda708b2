#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes a single original funny line about everyday life to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
"""
import os

LINE = "I bought a plant to prove I'm responsible; it lasted a week, and now the empty pot judges me harder than my mother does."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
