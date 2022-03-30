import area
import pytest

def test_area_of_rectangle():
    length = 20
    breadth = 10
    result = area.area_of_rectangle(length, breadth)
    assert result == length * breadth

def test_perimeter_of_rectangle():
    length = 4
    breadth = 5
    result = area.perimeter_of_rectangle(length, breadth)
    assert result == 2*(length+breadth)

def test_area_of_circle():
    radius = 2
    result = area.area_of_circle(radius)
    assert result == 3.14*radius*radius

def test_area_of_square():
    side = 3
    result = area.area_of_square(side)
    assert result == side * side

def test_area_of_triangle():
    breadth = 4
    height = 5
    result = area.area_of_triangle(breadth, height)
    assert result == 1/2*(breadth*height)