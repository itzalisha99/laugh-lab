"""One-Liner Laugh Lab entry: the excuse a robot vacuum gives after eating a sock.

Writes a single short funny line (at most 200 characters) to /output/entry.txt.
Stdlib only, deterministic: the same line every run.
"""

import os

LINE = "The sock is not missing. It has been promoted to internal dust filter."


def validate(line: str) -> None:
    """Mirror the bounty gate: 1-200 UTF-8 chars, not only whitespace, one line."""
    text = line.encode("utf-8").decode("utf-8")
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
