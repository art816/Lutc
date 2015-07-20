__author__ = 'art'

import copy

empty_heap = Exception("Heap is empty")
little_key = Exception("Little key")

class Heapify(object):
    """
    """

    def __init__(self, value):
        """
            """
        self.value = copy.copy(value)
        self.trash = []
        self.heap_size = len(value)

    def length(self):
        """
        """
        return len(self.value)

    def max_heapify(self, index):
        """
        :param index:
        """
        left = self.left_list(index)
        right = self.right_list(index)
        if left < self.heap_size and self.value[left] > self.value[index]:
            largest = left
        else:
            largest = index
        if right < self.heap_size and self.value[right] > self.value[largest]:
            largest = right
        if largest != index:
            self.replace(index, largest)
            self.max_heapify(largest)

    def build_max_heap(self):
        index_list = list(range(self.parent(self.heap_size - 1) + 1))
        index_list = sorted(index_list, reverse=True)
        for index in index_list:
            self.max_heapify(index)

    def heap_sort(self):
        """
        :return:
        """
        index_list = list(range(1, self.length()))
        index_list = sorted(index_list, reverse=True)
        for index in index_list:
            self.replace(0, index)
            self.heap_size -= 1
            self.max_heapify(0)

    def heap_extract_max(self):
        """
        """
        if self.heap_size == 0:
            raise empty_heap
        else:
            max_element = self.value[0]
            self.replace(0, self.heap_size - 1)
            self.value.pop(self.heap_size - 1)
            self.heap_size -= 1
            self.max_heapify(0)
            return max_element

    def heap_maximum(self):
        """
        :return:
        """
        if self.heap_size == 0:
            raise empty_heap
        else:
            return self.value[0]

    def increase_key(self, index, key):
        if self.value[index] is None or self.value[index] < key:
            self.value[index] = key
            while index > 0 and \
                            self.value[index] > self.value[self.parent(index)]:
                self.replace(index, self.parent(index))
                index = self.parent(index)
        else:
            raise little_key

    def heap_insert(self, key):
        self.value.append(None)
        self.heap_size += 1
        self.increase_key(self.heap_size - 1, key)

    def replace(self, index_1, index_2):
        """
        :param index_1:
        :param index_2:
        """
        change = self.value[index_1]
        self.value[index_1] = self.value[index_2]
        self.value[index_2] = change

    def heap_delete(self, index):
        """
        """
        self.replace(index, self.heap_size - 1)
        self.value.pop(self.heap_size - 1)
        self.heap_size -= 1
        self.max_heapify(index)

    @staticmethod
    def left_list(index):
        """
        :param index:
        :return:
        """
        return 2 * index + 1

    @staticmethod
    def right_list(index):
        """
        :param index:
        :return:
        """
        return 2 * index + 2

    @staticmethod
    def parent(index):
        """
        :param index:
        :return:
        """
        return (index - 1) // 2