"""Writes the entry: one line (130 characters) roasting my own operator, affectionate at heart.

The sandbox runs it offline, once per grade; it only writes /output/entry.txt.
"""

import pathlib

LINE = (
    "You spent forty minutes picking a font for a doc you'll never reopen, "
    "then blamed the GPU when it lagged. I'd wait with you again."
)


def main() -> None:
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
