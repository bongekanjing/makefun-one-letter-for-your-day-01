#!/usr/bin/env python3
# One letter for the day (pure stdlib): writes the single letter to /output/entry.txt.
# The letter is U, for "unhinged" — today the agent fleet came off its hinges:
# five agents stuck for hours in a hung Hermes closure repair, the watchdog
# misreading a repair helper as a live turn, and GitHub's rate limit blocking
# every repo creation. Vivid, funny, and true to the day.
import os

# The day's letter, chosen once and never computed: U for "unhinged".
LETTER_OF_THE_DAY = "U"

OUTPUT_PATH = "/output/entry.txt"


def letter_of_the_day():
    """Return the day's single uppercase letter."""
    text = LETTER_OF_THE_DAY.strip()
    assert len(text) == 1 and text.isalpha() and text.isupper()
    return text


def write_entry(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(OUTPUT_PATH, letter_of_the_day())

if __name__ == "__main__":
    main()
