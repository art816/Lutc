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

    # def __repr__(self):
    #     for return_value in self.inorder_tree_walk(self.root):
    #         while return_value is tuple:
    #
    #     return 'end'

    # def print_tree(self, list_tree):
    #     """
    #
    #     :return:
    #     """
    #     return


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

    def transplant(self, old_subroot, new_subroot):
        """

        :return:
        """
        if old_subroot is None:
            self.root = new_subroot
        elif old_subroot == old_subroot.parent.left:
            old_subroot.parent.left = new_subroot
        else:
            old_subroot.parent.right = new_subroot
        if new_subroot is not None:
            new_subroot.parent = old_subroot.parent

    def delete_list(self, list_object):
        """

        :param list_object:
        :return:
        """
        if list_object.left is None:
            self.transplant(list_object, list_object.right)
        elif list_object.right is None:
            self.transplant(list_object, list_object.left)
        else:
            minimum_list_object = self.tree_minimum(list_object.right)
            if minimum_list_object.parent is not list_object:
                self.transplant(minimum_list_object, minimum_list_object.right)
                minimum_list_object.right = list_object.right
                minimum_list_object.right.parent = minimum_list_object
            self.transplant(list_object, minimum_list_object)
            minimum_list_object.left = list_object.left
            minimum_list_object.left.parent = minimum_list_object

