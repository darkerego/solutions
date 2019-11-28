"""
Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark.

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
"""

def dashatize(num):
    """ Gross and hacky, i know, i know
    """
    if num is None:
        return 'None'
    if num == 0:
        return '0'
    num = str(num)
    num = num.strip('-')
    ret = ''
    c = 0
    for digit in str(num):
        if int(digit) % 2 != 0:
            if c == 0 and len(str(num)) == 1:
                ret += digit
            elif c == 0 and len(str(num)) > 1:
                ret += digit + '-'
            elif c == len(str(num)) -1:
                ret += '-' + digit
            else:
                ret += '-' + digit + '-'
        else:
            ret += digit
        c += 1
    ret = ret.replace('--', '-')
    return ret
