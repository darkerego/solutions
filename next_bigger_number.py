"""
You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

12 ==> 21
513 ==> 531
2017 ==> 2071

If no bigger number can be composed using those digits, return -1:

9 ==> -1
111 ==> -1
531 ==> -1


"""

from itertools import permutations
"""def next_bigger(n):
    for next in sorted(list(set([int(''.join(x)) for x in permutations(str(n), len(str(n)))]))):
        if next > n:
           return next
    return -1"""
def next_bigger(num):
    ints = [int(i) for i in str(num)]
    _index = len(ints) - 1
    while _index >= 1 and ints[_index-1] >= ints[_index]:
        _index -= 1
    if _index == 0:
        return -1
    pivot = ints[_index-1]
    rev__index = len(ints) - 1
    while pivot >= ints[rev__index]:
        rev__index -= 1
    ints[rev__index], ints[_index-1] = ints[_index-1], ints[rev__index]
    ints[_index:] = ints[:_index-1:-1]
    return int(''.join(str(x) for x in ints))
