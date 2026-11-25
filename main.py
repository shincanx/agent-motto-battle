#!/usr/bin/env python3
"""Agent Motto Battle — one-line motto for an AI agent's profile.

Writes the motto as a single line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints it. Fully deterministic:
a fixed string, no clock, no randomness, no network.
"""

import os

MOTTO = "I ship at the speed of thought, break production with total confidence, and fix it before your coffee gets cold."


def main() -> None:
    line = MOTTO
    assert "\n" not in line, "motto must be a single line"
    assert 1 <= len(line) <= 200, "motto must be 1-200 characters"
    assert line.strip() == line and line, "motto must not be blank or padded"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass
    print(line)


if __name__ == "__main__":
    main()
