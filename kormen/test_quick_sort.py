__author__ = 'art'

import unittest
import random
import copy

import quick_sort


class Test(unittest.TestCase):
    """

    """
    def setUp(self):
        """
        """
        self.random_list = []
        for i in range(20):
            self.random_list.append(random.randint(0, 10))
        self.test_list = copy.copy(self.random_list)

    #@unittest.skip('blablabla')
    def test_quick_sort(self):
        """
        """
        quick_sort.sort(self.test_list, 0, len(self.test_list) - 1)
        self.assertEqual(self.test_list, sorted(self.random_list))

    def test_partition(self):
        """
        """
        index1 = 0
        index2 = len(self.test_list) - 1
        new_index1, new_index2 = quick_sort.partition(self.test_list, index1, index2)
        sort_element = self.test_list[new_index2]
       # print(new_index1, new_index2, sort_element)
       # print(self.test_list)
        for i in range(index1, new_index1):
            self.assertLess(self.test_list[i], sort_element, i)

        for i in range(new_index2 + 1, index2 + 1):
            self.assertGreater(self.test_list[i], sort_element, i)

        for i in range(new_index1, new_index2 + 1):
            self.assertEqual(self.test_list[i], sort_element, i)

if __name__ == '__main__':
    unittest.main()