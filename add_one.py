"""
You are given a non-negative number in the form of list elements. For example,
the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

Example 1:

input = [1, 2, 3]
output = [1, 2, 4]
Example 2:

input = [1, 2, 9]
output = [1, 3, 0]
Example 3:

input = [9, 9, 9]
output = [1, 0, 0, 0]
Challenge: One way to solve this problem is to convert the input array into a number and then add one to it. For example,
if we have input = [1, 2, 3], you could solve this problem by creating the number 123 and then separating the digits of the output number 124.
"""
def add_one(arr):
    num = ''
    for val in arr:
        num += str(val)
    num = int(num) + 1
    list = print_arr_add_one(num)
    return list


def print_arr_add_one(arr):
    list = []
    size = 10**(len(str(arr))-1)
    while size > 0:
        digit = arr // size
        list.append(digit)
        arr = arr % size
        size //= 10
    return list



print(add_one([9, 9, 9]))
#print(print_arr_add_one(add_one([9, 9, 9])))