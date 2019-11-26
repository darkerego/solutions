"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Notes:

    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space, and highest number is first.


"""


def high_and_low(numbers):
    """
    :param: numbers: tuple of numbers supplied
    :return: highest number + ' ' + lowest number
    """

    n = []  # create a list
    numbers = numbers.split(' ')  # split numbers by space
    #  print(numbers) #  leftover code from debugging
    for i in numbers:
        n.append(int(i))  # create a list of numbers so we can ...
    low = min(n)  # find the lowest
    high = max(n)  # and the highest
    return str("%d %d" % (high, low))  # return a string with instructed output
