"""
This module provides functions to compute how much paint is needed to paint a
room, including paint coverage and wall surface area.
"""

import math


def wall_surface_area(length: float, width: float) -> float:
    """
    Compute the surface area of all four walls in a room. For the purposes of
    this estimation... it is assumed that

      1. each wall is a rectangle with no doorways or windows
      2. there are four (4) walls in the room

    Args:
        length: room length
        width: room width

    Returns:
        Wall surface area for a single room
    """

    area_one_wall = length * width
    area_four_walls = 4 * area_one_wall

    return area_four_walls


def gallons_required(
    wall_area: float, min_coverage: float = 350, max_coverage: float = 400
) -> tuple[int, int]:
    """
    Compute the number of gallons of paint required for a given surface area.

    Args:
        wall_area: surface area to be covered
        min_coverage: minimum area covered by a gallon of paint
        max_coverage: maximum area covered by a gallon of paint

    Returns:
        minimum and maximum gallons of paint required rounded up to the next
        whole gallon.
    """

    max_gallons = math.ceil(wall_area / min_coverage)
    min_gallons = math.ceil(wall_area / max_coverage)

    return min_gallons, max_gallons
