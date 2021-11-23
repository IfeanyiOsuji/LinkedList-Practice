import copy


def permute2(inputList):
    """
    Args: myList: list of items to be permuted
    Returns: list of permutation with each permuted item being represented by a list
    """
    if len(inputList) == 0:
        return [[]]
    first_el = inputList[0]
    after_first = slice(1, None)
    rest_el = inputList[after_first]

    combs_without_first = permute2(rest_el)
    combs_with_first = []
    for comb in combs_without_first:
        print(comb)
        comb_with_first = comb +list(first_el)
        combs_with_first.append(comb_with_first)
    return combs_without_first + combs_with_first


print(permute2(['a', 'b', 'c']))

"""
Question - Let's use recursion to help us solve the following permutation problem:

Given a list of items, the goal is to find all of the permutations of that list. For example,
Given a list like: [0, 1, 2]
Permutations: [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

Notice that the expected output is a list of permutation with each permuted item being represented by a list. Such an object that contains other object is called "compound" object.

The Idea
Build a compoundList incrementally starting with a blank list, and permute (add) each element of original input list at all possible positions.


For example, take [0, 1, 2] as the original input list:

Start with a blank compoundList [[]]. This is actually the last call of recursive function stack. Pick the element 2 of original input list, making the compoundList as [[2]]


Pick next element 1 of original input list, and add this element at position 0, and 1 for each list of previous compoundList. We will require to create copy of all lists of previous compoundList, and add the new element. Now, the compoundList will become [[1, 2], [2, 1]].


Pick next element 0 of original input list, and add this element at position 0, 1, and 2 for each list of previous compoundList. Now, the compoundList will become [[0, 1, 2], [1, 0, 2], [1, 2, 0], [0, 2, 1], [2, 0, 1], [2, 1, 0]] .
"""


def permute(inputList):
    totalCombination = []
    if len(inputList) == 0:
        totalCombination.append([])
    else:
        first_el = inputList[0]
        without_first_el = slice(1, None)
        rest_el = inputList[without_first_el]

        sub_combination = permute(rest_el)
        for element1_list in sub_combination:
            for j in range(0, len(element1_list)+1):
                element2_list = copy.deepcopy(element1_list)
                print(element2_list)
                element2_list.insert(j, first_el)
                totalCombination.append(element2_list)
    return totalCombination


print(permute([1, 2, 3]))
