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

    with open(sys.argv[1], "r") as shape_file:
        shape_data = parse_shape_file(shape_file)


if __name__ == "__main__":
    main()
