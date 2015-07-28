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

    def inorder_tree_walk(self, list_tree):
        """

        :return:
        """
        if list_tree is not None:
            self.inorder_tree_walk(list_tree.left)
            print(list_tree.key)
            self.inorder_tree_walk(list_tree.right)

    def tree_search(self, list_object, key):
        """

        :param key:
        :return:
        """
        while list_object is not None and key != list_object.key:
            if key < list_object.key:
                next_list_object = list_object.left
            else:
                next_list_object = list_object.right
        return next_list_object

    def tree_minimum(self, list_oblect):
        """

        :return:
        """
        while list_oblect.left is not None:
            left_list_oblect = list_oblect.left
        return left_list_oblect

    def tree_maximum(self, list_oblect):
        """

        :return:
        """
        while list_oblect.right is not None:
            right_list_oblect = list_oblect.right
        return right_list_oblect

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
        while curent_list is not None:
            member_curent_list = curent_list
            if list_object.key < curent_list.key:
                curent_list = curent_list.left
            else:
                curent_list = curent_list.right
        list_object.parent = member_curent_list
        if member_curent_list is None:
            self.root = list_object
        elif list_object.key < member_curent_list.key:
            member_curent_list.left = list_object
        else:
            member_curent_list.right = list_object

