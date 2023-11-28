from typing import TextIO
import sys


def parse_shape_file(input_file: TextIO) -> list[tuple[str, list[float]]]:

    for line in input_file:
        # Remove leading and trailing whitespace
        line = line.strip()

        if not line:
            continue

        print(line)

    return []


def main():

    try:
        shape_filename = sys.argv[1]

    except IndexError as _err:
        print("Usage: exception_ex_5.py INPUT_FILENAME")
        sys.exit(1)

    try:
        with open(shape_filename, "r") as shape_file:
            shape_data = parse_shape_file(shape_file)

    except FileNotFoundError as err:
        print(err)
        sys.exit(2)


if __name__ == "__main__":
    main()
