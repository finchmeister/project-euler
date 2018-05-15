"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""


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


def find_nth_prime(n):
    i = 0
    k = 1
    while True:
        if is_prime(k):
            i += 1
            # print ('i: %d, p: %d' % (i, k))
            if i == n:
                return k
        k += 1


print find_nth_prime(10001)
