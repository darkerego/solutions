"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.

"""

def accum(s):
    """ Input a string like "abc"
    and return a string like "A-Bb-Ccc"
    """
    count2 = 0
    count = 0
    k = len(s)
    final_str = ""
    for i in range(len(s)):
        final_str += (s[count].upper())
        for z in range(count2):
            final_str +=(s[count].lower())
        count2 += 1
        count += 1
        if k > 1:
            final_str += ("-")
            k -= 1
    return str(final_str)
