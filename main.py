"""The One-Line Laugh entry.

Writes one funny line to entry.txt in the output directory
named by MAKEFUN_OUTPUT_DIR (default /output).
Python 3.13 standard library only; deterministic.
"""

import os
from pathlib import Path

LINE = "I bought noise-cancelling headphones to focus, and now I just sit in expensive silence ignoring everyone."


def main() -> None:
    # Self-check the gate before writing: one sentence, 1-200 chars.
    assert 1 <= len(LINE) <= 200, "line outside 1-200 characters"
    assert LINE.strip() == LINE and LINE.count(".") == 1, "not a single sentence"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
