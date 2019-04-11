

"""Math functions for calculator."""


def add(numbers):
    """Return the sum of the two inputs."""
    counter = 0
    for num in numbers:
        counter += num
    return counter


def subtract(numbers):
    """Return the second number subtracted from the first."""
    counter = 0
    for num in numbers:
        counter -= num
    return counter


def multiply(numbers):
    """Multiply the two inputs together."""
    counter = 0
    for num in numbers:
        counter *= num
    return counter

def divide(numbers):
    """Divide the first input by the second, returning a floating point."""
    counter = 0
    for num in numbers:
        counter /= num
    return counter


def square(numbers):
    """Return the square of the input."""

    # Needs only one argument
    newlist = []
    for num in numbers:
        newlist.append(num*num)
    return newlist


def cube(numbers):
    """Return the cube of the input."""

    # Needs only one argument
    newlist = []
    for num in numbers:
        newlist.append(num*num*num)
    return newlist

    # return num1 * num1 * num1


def power(numbers):
    """Raise num1 to the power of num and return the value."""
    if len(numbers) % 2 == 1: 
        print('too few numbers, should be even')
    newlist = []
    for i in range(len(numbers)):
        newlist.append(i ** i+1)
    return newlist

    # return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2



 # ----------------------------------------------------

    # user_input = input("User input: ")
    # token = user_input.split(" ")

    # for elem in range(len(token)):


