from typing import TextIO, Generator
import sys
import pprint as pp


def parse_shape_file(input_file: TextIO) -> Generator[tuple[str, list[float]], None, None]:
    """
    Take each line from a given file (or file-like object) and split it into a
    tuple in the form

      (name, [val_1, val_2, ...])

    If a line is invalid (e.g., contains non-numeric values after the
    semicolon)... skip the line.
    """

    for line in input_file:
        # Remove leading and trailing whitespace
        line = line.strip()

        if not line:
            continue

        try:
            name, the_rest = line.split(";")
        except ValueError as _err:
            print(f"Missing ';' -> \"{line}\" is malformed.", file=sys.stderr)
            continue

        the_rest = the_rest.lstrip()
        the_rest = the_rest.split()

        try:
            numbers = [float(val) for val in the_rest]
        except ValueError as err:
            print(f"{err} -> \"{line}\" is malformed.", file=sys.stderr)
            continue

        yield (name, numbers)


def main():

    try:
        shape_filename = sys.argv[1]

    except IndexError as _err:
        print("Usage: exception_ex_5.py INPUT_FILENAME")
        sys.exit(1)

    try:
        with open(shape_filename, "r") as shape_file:
            shape_data = list(parse_shape_file(shape_file))

    except FileNotFoundError as err:
        print(err)
        sys.exit(2)

    #  print(shape_data)
    pp.pprint(shape_data, indent=2, width=72)


if __name__ == "__main__":
    main()
