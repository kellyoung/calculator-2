def add(num1, num2):
    return round(num1 + num2, 2)


def subtract(num1, num2):
    return round(num1 - num2, 2)


def multiply(num1, num2):
    return round(num1 * num2, 2)


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return round(float(num1) / float(num2), 2)


def square(num1):
    # Needs only one argument
    return round(num1 ** 2, 2)


def cube(num1):
    # Needs only one argument
    return round(num1 ** 3, 2)


def power(num1, num2):
    return round(num1 ** num2, 2)  # ** = exponent operator


def mod(num1, num2):
    return round(num1 % num2, 2)
