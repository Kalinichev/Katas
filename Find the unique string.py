"""
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 2 strings.
"""


def find_uniq(arr):
    standard = set(arr[0].lower()) if set(arr[0].lower()) == set(arr[1].lower()) else set(arr[2].lower())
    for i in arr:
        if set(i.lower()) != standard:
            return i


print(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))
print(find_uniq(['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']))
