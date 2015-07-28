__author__ = 'art'

import unittest
import random
import sort_by_equal as eq


class Test(unittest.TestCase):
    def test_help_massive(self):
        A = [1, 4, 1, 4, 5, 6]
        help_massive, help_dict = eq.create_help_massive(A)
        self.assertEqual(help_massive, [0, 2, 0, 0, 2, 1, 1])
        self.assertEqual(help_dict, {1 : 2, 4 : 2, 5 : 1, 6 : 1})

    def test_num_les_element(self):
        A = [1, 4, 1, 4, 5, 6]
        help_massive, help_dict = eq.create_help_massive(A)
        eq.num_les_element(help_massive, help_dict)
        self.assertEqual(help_massive, [0, 2, 2, 2, 4, 5, 6])
        self.assertEqual(help_dict, {1 : 2, 4 : 4, 5 : 5, 6 : 6})

    def test_sort(self):
        random_list = []
        for i in range(20):
            random_list.append(random.randint(0, 10))
        sorted_list, sorted_list2 = eq.sort(random_list)
        self.assertEqual(sorted_list, sorted(random_list))
        self.assertEqual(sorted_list2, sorted(random_list))


if __name__ == '__main__':
    unittest.main()