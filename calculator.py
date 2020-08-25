def add_exercise_1(x, y):
    return x + y


def factorial_exercise_4(n):
    ans = 1
    ints_to_n = range(1, n + 1)
    for i in ints_to_n:
        ans *= i
    return ans


def sin_exercise_4(x, n):
    ans = 0
    for i in range(n + 1):
        ans += ((-1) ** i * x ** (2*i + 1))/factorial_exercise_4(2*i + 1)
    return ans


def divide_exercise_4(x, y):
    return x/y


def multiply_exercise_4(x, y):
    return x * y


def subtract_exercise_4(x, y):
    return x - y
