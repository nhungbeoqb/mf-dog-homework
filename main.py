#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — entry program.

Writes one line (under 200 characters) to /output/entry.txt: the excuse
a dog gives after being caught eating the homework, in the dog's own
voice. The dog believes it has done nothing wrong — it saved its owner.
"""

import os

ENTRY = (
    "Relax, I saved you. That essay was about to tell the teacher you "
    "never walk me, so I ate the evidence. You're welcome. "
    "I take payment in bones."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip() == ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
