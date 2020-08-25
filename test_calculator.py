import calculator
from math import pi
import pytest

epsilon = 1e-10


def test_add_exercise_1():
    expected = 0.3
    actual = calculator.add_exercise_1(0.2, 0.1)
    assert abs(actual - expected) < epsilon


def test_add_strings_exercise_3():
    expected = "hello world"
    actual = calculator.add_exercise_1("hello ", "world")
    assert actual == expected


def test_factorial__exercise_4():
    expected = 720
    actual = calculator.factorial_exercise_4(6)
    assert abs(expected - actual) < epsilon


def test_sin_exercise_4():
    expected = 1
    actual = calculator.sin_exercise_4(pi/2, 10)
    assert abs(expected - actual) < epsilon


def test_divide_exercise_4():
    expected = 3.5
    actual = calculator.divide_exercise_4(7, 2)
    assert abs(expected - actual) < epsilon


def test_multiply_exercise_4():
    expected = 14
    actual = calculator.multiply_exercise_4(7, 2)
    assert abs(expected - actual) < epsilon


def test_subtract_exercise_4():
    expected = 5
    actual = calculator.subtract_exercise_4(7, 2)
    assert abs(expected - actual) < epsilon


def test_add_raises_TypeError_exercise_5():
    with pytest.raises(TypeError):
        calculator.add_exercise_1(4, "Hei verden")


def test_divide_raises_ZeroDivisionError_exercise_5():
    with pytest.raises(ZeroDivisionError):
        calculator.divide_exercise_4(4, 0)
