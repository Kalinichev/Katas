"""
Given a string, determine if it's a valid identifier.

Here is the syntax for valid identifiers:
Each identifier must have at least one character.
The first character must be picked from: alpha, underscore, or dollar sign. The first character cannot be a digit.
The rest of the characters (besides the first) can be from: alpha, digit, underscore, or dollar sign. In other words,
it can be any valid identifier character.

Examples of valid identifiers:
i
wo_rd
b2h
Examples of invalid identifiers:
1i
wo rd
!b2h
"""


def is_valid(idn):
    if idn:
        if idn[0].isalpha() or idn[0] in ['_', '$']:
            for i in idn[1:]:
                if not (i.isalpha() or i.isdigit() or i in ['_', '$']):
                    return False
            return True
    return False


print(is_valid('b2h'))
