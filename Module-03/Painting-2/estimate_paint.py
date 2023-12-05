import compute_paint


def get_report(min_gallons: int, max_gallons: int, price_per_gallon: float) -> str:
    if min_gallons == max_gallons:
        gallons = max_gallons
        cost = gallons * price_per_gallon

        return "\n".join(
            (
                f"You will need to buy {gallons} gallons of paint.",
                f"You will spend $ {cost:.2f}.",
            )
        )

    else:
        min_cost = min_gallons * price_per_gallon
        max_cost = max_gallons * price_per_gallon

        return "\n".join(
            (
                f"You will need to buy {min_gallons} to {max_gallons} gallons of paint.",
                f"You will spend $ {min_cost:.2f} to $ {max_cost:.2f}.",
            )
        )


def main():
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
