"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(x):
    x = str(x)
    return x == x[::-1]


def find_palindrome():
    for x in range(999, 900, -1):
        for y in range(999, 900, -1):  # type: int
            if is_palindrome(x * y):
                print 'Palindrome: ' + str(x * y)
                print 'x: ' + str(x)
                print 'y: ' + str(y)
                return


find_palindrome()