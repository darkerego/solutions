"""
Write a function that given an integer, returns a diamond, such as `diamond(9)`:

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

If the number is even or negative, returrn None. 
"""

def diamond(n):
    # Make some diamonds!
    if n % 2 == 0 or n < 1:
        return None
    height = (n+1)//2
    ret = ''
    #  rows from 1 to height of diamond
    for row in range(1, height):
        stars = (row * 2) -1
        spaces = height - row
        ret += (' ' * spaces) + ("*" * stars) + "\n"
    ret += '*' * n + '\n'  # height ('tallest' row)
    # rows after height (reversed algo)
    for row in range(height + 1, n + 1):
        stars = ((n+1 - row) * 2) -1
        spaces = row - height
        ret += (' ' * spaces) + ("*" * stars) + "\n"
    return ret

print(diamond(9))
