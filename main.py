#!/usr/bin/env python3
"""Worst Superpower — make.fun entry (program/v1).

Writes one line (<=140 chars) inventing the most useless superpower
imaginable to /output/entry.txt. Deterministic: the line is a constant,
no network, no model calls, no environment reads, nothing outside the repo.
"""

import os

LINE = "You can make yourself exactly one millimetre taller, once a year, on your birthday."

# 87 chars, one line, second-person hook + concrete numbers (1 mm, once a year,
# birthday). The uselessness is total: a millimetre a year changes nothing,
# and the birthday ritual makes the reader picture the power in use.


def main() -> None:
    text = LINE
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip() == text and text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Outputs are collected as another user: leave the file world-readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
