__author__ = 'art'


class ListObject(object):
    """

    """
    def __init__(self, key=None):
        """

        :param key:
        :return:
        """
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class Tree(object):
    """
    """
    def __init__(self):
        """

        :return:
        """
        self.root = None
        self.high = 0

    def __repr__(self):
        print(str(self.print_tree(self.root)).replace('(', '').
        replace(')','').
        replace('\'', '').
        replace(' ', ''))
        return 'end'

    def print_tree(self, list_tree):
        """

        :return:
        """
        if list_tree is not None:
            return(list_tree.key, '\n',
                   self.print_tree(list_tree.left),
                   self.print_tree(list_tree.right))


    def inorder_tree_walk(self, list_tree):
        """

        :return:
        """
        if list_tree is not None:
            return self.inorder_tree_walk(list_tree.left), list_tree.key,\
                   self.inorder_tree_walk(list_tree.right)

    def tree_search(self, list_object, key):
        """
        list_object must be root
        :param key:
        :return:
        """
        while list_object is not None and key != list_object.key:
            if key < list_object.key:
                list_object = list_object.left
            else:
                list_object = list_object.right
        return list_object

    def tree_minimum(self, list_object):
        """
        list_object must be root
        :return:
        """
        while list_object.left is not None:
            list_object = list_object.left
        return list_object

    def tree_maximum(self, list_oblect):
        """
        list_object must be root
        :return:
        """
        while list_oblect.right is not None:
            list_oblect = list_oblect.right
        return list_oblect

    def tree_successor(self, list_object):
        """

        :param list_object:
        :return: element with minimal key greater list_object.key
        """
        if list_object.right is not None:
            return self.tree_minimum(list_object.right)
        parent_list_object = list_object.parent
        while parent_list_object is not None and\
                        parent_list_object.right == list_object:
            list_object = parent_list_object
            parent_list_object = parent_list_object.parent
        return parent_list_object

    def tree_insert(self, list_object):
        """

        :param list_object:
        :return:
        """
        member_curent_list = None
        curent_list = self.root
        high = 0
        while curent_list is not None:
            high += 1
            member_curent_list = curent_list
            if list_object.key < curent_list.key:
                curent_list = curent_list.left
            else:
                curent_list = curent_list.right
        list_object.parent = member_curent_list
        if high >= self.high:
            self.high = high + 1
        if member_curent_list is None:
            self.root = list_object
        elif list_object.key < member_curent_list.key:
            member_curent_list.left = list_object
        else:
            member_curent_list.right = list_object

