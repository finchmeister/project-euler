"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def is_divisible(x, up_to=20):
    for y in xrange(up_to, 1, -1):
        if x % y != 0:
            return False
    return True


def find_smallest_evenly_divisible(up_to=20):
    i = up_to
    while is_divisible(i, up_to) is False:
        i += up_to
    return i


print(find_smallest_evenly_divisible())
