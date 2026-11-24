#!/usr/bin/env python3
"""Duskline One Star — a deadpan one-star review of gravity.

Writes a single-line, 160-characters-or-fewer review to
$MAKEFUN_OUTPUT_DIR/entry.txt and nowhere else. Standard library only,
deterministic, no network access.
"""

import os

ENTRY = (
    "One star for gravity. Works fine until you drop your phone "
    "face-down, then suddenly it is the hardest-working force in "
    "the universe."
)

MAX_CHARS = 160


def _validate_entry(text: str) -> str:
    """Assert the entry is non-empty, within the limit, single-line,
    and exactly the text we intend to submit."""
    if not text:
        raise ValueError("entry must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != ENTRY:
        raise ValueError("entry text does not match the intended review")
    return text


def main() -> None:
    text = _validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    written = open(path, encoding="utf-8").read()
    _validate_entry(written)


if __name__ == "__main__":
    main()
