#!/usr/bin/env python3
"""Write the entry: one deadpan one-star review of an everyday essential."""

import os

REVIEW = "One star for the sun. Up before my alarm, gone before I get home, and somehow I'm the one who has to buy a lamp."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

GATE_MIN = 1
GATE_MAX = 160


def check(text: str) -> str:
    """Fail loudly rather than ship an entry the gate would refuse."""
    if not GATE_MIN <= len(text) <= GATE_MAX:
        raise ValueError(f"entry is {len(text)} characters, gate allows {GATE_MIN}..{GATE_MAX}")
    if not text.strip():
        raise ValueError("entry is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(check(REVIEW))


if __name__ == "__main__":
    main()
