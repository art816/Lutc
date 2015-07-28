__author__ = 'art'

import copy

def sort(A):
    pass

def create_help_massive(A, k):
    """

    :param A:
    :return:
    """
    # num_different_elements = max(A)
    num_different_elements = k
    help_massive = []
    help_dict = dict()
    dict_keys = []
    for i in range(num_different_elements + 1):
        help_massive.append(0)
    for element in A:
        help_massive[element] += 1

    for element in A:
        if element in dict_keys:
            help_dict[element] += 1
        else:
            help_dict[element] = 1
            dict_keys.append(element)
    return help_massive, help_dict

def num_les_element(A, B):
    """

    :param A:
    :return:
    """
    for i in range(1, len(A)):
        A[i] += A[i - 1]
    list_index = sorted(B.keys())
    less_index = list_index.pop(0) if list_index else None
    for i in list_index:
        B[i] += B[less_index]
        less_index = i


def sort(A, k):
    """

    :param A:
    :return:
    """
    help_massive, help_dict = create_help_massive(A, k)
    num_les_element(help_massive, help_dict)
    res = copy.copy(A)
    res2 = copy.copy(A)
    # res2 = []
    for i in range(-len(A) + 1, 1):
        i = abs(i)
        res[help_massive[A[i]] - 1] = A[i]
        help_massive[A[i]] -= 1
    for i in range(-len(A) + 1, 1):
        i = abs(i)
        res2[help_dict[A[i]] - 1] = A[i]
        help_dict[A[i]] -= 1
    return res, res2