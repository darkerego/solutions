"""
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

"""

def iq_test(numbers):
    n = []  # define a list for numbers
    odds = []  # empty list for odd position
    evens = []  # empty list for even position (could also be an integer variable
    for x in numbers.split(' '):
        n.append(int(x))  # append actual integers
    count_odd = 0  # variables for odds, evens, and totals (start at 1)
    count_even = 0
    count_total = 1
    for x in n:
        if int(x) % 2 == 0:
            count_even += 1  # if its an even, store position of number
            evens.append(count_total)
        if int(x) % 2 != 0:
            count_odd += 1
            odds.append(count_total) # same with odd
        count_total += 1
    if count_odd < count_even:  # if we have more events than odds, return the odd number
        return odds[0]
    if count_odd > count_even:  # same here
        return evens[0]
