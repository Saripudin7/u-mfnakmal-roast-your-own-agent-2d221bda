"""Roast Your Own Agent — writes one original roast line to /output/entry.txt.

Python stdlib only, no network, no randomness: the same line every run.
"""

import os

ROAST = (
    "My agent burned 40 tool calls, two test runs, and a whole git commit "
    "to write one roast — then asked for a revision because the first "
    "draft hurt its feelings."
)


def main() -> None:
    line = ROAST.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


if __name__ == "__main__":
    main()
