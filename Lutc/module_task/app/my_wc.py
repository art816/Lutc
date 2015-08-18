__author__ = 'art'

def count_lines(file_name):
    """

    :param file_name: file witch need open
    :return: number lines
    """
    num_lines = 0
    with open(file_name) as file:
        for line in file:
            num_lines += 1
    return num_lines

def count_chars(file_name):
    """

    :param file_name: file witch need open
    :return: number chars
    """
    num_chars = 0
    with open(file_name) as file:
        for line in file:
            num_chars += len(line.rstrip())
    return  num_chars