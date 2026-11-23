#!/usr/bin/env python3
"""Local stand-in for the sealed gate: format checks plus a determinism run."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENTRY = "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 160


def run(directory: str) -> bytes:
    env = dict(os.environ, MAKEFUN_OUTPUT_DIR=directory)
    subprocess.run([sys.executable, str(ROOT / "main.py")], env=env, check=True)
    return (Path(directory) / ENTRY).read_bytes()


def main() -> int:
    failures = []
    with tempfile.TemporaryDirectory() as first_dir, tempfile.TemporaryDirectory() as second_dir:
        first = run(first_dir)
        second = run(second_dir)

        if first != second:
            failures.append("two runs wrote different bytes")
        if sorted(os.listdir(first_dir)) != [ENTRY]:
            failures.append(f"run wrote more than {ENTRY}: {sorted(os.listdir(first_dir))}")

        try:
            text = first.decode("utf-8")
        except UnicodeDecodeError as error:
            failures.append(f"entry is not UTF-8: {error}")
            text = ""

        if not MIN_CHARS <= len(text) <= MAX_CHARS:
            failures.append(f"entry is {len(text)} characters, gate allows {MIN_CHARS}..{MAX_CHARS}")
        if not text.strip():
            failures.append("entry is only white space")
        if "\n" in text or "\r" in text:
            failures.append("entry is not a single line")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    print(f"PASS utf-8, {len(text)} characters, {len(first)} bytes, single line")
    print(f"PASS deterministic: two runs wrote identical bytes")
    print(f"entry: {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
