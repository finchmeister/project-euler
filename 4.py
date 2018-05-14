"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(x):
    x = str(x)
    return x == x[::-1]

"""
Start at 999, 999
two loops iterating down
"""

