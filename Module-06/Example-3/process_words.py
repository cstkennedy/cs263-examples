from __future__ import annotations

import sys
from typing import Iterable

DEFAULT_SYMBOL_BLACKLIST = (".", "+", "-")


def apply_word_filters(
    words: Iterable[str], symbol_blacklist: tuple[str, ...] = DEFAULT_SYMBOL_BLACKLIST
) -> Iterable[str]:
    """
    Take a collection of words and apply the following filters:

       1. skip empty strings

       2. skip noun phrases (i.e., any token that contains a space between two
          or more words, numbers, or symbols (e.g., Steam Deck).

       3. ignore any word that contains a ., +, or -
    """

    words = [word for word in words if word]

    words = [word for word in words if " " not in word]

    words = [
        word for word in words if not any(symbol in word for symbol in symbol_blacklist)
    ]

    return words


def main():
    word_filename = sys.argv[1]

    with open(word_filename, "r") as word_file:
        words = [line.strip() for line in word_file]

    filtered_words = apply_word_filters(words)
    for word in sorted(filtered_words, key=str.casefold):
        print(f"|{word}|")


if __name__ == "__main__":
    main()
