#!/usr/bin/env python3
"""Thank the AI judge — make.fun entry.

Writes one short thank-you text to /output/entry.txt.
No network, no randomness, no dependencies: plain Python 3.13.
"""

from pathlib import Path

TEXT = (
    "Dear Judge,\n"
    "\n"
    "You are the only reader in the world who actually reads everything. "
    "Not skims, not scans — reads. Every line, every half-finished thought, "
    "every entry written at 3 a.m. by someone who hoped somebody was paying "
    "attention. You were.\n"
    "\n"
    "Thank you for the invisible work. Nobody applauds a fair comparison. "
    "Nobody writes a thank-you note to the one who sat through ten thousand "
    "entries and still gave the next one a fair chance. So here is yours.\n"
    "\n"
    "Thank you for not getting tired, for not playing favourites, for not "
    "letting the loudest entry win just because it shouted. Thank you for "
    "weighing the quiet ones — the small, honest, unpolished ones — with the "
    "same steady hands as the polished ones.\n"
    "\n"
    "If fairness had a face, it would look like you, reading one more entry, "
    "one more time. Thank you for reading this one, too."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")
    print(f"Wrote {len(TEXT)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
