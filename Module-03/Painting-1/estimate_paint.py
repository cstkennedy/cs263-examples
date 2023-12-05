import math

def compute_wall_surface_area(length: float, width: float) -> float:

    area_one_wall = length * width
    area_four_walls = 4 * area_one_wall

    return area_four_walls


def determine_gallons_required(
    wall_area: float, min_coverage: float = 350, max_coverage = 400
) -> tuple[int, int]:

    max_gallons = math.ceil(wall_area / min_coverage)
    min_gallons = math.ceil(wall_area / max_coverage)

    return min_gallons, max_gallons


def main():
    # Dimensions in feet
    length = 50
    width = 40

    # Price in dollars
    price_per_gallon = 49.95

    area = compute_wall_surface_area(length, width)

    gallons_required = determine_gallons_required(area)

    min_required, max_required = gallons_required
    min_cost = min_required * price_per_gallon
    max_cost = max_required * price_per_gallon

    print(f"You will need to buy {min_required} to {max_required} gallons of paint.")
    print(f"You will spend $ {min_cost:.2f} to $ {max_cost:.2f}")


if __name__ == "__main__":
    main()
