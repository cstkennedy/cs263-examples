"""
This program generates a summary that contains the amount of paint required to
paint a room (in gallons) and the cost of that paint.
"""

import compute_paint


def get_report(min_gallons: int, max_gallons: int, price_per_gallon: float) -> str:
    """
    Generate a summary of the amount of paint required to paint a room and the
    project cost of that paint.

    Args:
        min_gallons: estimate of the minimum amount of paint required
        max_gallons: estimate of the maximum amount of paint required

        price_per_gallon: cost for a single gallon of paint (e.g.,  for a
            single gallon or as part of a five gallon bucket)

    Returns:
        Summary of the estimated gallons of paint required if the min and max
        estimates are the same. Otherwise a report listing the min and max
        values is provided.
    """

    if min_gallons == max_gallons:
        gallons = max_gallons
        cost = gallons * price_per_gallon

        return "\n".join(
            (
                f"You will need to buy {gallons} gallons of paint.",
                f"You will spend $ {cost:.2f}.",
            )
        )

    min_cost = min_gallons * price_per_gallon
    max_cost = max_gallons * price_per_gallon

    return "\n".join(
        (
            f"You will need to buy {min_gallons} to {max_gallons} gallons of paint.",
            f"You will spend $ {min_cost:.2f} to $ {max_cost:.2f}.",
        )
    )


def main():
    """
    This is the driver logic for the program. The length, width, and price per
    gallon are currently hardcoded.

    TODO: add user input
    """
    # Dimensions in feet
    length = 50
    width = 40

    # Price in dollars
    price_per_gallon = 49.95

    area = compute_paint.wall_surface_area(length, width)

    min_required, max_required = compute_paint.gallons_required(area)

    summary = get_report(min_required, max_required, price_per_gallon)
    print(summary)


if __name__ == "__main__":
    main()
