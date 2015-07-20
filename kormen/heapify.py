__author__ = 'art'


class Heapify(list):
    """
    """

    def __init__(self, value):
        """
            """
        super().__init__()
        self.value = value
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
            change = self.value[index]
            self.value[index] = self.value[largest]
            self.value[largest] = change
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
        self.build_max_heap()
        index_list = list(range(1, self.length()))
        index_list = sorted(index_list, reverse=True)
        for index in index_list:
            change = self.value[0]
            self.value[0] = self.value[index]
            self.value[index] = change
            self.heap_size -= 1
            self.max_heapify(0)

    def heap_maximum(self):
        """
        :return:
        """
        return self.value[0]

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