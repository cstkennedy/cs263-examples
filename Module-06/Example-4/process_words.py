from __future__ import annotations

import sys
from string import ascii_lowercase
from typing import Iterable

DEFAULT_SYMBOL_BLACKLIST = (".", "+", "-")


def apply_word_filters(
    words: Iterable[str], symbol_blacklist: tuple[str] = DEFAULT_SYMBOL_BLACKLIST
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

    words_sorted_lex = sorted(filtered_words, key=str.casefold)
    words_sorted_len = sorted(filtered_words, key=len)

    for word_lhs, word_rhs in zip(words_sorted_lex, words_sorted_len):
        print(f"| {word_lhs:<18} | {word_rhs:<18} |")

    print()
    print("Top 3 Longest Words:")
    print()
    for word in reversed(words_sorted_len[-3:]):
        print(f"  {word}")

    print()
    print("Longest Word By Letter:")
    print()

    for letter in ascii_lowercase:
        try:
            longest_word = max(
                word for word in words if word.lower().startswith(letter)
            )

        except ValueError as _err:
            # There were words that started with "letter"
            # There is nothing to output
            continue

        print(f"  ({letter}) - {longest_word}")

    print()
    print("Shortest Word By Letter:")
    print()

    for letter in ascii_lowercase:
        try:
            shortest_word = min(
                word for word in words if word.lower().startswith(letter)
            )

        except ValueError as _err:
            # There were words that started with "letter"
            # There is nothing to output
            continue

        print(f"  ({letter}) - {shortest_word}")


if __name__ == "__main__":
    main()
