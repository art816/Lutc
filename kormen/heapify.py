__author__ = 'art'

class Heapify(list):
    """
    """
    def __init__(self, value):
        """
        """
        self.value = value
        self.trash = []
        self.heap_size = len(value)

    def length(self):
        """
        """
        return len(self.value)


def max_heapify(heap, index):
    """
    :param heap:
    :param index:
    """
    left = left_list(index)
    right = right_list(index)
    if left < heap.heap_size and heap.value[left] > heap.value[index]:
        largest = left
    else:
        largest = index
    if right < heap.heap_size and heap.value[right] > heap.value[largest]:
        largest = right
    if largest != index:
        change = heap.value[index]
        heap.value[index] = heap.value[largest]
        heap.value[largest] = change
        max_heapify(heap, largest)

def build_max_heap(heap):
    index_list = list(range(parent(heap.heap_size-1)+1))
    index_list = sorted(index_list, reverse=True)
    for index in index_list:
        max_heapify(heap, index)

def heap_sort(heap):
    """
    :param heap:
    :return:
    """
    build_max_heap(heap)
    index_list = list(range(1, heap.length()))
    index_list = sorted(index_list, reverse=True)
    for index in index_list:
        change = heap.value[0]
        heap.value[0] = heap.value[index]
        heap.value[index] = change
        heap.heap_size -= 1
        max_heapify(heap, 0)




def left_list(index):
    """
    :param index:
    :return:
    """
    return 2*index + 1


def right_list(index):
    """
    :param index:
    :return:
    """
    return 2*index + 2

def parent(index):
    """
    :param index:
    :return:
    """
    return (index - 1) // 2