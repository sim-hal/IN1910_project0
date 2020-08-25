import calculator

epsilon = 1e-10


def test_add():
    expected = 0.3
    actual = calculator.add(0.2, 0.1)
    assert abs(actual - expected) < epsilon
