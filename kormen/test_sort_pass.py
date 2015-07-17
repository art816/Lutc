__author__ = 'art'

import unittest
import random
import time

from my_sort import sort_pass, sort_select, sort_sort_merge
import heapify

class Test(unittest.TestCase):

    def test_sort_pass(self):
        a_list = []
        for ind in range(11**6):
            a_list.append(random.randint(1, 100))
        heap = heapify.Heapify(a_list)
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
        start = time.time()
        merge_list = sort_sort_merge(a_list)
        print('my_merge==', time.time() - start)
        start = time.time()
        heapify.heap_sort(heap)
        print('my_heap==', time.time() - start)
        # assert pass_list == true_result, \
        #     '{}\n{}'.format(pass_list, true_result)
        # assert select_list == true_result, \
        #     '{}\n{}'.format(select_list, true_result)
        assert merge_list == true_result, \
            '{}\n{}'.format(merge_list, true_result)
        assert heap.value == true_result, \
            '{}\n{}'.format(heap.value, true_result)


if __name__ == '__main__':
    unittest.main()