__author__ = 'art'

import unittest
import random

from max_find_subarray import find_max_subarray

class Test(unittest.TestCase):

    def test_find_max_subarray(self):
        # a_list = [-1, 100, -1, 101, -2, 2, -2, -2]
        a_list = []
        for ind in range(10**6):
            a_list.append(random.randint(1, 100) - 70)
        a_list = tuple(a_list)
        [sum_subarray, start_ind, end_ind] = find_max_subarray(a_list)
        if start_ind == end_ind:
            print(a_list[start_ind])
        # assert (sum_subarray == 0), sum_subarray
        # assert (start_ind == 0)
        # assert (end_ind == 5)


if __name__ == '__main__':
    unittest.main()