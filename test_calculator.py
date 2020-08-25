import calculator
from math import pi
import pytest

epsilon = 1e-10


@pytest.mark.parametrize("x, y, ans", [(0.2, 0.1, 0.3), (1, 1, 2), (1/3, 1/3, 2/3), (3, 6, 9)])
def test_add_exercise_1(x, y, ans):
    expected = ans
    actual = calculator.add_exercise_1(x, y)
    assert abs(actual - expected) < epsilon


@pytest.mark.parametrize("x, y, ans", [("Hello ", "world", "Hello world"), ("1", "1", "11"), ("Hei", "Verden", "HeiVerden")])
def test_add_strings_exercise_3(x, y, ans):
    expected = ans
    actual = calculator.add_exercise_1(x, y)
    assert actual == expected


@pytest.mark.parametrize("n, ans", [(1, 1), (2, 2), (6, 720)])
def test_factorial__exercise_4(n, ans):
    expected = ans
    actual = calculator.factorial_exercise_4(n)
    assert abs(expected - actual) < epsilon


@pytest.mark.parametrize("x, ans", [(0, 0), (pi/2, 1), (pi, 0)])
def test_sin_exercise_4(x, ans):
    expected = ans
    actual = calculator.sin_exercise_4(x, 10)
    assert abs(expected - actual) < epsilon


@pytest.mark.parametrize("x, y, ans", [(1, 1, 1), (3, 2, 1.5), (7, 2, 3.5)])
def test_divide_exercise_4(x, y, ans):
    expected = ans
    actual = calculator.divide_exercise_4(x, y)
    assert abs(expected - actual) < epsilon


@pytest.mark.parametrize("x, y, ans", [(1, 1, 1), (3, 2, 6), (7, 2, 14)])
def test_multiply_exercise_4(x, y, ans):
    expected = ans
    actual = calculator.multiply_exercise_4(x, y)
    assert abs(expected - actual) < epsilon


@pytest.mark.parametrize("x, y, ans", [(1, 1, 0), (0.001, 0.0001, 0.0009), (7, 2, 5)])
def test_subtract_exercise_4(x, y, ans):
    expected = ans
    actual = calculator.subtract_exercise_4(x, y)
    assert abs(expected - actual) < epsilon


@pytest.mark.parametrize("x, y", [(1, "hei verden"), (0.001, "0.001"), ("3", 5)])
def test_add_raises_TypeError_exercise_5(x, y):
    with pytest.raises(TypeError):
        calculator.add_exercise_1(x, y)


@pytest.mark.parametrize("x, y", [(1, 0), (0.001, 0), (6, 0)])
def test_divide_raises_ZeroDivisionError_exercise_5(x, y):
    with pytest.raises(ZeroDivisionError):
        calculator.divide_exercise_4(x, y)
