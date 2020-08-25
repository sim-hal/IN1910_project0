import calculator
from math import pi

epsilon = 1e-10


def test_add():
    expected = 0.3
    actual = calculator.add(0.2, 0.1)
    assert abs(actual - expected) < epsilon


def test_add_strings():
    expected = "hello world"
    actual = calculator.add("hello ", "world")
    assert actual == expected


def test_factorial():
    expected = 720
    actual = calculator.factorial(6)
    assert abs(expected - actual) < epsilon


def test_sin():
    expected = 1
    actual = calculator.sin(pi/2, 10)
    assert abs(expected - actual) < epsilon


def test_divide():
    expected = 3.5
    actual = calculator.divide(7, 2)
    assert abs(expected - actual) < epsilon


def test_multiply():
    expected = 14
    actual = calculator.multiply(7, 2)
    assert abs(expected - actual) < epsilon


def test_subtract():
    expected = 5
    actual = calculator.subtract(7, 2)
    assert abs(expected - actual) < epsilon
