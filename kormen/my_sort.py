__author__ = 'art'


def sort_pass(a_list):
    """Sorted by pass"""
    sort_list = list(a_list)
    # recurs_pass(sort_list, len(sort_list)-1)
    for ind in range(1, len(sort_list)):
        key = sort_list[ind]
        new_ind = ind - 1
        while new_ind >= 0 and sort_list[new_ind] > key:
            sort_list[new_ind + 1] = sort_list[new_ind]
            new_ind -= 1
        sort_list[new_ind + 1] = key
    return sort_list


def recurs_pass(sort_list, end_ind):
    """"""
    if end_ind > 0:
        recurs_pass(sort_list, end_ind-1)
        key = sort_list[end_ind]
        new_ind = end_ind - 1
        while new_ind >= 0 and sort_list[new_ind] > key:
            sort_list[new_ind + 1] = sort_list[new_ind]
            new_ind -= 1
        sort_list[new_ind + 1] = key


def sort_select(a_list):
    """Sorted by select"""
    sort_list = list(a_list)
    new_list = []
    for ind in range(0, len(sort_list)):
        new_list.append(sort_list.pop(sort_list.index(min_lin(sort_list))))
    return new_list


def min_lin(sort_list):
    """Lineal find"""
    min_element = sort_list[0]
    for i in range(1, len(sort_list)):
        min_element = sort_list[i] if sort_list[i] < min_element else min_element
    return min_element


def sort_sort_merge(a_list):
    """Sort by merge"""
    sort_list = list(a_list)
    sort_merge(sort_list, 0, len(sort_list)-1)
    return sort_list


def sort_merge(sort_list, p, r):
    """Recursia"""
    if p < r:
        q = (p+r)//2
        sort_merge(sort_list, p, q)
        sort_merge(sort_list, q+1, r)
        merge(sort_list, p, q, r)


def merge(sort_list, p, q, r):
    """Merge"""
    n1 = q - p + 1
    n2 = r - q
    l_list = []
    r_list = []
    for i in range(0, n1):
        l_list.append(sort_list[p+i])
    for j in range(0, n2):
        r_list.append(sort_list[q+j+1])
    i = j = 0
    for k in range(p, r+1):
        if (j == n2 and i < n1) or (i < n1 and j < n2 and l_list[i] <= r_list[j]):
            sort_list[k] = l_list[i]
            i += 1
        elif j < n2:
            sort_list[k] = r_list[j]
            j += 1

