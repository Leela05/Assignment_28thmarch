import Prgm2
import pytest

def test_area():
    length = 20
    width = 10
    height = 30
    result = Prgm2.area(length, width, height)
    assert result == 2*((width*length)+(height*length)+(height*width))

def test_volume():
    length = 20
    width = 10
    height = 30
    result = Prgm2.volume(length, width, height)
    assert result == length*width*height

def test_spaceDiagonal():
    length = 20
    width = 10
    height = 30
    diagonal = ((length * length) + (width * width) + (height * height))
    result = Prgm2.spaceDiagonal(length, width, height)
    assert result == diagonal ** 0.5




