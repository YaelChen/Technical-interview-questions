"""1. give me python method that gets a sorted list of numbers
and returns 2 numbers that equal to input"""


def nums_from_list(sorted_list, target_num):
    """a function that gets a sorted list of numbers and an int,
    and returns two nums from the list that their sum is equal to the int input.
    :param: a list of ints and a number.
    :type: list, int
    :return: two numbers from the list
    :rtype: tup"""

    for first_num in sorted_list:
        second_num = target_num - first_num
        if second_num in sorted_list:
            return first_num, second_num
    return -1, -1


sortedlist = [1, 2, 3, 4, 5, 6, 7]
target = 7

print(nums_from_list(sortedlist, target))


"""2. Same as 1, but return a list with the 2 numbers"""


def numlist_from_list(sorted_list, target_num):
    """a function that gets a sorted list of numbers and an int,
    and returns a list of two nums from the list that their sum is equal to the int input.
    :param: a list of ints and a number.
    :type: list, int
    :return: a list of two numbers
    :rtype: list"""

    for first_num in sorted_list:
        second_num = target_num - first_num
        if second_num in sorted_list:
            return [first_num, second_num]
    return [-1, -1]


sortedlist = [1, 2, 3, 4, 5, 6, 7]
target = 13

print(numlist_from_list(sortedlist, target))

