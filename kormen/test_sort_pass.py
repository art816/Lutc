__author__ = 'art'

import unittest
import random
import time
import copy

from my_sort import sort_pass, sort_select, sort_sort_merge
import quick_sort
import sort_by_equal
import heapify


class Test(unittest.TestCase):
    def test_sort_pass(self):
        a_list = []
        num_element = 10**3
        for ind in range(10**3):
            a_list.append(random.randint(0, num_element - 0))

        heap = heapify.Heapify(a_list)
        test_list = copy.copy(a_list)
        a_list = tuple(a_list)
        start = time.time()
        true_result = sorted(a_list, reverse=False)
        print('sorted==', time.time() - start)
        # start = time.time()
        # pass_list = sort_pass(a_list)
        # print('my_pass==', time.time() - start)
        # start = time.time()
        # select_list = sort_select(a_list)
        # print('my_select==', time.time() - start)
        # start = time.time()
        # merge_list = sort_sort_merge(a_list)
        # print('my_merge==', time.time() - start)
        # start = time.time()
        # heap.build_max_heap()
        # heap.heap_sort()
        # print('my_heap==', time.time() - start)
        start = time.time()
        quick_sort.sort(test_list, 0, len(test_list) - 1)
        print('my_quick==', time.time() - start)
        start = time.time()
        equal_res, equal_res2 = sort_by_equal.sort(list(a_list), num_element)
        print('sort_by_equal==', time.time() - start)
        # assert pass_list == true_result, \
        # '{}\n{}'.format(pass_list, true_result)
        # assert select_list == true_result, \
        #     '{}\n{}'.format(select_list, true_result)
        # assert merge_list == true_result, \
        #     '{}\n{}'.format(merge_list, true_result)
        # assert heap.value == true_result, \
        #     '{}\n{}'.format(heap.value, true_result)
        assert test_list == true_result, \
            '{}\n{}'.format(test_list, true_result)
        assert equal_res == true_result, \
            '{}\n{}'.format(equal_res, true_result)
        # assert equal_res2 == true_result, \
        #     '{}\n{}'.format(equal_res2, true_result)

if __name__ == '__main__':
    unittest.main()