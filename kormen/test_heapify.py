__author__ = 'art'

import unittest
import random

import heapify


class Test(unittest.TestCase):
    """

    """
    def setUp(self):
        """
        """
        self.random_list = []
        for i in range(10):
            self.random_list.append(random.randint(0, 100))
        self.heap = heapify.Heapify(self.random_list)

    def test_left_list(self):
        """
        """
        index = 3
        self.assertEqual(self.heap.left_list(index), 2 * index + 1)

    def test_right_list(self):
        """
        """
        index = 3
        self.assertEqual(self.heap.right_list(index), 2 * index + 2)

    def test_parent(self):
        """
        """
        index = 4
        self.assertEqual(self.heap.parent(index), 1)
        index = 5
        self.assertEqual(self.heap.parent(index), 2)
        index = -5
        self.assertEqual(self.heap.parent(index), -3)
        index = 1
        self.assertEqual(self.heap.parent(index), 0)
        index = 2
        self.assertEqual(self.heap.parent(index), 0)

    def test_max_heapify(self):
        """
        """
        heap = heapify.Heapify([3, 2, 5])
        heap.max_heapify(0)
        self.assertEqual(heap.value, [5, 2, 3])

    def test_class_heapify(self):
        """
        """
        heap = heapify.Heapify([1, 2, 3])
        heap.value.append(1)
        self.assertEqual(heap.value[-1], 1)
        self.assertEqual(heap.length(), 4)
        self.assertEqual(heap.heap_size, 3)

    def test_build_max_heap(self):
        """
        """
        self.heap.build_max_heap()
        for index in range(1, self.heap.heap_size):
            self.assertGreaterEqual(self.heap.value[self.heap.parent(index)],
                                    self.heap.value[index])

    def test_heap_sort(self):
        """
        """
        self.heap.heap_sort()
        self.assertEqual(self.heap.value, sorted(self.random_list,
                         reverse=False))

    def test_heap_maximum(self):
        """
        """
        self.heap.build_max_heap()
        self.assertEqual(self.heap.heap_maximum(), max(self.random_list))


if __name__ == '__main__':
    unittest.main()