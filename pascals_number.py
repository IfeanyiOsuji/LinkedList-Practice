"""
Problem Statement
Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.

For example, if n = 4, then output = [1, 4, 6, 4, 1].

To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html
"""


def nth_row_pascal(n):
    #list1 = []

    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    number = 11 ** n
    list1 = [int(x) for x in str(number)]
    # num_power = 10 ** (len(str(number))-1)
    # print(num_power)
    # while number > 0:
    #     digit = number // num_power
    #     list1.append(digit)
    #     number = number % num_power
    #     num_power = num_power//10
    return list1
print(nth_row_pascal(4))