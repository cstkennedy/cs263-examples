"""
This program generates a summary that contains the amount of paint required to
paint a room (in gallons) and the cost of that paint.
"""

import sys

import compute_paint

MIN_COATS: int = 2  # Minimum number of paint coats
MAX_COATS: int = 4  # Maximum number of paint coats


def get_report(
    min_gallons: int, max_gallons: int, price_per_gallon: float, indent: int = 0
) -> str:
    """
    Generate a summary of the amount of paint required to paint a room and the
    project cost of that paint.

    Args:
        min_gallons: estimate of the minimum amount of paint required
        max_gallons: estimate of the maximum amount of paint required

        price_per_gallon: cost for a single gallon of paint (e.g.,  for a
            single gallon or as part of a five gallon bucket)

        indent: number of spaces by which to indent each line of the report

    Returns:
        Summary of the estimated gallons of paint required if the min and max
        estimates are the same. Otherwise a report listing the min and max
        values is provided.
    """
    indent = " " * indent

    if min_gallons == max_gallons:
        gallons = max_gallons
        cost = gallons * price_per_gallon

        return "\n".join(
            (
                f"{indent}You will need to buy {gallons} gallons of paint.",
                f"{indent}You will spend $ {cost:.2f}.",
            )
        )

    min_cost = min_gallons * price_per_gallon
    max_cost = max_gallons * price_per_gallon

    return "\n".join(
        (
            f"{indent}You will need to buy {min_gallons} to {max_gallons} gallons of paint.",
            f"{indent}You will spend $ {min_cost:.2f} to $ {max_cost:.2f}.",
        )
    )


def gather_input(args: list[str]) -> tuple[float, float, float, float]:
    """
    Check the supplied `args` for four (4) user supplied arguments (for a total
    length of 4). If three arguments were not supplied then prompt the used for
    length (in feet), width (in feet), height (in feet), and price per gallon.

    Args:
        args: command line arguments to process

    Returns:
        a four-tuple in the form (length, width, height price_per_gallon)
    """

    # Command Line Arguments were supplied
    if len(args) == 5:
        length = float(args[1])
        width = float(args[2])
        height = float(args[3])

        price_per_gallon = float(args[3])

    else:
        length = float(input("Enter the room length: "))
        width = float(input("Enter the room width: "))
        height = float(input("Enter the room height: "))

        price_per_gallon = float(input("Enter the cost per gallon of paint:  "))

    return length, width, height, price_per_gallon


def main():
    """
    This is the driver logic for the program. The length, width, and price per
    gallon are currently hardcoded.

    TODO: add user input
    """

    length, width, height, price_per_gallon = gather_input(sys.argv)

    area = compute_paint.wall_surface_area(length, width, height)

    for num_coats in range(MIN_COATS, MAX_COATS + 1):
        total_area_painted = area * num_coats

        print(f"For {num_coats} coats...")

        min_required, max_required = compute_paint.gallons_required(total_area_painted)
        summary = get_report(min_required, max_required, price_per_gallon, indent=2)
        print(summary)
        print()


if __name__ == "__main__":
    main()
