from __future__ import annotations

import sys


def main():
    word_filename = sys.argv[1]

    with open(word_filename, "r") as word_file:
        words = [line.strip() for line in word_file]

    # Grab all tokens that are not an empty string
    words = [word for word in words if word]

    # Grab all words that do not contain a space
    words = [word for word in words if " " not in word]

    # Grab all words that do not contain a ., +, or -
    symbol_blacklist = [".", "+", "-"]
    words = [word for word in words if all(symbol not in word for symbol in symbol_blacklist)]

    for word in sorted(words, key=str.casefold):
        print(f"|{word}|")


if __name__ == "__main__":
    main()
