import pytest

from hamcrest import *

from compute_paint import (wall_surface_area, gallons_required)


def test_wall_surface_area():
    assert_that(wall_surface_area(1, 1), equal_to(4))
    assert_that(wall_surface_area(1, 2), equal_to(8))
    assert_that(wall_surface_area(2, 2), equal_to(16))

    assert_that(wall_surface_area(10, 12), close_to(480, 1e-1))
    assert_that(wall_surface_area(10.5, 10), close_to(420, 1e-1))

test_data = [
    (1, 1, 4),
    (1, 2, 8),
    (2, 2, 16),
    (10, 12, 480),
    (10.5, 10, 420),
]

@pytest.mark.parametrize("length, width, surface_area", test_data)
def test_wall_surface_area_p(length, width, surface_area):
    assert_that(wall_surface_area(length, width), close_to(surface_area, 1e-1))


def test_gallons_required():
    lower, upper = gallons_required(wall_area=1)
    assert_that(lower, equal_to(1))
    assert_that(upper, equal_to(1))

    lower, upper = gallons_required(wall_area=10)
    assert_that(lower, equal_to(1))
    assert_that(upper, equal_to(1))

    lower, upper = gallons_required(wall_area=100)
    assert_that(lower, equal_to(1))
    assert_that(upper, equal_to(1))

    lower, upper = gallons_required(wall_area=1_000)
    assert_that(lower, equal_to(3))
    assert_that(upper, equal_to(3))

    lower, upper = gallons_required(wall_area=1_050)
    assert_that(lower, equal_to(3))
    assert_that(upper, equal_to(3))

    lower, upper = gallons_required(wall_area=1200)
    assert_that(lower, equal_to(3))
    assert_that(upper, equal_to(4))
