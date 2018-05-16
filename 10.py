"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def find_sum_of_primes_below_n(n):
    s = 0
    for x in xrange(1, n):
        if is_prime(x):
            s += x
    return s


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


print(find_sum_of_primes_below_n(2000000))
