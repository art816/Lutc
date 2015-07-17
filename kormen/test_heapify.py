__author__ = 'art'

import unittest
import random

import heapify


class Test(unittest.TestCase):
    """

    """
    def test_left_list(self):
        """
        """
        index = 3
        self.assertEqual(heapify.left_list(index), 2*index + 1)

    def test_right_list(self):
        """
        """
        index = 3
        self.assertEqual(heapify.right_list(index), 2*index + 2)

    def test_parent(self):
        """
        """
        index = 4
        self.assertEqual(heapify.parent(index), 1)
        index = 5
        self.assertEqual(heapify.parent(index), 2)
        index = -5
        self.assertEqual(heapify.parent(index), -3)
        index = 1
        self.assertEqual(heapify.parent(index), 0)
        index = 2
        self.assertEqual(heapify.parent(index), 0)

    def test_max_heapify(self):
        """
        """
        heap = heapify.Heapify([3, 2, 5])
        heapify.max_heapify(heap, 0)
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
        heap = heapify.Heapify(list(range(10)))
        heapify.build_max_heap(heap)
        for index in range(1, 10):
            self.assertGreaterEqual(heap.value[heapify.parent(index)],
                                    heap.value[index])

    def test_heap_sort(self):
        """
        """
        random_list = []
        for i in range(10):
            random_list.append(random.randint(0, 100))
        heap = heapify.Heapify(random_list)
        heapify.heap_sort(heap)
        self.assertEqual(heap.value, sorted(random_list, reverse=False))

if __name__ == '__main__':
    unittest.main()