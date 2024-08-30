'''

DESCRIPTOIN:

This challenge is to efficiently find the largest pronic number less than the method's input.

A pronic number is a composite number that is the product of two consecutive integers: n * (n + 1)

Sample pronic numbers:

6 = (2*3), 12 = (3*4), 20 = (4*5) ... 10100 = 100*101
The initial solution passes the sample tests, but fails for larger numbers used in the acceptance tests.

Your algorithm should be fast as the acceptance tests will run 10,000 randomly selected numbers.

Are you up to the challenge?
'''

import math


def next_smaller_pronic(n):
    my_sqroot = int(math.sqrt(n))
    return my_sqroot * (my_sqroot + 1) if my_sqroot * (my_sqroot + 1) < n else my_sqroot * (my_sqroot - 1)


print(next_smaller_pronic(6))
print(next_smaller_pronic(7))
print(next_smaller_pronic(8))
print(next_smaller_pronic(12))
print(next_smaller_pronic(22))
print(next_smaller_pronic(32))
print(next_smaller_pronic(112))
