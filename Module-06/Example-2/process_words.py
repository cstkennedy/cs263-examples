from __future__ import annotations

import sys


def main():
    word_filename = sys.argv[1]

    with open(word_filename, "r") as word_file:
        words = [line.strip() for line in word_file]

    #  for word in sorted(words, key=lambda word: word.lower()):
    for word in sorted(words, key=str.casefold):
        print(f"|{word}|")


if __name__ == "__main__":
    main()
