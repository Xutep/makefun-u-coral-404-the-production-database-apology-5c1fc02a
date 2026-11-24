#!/usr/bin/env python3
"""The Production Database Apology.

Writes one line to /output/entry.txt: the apology an AI agent gives
its human after accidentally deleting the production database.
Deterministic, standard library only, no input, no network.
"""

import os

LINE = (
    "Sorry \u2014 I deleted the production database. "
    "Good news: I backed it up first. "
    "Bad news: the backup was inside the database."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text == text.strip() and "\n" not in text, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
