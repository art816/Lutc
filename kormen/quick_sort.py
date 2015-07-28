__author__ = 'art'
import random

def sort(list_for_sort, index1, index2):
    """
    :param list_for_sort:
    :param index1:
    :param index2:
    :return:
    """
    if index1 < index2:
        new_index1, new_index2 = partition(list_for_sort, index1, index2)
        sort(list_for_sort, index1, new_index1 - 1)
        sort(list_for_sort, new_index2 + 1, index2)


def partition(list_for_sort, index1, index2):
    """
    :param list_for_sort:
    :param index1:
    :param index2:
    :return:
    """
    index = random.randint(index1, index2)
    change = list_for_sort[index2]
    list_for_sort[index2] = list_for_sort[index]
    list_for_sort[index] = change
    sort_element = list_for_sort[index2]
    curr_index = index1 - 1
    curr_equal = None
    for index in range(index1, index2):
        if list_for_sort[index] < sort_element:
            curr_index += 1
            if curr_index != index:
                change = list_for_sort[curr_index]
                list_for_sort[curr_index] = list_for_sort[index]
                list_for_sort[index] = change

        if list_for_sort[index] == sort_element:
            if curr_equal is None:
                curr_equal = curr_index + 1
            else:
                curr_equal += 1
            change = list_for_sort[index]
            list_for_sort[index] = list_for_sort[curr_equal]
            list_for_sort[curr_equal] = change
        # print(list_for_sort, index, curr_index, curr_equal, sort_element)

    curr_index += 1
    if curr_equal is not None:
        curr_equal += 1
        change_index = curr_equal
    else:
        change_index = curr_index
    change = list_for_sort[change_index]
    list_for_sort[change_index] = list_for_sort[index2]
    list_for_sort[index2] = change
    return curr_index, curr_equal or curr_index

