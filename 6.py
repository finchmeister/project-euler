"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_of_squares(n):
    x = 0
    for i in xrange(n+1):
        x += i**2
    return x


def square_of_sum(n):
    x = 0
    for i in xrange(n + 1):
        x += i
    return x**2


def difference_between_square_of_sum_and_sum_of_squares(n):
    return square_of_sum(n) - sum_of_squares(n)


print difference_between_square_of_sum_and_sum_of_squares(100)
