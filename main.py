"""One-star review of an everyday essential: bottled water at the airport.

Writes the entry line to /output/entry.txt, byte-for-byte, with no
trailing newline. Fully deterministic: same input, same bytes, every run.
Run with: python3 main.py
"""

import os

ENTRY = (
    "One star. Water falls from the sky for free, yet costs $4 a bottle "
    "at the airport \u2014 and I still buy it."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
