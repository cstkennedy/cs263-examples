import pytest
from hamcrest import assert_that, close_to, equal_to

from compute_paint import gallons_required, wall_surface_area

test_data = [
    (1, 1, 4),
    (1, 2, 8),
    (2, 2, 16),
    (10, 12, 480),
    (10.5, 10, 420),
]


@pytest.mark.parametrize("length, width, surface_area", test_data)
def test_wall_surface_area(length, width, surface_area):
    assert_that(wall_surface_area(length, width), close_to(surface_area, 1e-1))


def test_gallons_required():
    assert_that(gallons_required(wall_area=1), equal_to((1, 1)))
    assert_that(gallons_required(wall_area=10), equal_to((1, 1)))
    assert_that(gallons_required(wall_area=100), equal_to((1, 1)))
    assert_that(gallons_required(wall_area=1_000), equal_to((3, 3)))
    assert_that(gallons_required(wall_area=1_050), equal_to((3, 3)))
    assert_that(gallons_required(wall_area=1_200), equal_to((3, 4)))
