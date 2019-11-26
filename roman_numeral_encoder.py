"""
Convert an integer to roman numeral
"""

def solution(num):
    dct = { 1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: 
    "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M" }
    if(num in dct):
        return dct[num] # if its already defined, we're good
    for i in [1000,100,10,1]:
        for j in [9*i, 5*i, 4*i, i]:
            if(num>=j):
                return solution(j) + solution(num-j) # recursive function
