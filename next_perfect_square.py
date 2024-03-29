"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
"""

import math
def find_next_square(sq):
    """
    if ( a number is a perfect square ), 
    return the next perfect square
    else return -1
    btw: check your libraries. was getting a weird zerodivisonerror
    sometimes
    """
       
    root = math.sqrt(sq)  # get square root
    if int(root + 0.5) ** 2 == sq:  # is a perfect square
        if int(sq) % int(sq) ** 0.5 == 0.0:  # in python3, must use float(0.0)
            return math.pow((math.sqrt(sq) + 1), 2)  # calculate next perfect square
    else:
        return -1  # otherwise return -1
