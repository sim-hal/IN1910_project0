def add(x, y):
    return x + y


def factorial(n):
    ans = 1
    ints_to_n = range(1, n + 1)
    for i in ints_to_n:
        ans *= i
    return ans


def sin(x, n):
    ans = 0
    for i in range(n + 1):
        ans += ((-1) ** i * x ** (2*i + 1))/factorial(2*i + 1)
    return ans


def divide(x, y):
    return x/y


def multiply(x, y):
    return x * y


def subtract(x, y):
    return x - y
