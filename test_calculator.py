import calculator

epsilon = 1e-10


def test_add():
    assert abs(calculator.add(0.2, 0.1) - 0.3) < epsilon
