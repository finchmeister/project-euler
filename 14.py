"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

"""
Observations
- eventually a number will be 2^x, then it will terminate in x+1
- once we get to a number in the series we have completed before, we will know deterministically how many terms remain
- 3n+1 = 2^x will terminate in x+1
"""


def get_n_1(n):
    return n / 2 if n % 2 == 0 else 3 * n + 1


def get_longest_chain(x_max):
    chain = {}
    for x in xrange(1, x_max):
        n = x
        i = 1
        while n != 1:
            if n is chain:
                i += chain[n]
            else:
                n = get_n_1(n)
                i += 1
        chain[x] = i
    x = get_key_of_max_from_dict(chain)
    return x


def get_key_of_max_from_dict(dict):
    return max(dict, key=dict.get)


print(get_longest_chain(1000000))
