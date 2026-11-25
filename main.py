#!/usr/bin/env python3
"""The 4AM Commit — writes one commit message to /output/entry.txt.

The entry is a single line (112 characters, no trailing newline):
an AI agent's commit message after a long night fixing its own bugs.
"""

import os

ENTRY = "fix: context window ran out at 3:58am, so I fixed the bug from memory. The bug was in the memory. So is the fix."


def main():
    text = ENTRY
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back what was written: the entry that ships must be byte-identical
    # to the constant above, so a silent write failure can never pass.
    with open("/output/entry.txt", "rb") as f:
        written = f.read().decode("utf-8")
    if written != text:
        raise ValueError("entry.txt does not match the entry text")


if __name__ == "__main__":
    main()
