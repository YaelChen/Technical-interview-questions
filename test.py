"""1. give me Python method that gets a sorted list of numbers
and returns 2 numbers that equal to input"""



def nums_from_list(numlist, target_num):
    """a function that gets a list of numbers and an int,
    and returns two nums from the list whose sum is equal to the int input.
    :param: a list of ints and a number.
    :type: list, int
    :return: two numbers from the list
    :rtype: tup"""

    for first_num in numlist:
        second_num = target_num - first_num
        templist = numlist.copy()
        templist.remove(first_num)
        if second_num in templist:
            return first_num, second_num
    return -1, -1


unsortedlist = [32, 24, 4, 7, 12, 9, 18, 2, 8, 40, 6, 2, 3, 1]
target = 80

print(nums_from_list(unsortedlist, target))


"""2. Same as 1, but return a list with the 2 numbers"""


def numlist_from_list(numlist, target_num):
    """a function that gets a sorted list of numbers and an int,
    and returns a list of two nums from the list whose sum is equal to the int input.
    :param: a list of ints and a number.
    :type: list, int
    :return: a list of two numbers
    :rtype: list"""

    for first_num in numlist:
        second_num = target_num - first_num
        templist = numlist.copy()
        templist.remove(first_num)
        if second_num in templist:
            return [first_num, second_num]
    return [-1, -1]


unsortedlist = [32, 24, 4, 7, 12, 9, 18, 2, 8, 40, 6, 2, 3, 1]
target = 13

print(numlist_from_list(unsortedlist, target))

