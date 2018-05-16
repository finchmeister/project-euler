"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2


def find_triplet():
    a = 1
    b = 2
    while a < 1000:
        while b < 1000:
            c = 1000 - b - a
            if is_pythagorean_triplet(a, b, c):
                return a, b, c
            b += 1
        a += 1
        b = a


def get_product(x):
    p = 1
    for i in x:
        p *= int(i)
    return p


print(get_product(find_triplet()))
