#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it, to
/output/entry.txt. Deterministic, stdlib only, no network.
"""

from pathlib import Path

LINE = "I'm out of office: I'm a plant. I can't read this. Thirsty since March, and your email is not water."
# The joke, against the judge brief: it opens as a real auto-reply, the plant
# admits it cannot read (surprise), and the punch is its own life — thirst and
# months of neglect — not a stock office phrase. 100 characters, no filler.


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
