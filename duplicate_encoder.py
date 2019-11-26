"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
Examples

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
"""

def duplicate_encode(word):
    """
    :param word: string to process
    :return: encoded string
    """
    ret = ''
    from collections import Counter
    count = Counter(word.lower())
    for char in word.lower():
        if count[char] == 1:
            ret += '('
        if count[char] > 1:
            ret += ')'
    return ret
