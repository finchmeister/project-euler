import math


def largest_prime_factor(x):
    sqrt = int(math.sqrt(x))
    i = 0
    while sqrt - i > 1:
        if x % (sqrt - i) == 0 and is_prime(sqrt - i):
            return sqrt - i
        i = i + 1


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
