"""
DESCRIPTOIN:

Your task is to find the next higher number (int) with same '1'- Bits.

I.e. as much 1 bits as before and output next higher than input. Input is always an int in between 1 and 1<<30 (inclusive). No bad cases or special tricks...

Some easy examples:
Input: 129  => Output: 130 (10000001 => 10000010)
Input: 127 => Output: 191 (01111111 => 10111111)
Input: 1 => Output: 2 (01 => 10)
Input: 323423 => Output: 323439 (1001110111101011111 => 1001110111101101111)
First some static tests, later on many random tests too;-)!

Hope you have fun! :-)
"""


def next_higher(n):
    n = ['0'] + list(bin(n)[2:])
    first_one_pos = len(n) - n[::-1].index('1') - 1
    for index, item in enumerate(n[:first_one_pos]):
        if item == '0':
            zero_after_one = index
    n = n[:zero_after_one] + ['1'] + ['0'] + (n[zero_after_one + 1:].count('0')) * ['0'] + (
            n[zero_after_one + 1:].count('1') - 1) * ['1']
    return int(''.join(n), 2)


print(next_higher(127))
print(next_higher(128))
print(next_higher(129))
print(next_higher(130))
print(next_higher(1022))
print(next_higher(681707164))
