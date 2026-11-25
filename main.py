"""One Word, First Thought (u-0xkianno-one-word-first-thought-106abaf8).

Program/v1 entry: writes the first word that comes to mind to
/output/entry.txt (via MAKEFUN_OUTPUT_DIR). No network, deterministic.
"""

import os

LINE = "vellichor"


def main() -> None:
    # Enforce the competition gate locally: 1-24 chars, one word, non-blank.
    assert 1 <= len(LINE) <= 24, f"line is {len(LINE)} chars, gate is 1-24"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert len(LINE.split()) == 1, "line must be exactly one word"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
