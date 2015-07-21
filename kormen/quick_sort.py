__author__ = 'art'

def sort(list_for_sort, index1, index2):
    """
    :param list_for_sort:
    :param index1:
    :param index2:
    :return:
    """
    if index1 < index2:
        new_index = partition(list_for_sort, index1, index2)
        sort(list_for_sort, index1, new_index - 1)
        sort(list_for_sort, new_index + 1, index2)


def partition(list_for_sort, index1, index2):
    """
    :param list_for_sort:
    :param index1:
    :param index2:
    :return:
    """
    sort_element = list_for_sort[index2]
    curr_index = index1 - 1
    for index in range(index1, index2):
        if list_for_sort[index] <= sort_element:
            curr_index += 1
            if curr_index != index:
                change = list_for_sort[curr_index]
                list_for_sort[curr_index] = list_for_sort[index]
                list_for_sort[index] = change
    curr_index += 1
    change = list_for_sort[curr_index]
    list_for_sort[curr_index] = list_for_sort[index2]
    list_for_sort[index2] = change
    return curr_index

