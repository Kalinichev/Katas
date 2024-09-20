"""

DESCRIPTOIN:

Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with
all of the integer's divisors(except for 1 and the number itself), from smallest to largest.
If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL)
(use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Examples:
divisors(12) --> [2, 3, 4, 6]
divisors(25) --> [5]
divisors(13) --> "13 is prime"
"""


def divisors(integer):
    answer = [i for i in range(2, int(integer ** 0.5) + 1) if integer % i == 0]
    for i in answer[:]:
        if int(integer / i) not in answer:
            answer.append(int(integer / i))
    return sorted(answer) if answer else f'{integer} is prime'


