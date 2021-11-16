"""
Problem Statement
You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

Example 1:

arr= [1, 2, 3, -4, 6]
The largest sum is 8, which is the sum of all elements of the array.
Example 2:

arr = [1, 2, -5, -4, 1, 6]
The largest sum is 7, which is the sum of the last two elements of the array.
"""

def max_sum_sub_array2(arr):
    highest = 0
    for i in arr:
        highest+= i
    return highest


""" checks for max contigious until a negative value"""
def max_sum_sub_array(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for i in arr[1:]:
        current_sum += i
        if i > current_sum:
            current_sum = i
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
arr= [1, 2, 3, -4, 6]
arr1 = [1, 2, -5, -4, 1, 6]
print(max_sum_sub_array(arr1))



