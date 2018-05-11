import math

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def largest_prime_factor(x):
    sqrt = int(math.sqrt(x))
    i = sqrt
    while i > 1:
        if x % i == 0 and is_prime(i):
            return i
        i = i - 1


def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i = i + 6
    return True


print(largest_prime_factor(600851475143))
