import math


def wall_surface_area(length: float, width: float) -> float:
    area_one_wall = length * width
    area_four_walls = 4 * area_one_wall

    return area_four_walls


def gallons_required(
    wall_area: float, min_coverage: float = 350, max_coverage: float = 400
) -> tuple[int, int]:
    max_gallons = math.ceil(wall_area / min_coverage)
    min_gallons = math.ceil(wall_area / max_coverage)

    return min_gallons, max_gallons
