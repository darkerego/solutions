"""
Detect a panagram
"""

import string

def is_pangram(s):
    ascii_map = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if s.lower() == 'abcdefghijklmopqrstuvwxyz': # this is not a panagram I guess ... 
        return False
    for i in ascii_map:  # for every letter in the string
        if i in s.lower(): # if letter in string, ret is true (ignore case)
            ret = True
        else:
            ret = False # if a letter does not exist, it's not a panagram
    return ret # return ret
