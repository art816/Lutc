__author__ = 'art'


import binary_tree



class Tree(object):
    """

    """
    def __init__(self):
        """

        :return:
        """
        self.nil = ListObject()
        self.nil.color = 'black'
        self.nil.size = 0
        self.root = self.nil
        self.nil.left = self.root
        self.nil.right = self.root


    def tree_insert(self, list_object):
        """

        :param list_object:
        :return:
        """
        member_curent_list = self.nil
        curent_list = self.root
        while curent_list is not self.nil:
            curent_list.size += 1
            member_curent_list = curent_list
            if list_object.key < curent_list.key:
                curent_list = curent_list.left
            else:
                curent_list = curent_list.right
        list_object.parent = member_curent_list
        if member_curent_list is self.nil:
            self.root = list_object
        elif list_object.key < member_curent_list.key:
            member_curent_list.left = list_object
        else:
            member_curent_list.right = list_object
        list_object.left = self.nil
        list_object.right = self.nil
        list_object.color = 'red'
        self.insert_fixup(list_object)

    def insert_fixup(self, list_object):
        """
        """

        while list_object.parent.color == 'red':
            if list_object.parent == list_object.parent.parent.left:
                curent_list = list_object.parent.parent.right
                if curent_list.color == 'red':
                    list_object.parent.color = 'black'
                    curent_list.color = 'black'
                    list_object.parent.parent.color = 'red'
                    list_object = list_object.parent.parent
                else:
                    if list_object == list_object.parent.right:
                        list_object = list_object.parent
                        self.left_rotate(list_object)
                    list_object.parent.color = 'black'
                    list_object.parent.parent.color = 'red'
                    self.right_rotate(list_object.parent.parent)
            else:
                curent_list = list_object.parent.parent.left
                if curent_list.color == 'red':
                    list_object.parent.color = 'black'
                    curent_list.color = 'black'
                    list_object.parent.parent.color = 'red'
                    list_object = list_object.parent.parent
                else:
                    if list_object == list_object.parent.left:
                        list_object = list_object.parent
                        self.right_rotate(list_object)
                    list_object.parent.color = 'black'
                    list_object.parent.parent.color = 'red'
                    self.left_rotate(list_object.parent.parent)
        self.root.color = 'black'

    def left_rotate(self, list_object):
        """
        """
        curent_list = list_object.right
        list_object.right = curent_list.left

        if curent_list.left is not self.nil:
            curent_list.left.parent = list_object
        curent_list.parent = list_object.parent
        if list_object.parent == self.nil:
            self.root = curent_list
        elif list_object == list_object.parent.left:
            list_object.parent.left = curent_list
        else:
            list_object.parent.right = curent_list
        curent_list.left = list_object
        list_object.parent = curent_list
        curent_list.size = list_object.size
        list_object.size = list_object.left.size + list_object.right.size + 1

    def right_rotate(self, list_object):
        """
        """
        curent_list = list_object.left
        list_object.left = curent_list.right
        if curent_list.right is not self.nil:
            curent_list.right.parent = list_object
        curent_list.parent = list_object.parent
        if list_object.parent == self.nil:
            self.root = curent_list
        elif list_object == list_object.parent.right:
            list_object.parent.right = curent_list
        else:
            list_object.parent.left = curent_list
        curent_list.right = list_object
        list_object.parent = curent_list
        curent_list.size = list_object.size
        list_object.size = list_object.left.size + list_object.right.size + 1

    def inorder_tree_walk(self, list_tree):
        """

        :return:
        """
        if list_tree is not self.nil:
            return (self.inorder_tree_walk(list_tree.left), list_tree.key,
                    self.inorder_tree_walk(list_tree.right))

    def transplant(self, old_subroot, new_subroot):
        """

        :return: different_size. How change size of root.
        """
        print('transplate')
        if old_subroot is self.nil:
            self.root = new_subroot
        elif old_subroot == old_subroot.parent.left:
            old_subroot.parent.left = new_subroot
        else:
            old_subroot.parent.right = new_subroot
        new_subroot.parent = old_subroot.parent
        different_size = new_subroot.size - old_subroot.size
        self.return_true_size(new_subroot, different_size)
        return different_size

    def return_true_size(self, new_subroot, different_size):
        up_parent = new_subroot.parent
        while up_parent is not self.root:
            up_parent.size += different_size
            up_parent = up_parent.parent
        self.root.size += different_size

    def delete_list(self, list_object):
        """

        :param list_object:
        :return:
        """
        print('delete', self.root.size)
        curent_list = list_object
        curent_list_original_color = curent_list.color
        if list_object.left is self.nil:
            member_list = list_object.right
            self.transplant(list_object, list_object.right)
        elif list_object.right is self.nil:
            member_list = list_object.left
            self.transplant(list_object, list_object.left)
        else:
            curent_list = self.tree_minimum(list_object.right)
            curent_list_original_color = curent_list.color
            member_list = curent_list.right
            self.true_size(self.root)
            if curent_list.parent is list_object:
                member_list.parent = curent_list
                assert(self.root.size == 200), "{}".format(self.root.size)
                # curent_list.size += list_object.left.size
            else:
                self.transplant(curent_list, curent_list.right)
                assert(self.root.size == 199), "{}".format(self.root.size)
                curent_list.right = list_object.right
                curent_list.right.parent = curent_list
                curent_list.size = list_object.right.size + 1
                self.true_size(self.root)
            curent_list.size += list_object.left.size
            self.transplant(list_object, curent_list)
            curent_list.left = list_object.left
            curent_list.left.parent = curent_list
            curent_list.color = list_object.color
            assert(self.root.size == 199), "{}".format(self.root.size)
            self.true_size(self.root)
            self.true_size(self.root)
            assert(self.root.size == 199), "{}".format(self.root.size)
        if curent_list_original_color == 'black':
            self.delete_fixup(member_list)

    def delete_fixup(self, list_object):
        """
        """
        print('delete_fixup')
        while list_object is not self.nil and \
                        list_object.color == 'black':
            if list_object == list_object.parent.left:
                curent_list = list_object.parent.right
                if curent_list.color == 'red':
                    curent_list.color = 'black'
                    list_object.parent.color = 'red'
                    self.left_rotate(list_object.parent)
                    curent_list = list_object.parent.right
                if curent_list.left.color == 'black' and \
                                curent_list.right.color == 'black':
                    curent_list.color = 'red'
                    list_object = list_object.parent
                else:
                    if curent_list.right.color == 'black':
                        curent_list.left.color = 'black'
                        curent_list.color = 'red'
                        self.right_rotate(curent_list)
                        curent_list = list_object.parent.right
                    curent_list.color = list_object.parent.color
                    list_object.parent.color = 'black'
                    curent_list.right.color = 'black'
                    self.left_rotate(list_object.parent)
                    list_object = self.root
            else:
                if curent_list.color == 'red':
                    curent_list.color = 'black'
                    list_object.parent.color = 'red'
                    self.right_rotate(list_object.parent)
                    curent_list = list_object.parent.left
                if curent_list.right.color == 'black' and \
                                curent_list.left.color == 'black':
                    curent_list.color = 'red'
                    list_object = list_object.parent
                else:
                    if curent_list.left.color == 'black':
                        curent_list.right.color = 'black'
                        curent_list.color = 'red'
                        self.left_rotate(curent_list)
                        curent_list = list_object.parent.left
                    curent_list.color = list_object.parent.color
                    list_object.parent.color = 'black'
                    curent_list.left.color = 'black'
                    self.right_rotate(list_object.parent)
                    list_object = self.root
        list_object.color = 'black'

    def tree_minimum(self, list_object):
        """
        list_object must be root
        :return:
        """
        while list_object.left is not self.nil:
            list_object = list_object.left
        return list_object

    def tree_maximum(self, list_oblect):
        """
        list_object must be root
        :return:
        """
        while list_oblect.right is not self.nil:
            list_oblect = list_oblect.right
        return list_oblect

    def tree_search(self, list_object, key):
        """
        list_object must be root
        :param key:
        :return:
        """
        while list_object is not self.nil and key != list_object.key:
            if key < list_object.key:
                list_object = list_object.left
            else:
                list_object = list_object.right
        return list_object

    def os_select(self, list_object, rank):
        """

        :param list_obgect: must be root
        :param rank:
        :return:
        """
        assert list_object.size != 0
        seach_rank = list_object.left.size + 1
        if seach_rank == rank:
            return list_object
        elif rank < seach_rank:
            return self.os_select(list_object.left, rank)
        else:
            return self.os_select(list_object.right, rank - seach_rank)

    def os_rank(self, list_object):
        """
        """
        assert list_object.size != 0
        seach_rank = list_object.left.size + 1
        curent_list = list_object
        while curent_list is not self.root:
            if curent_list == curent_list.parent.right:
                seach_rank += curent_list.parent.left.size + 1
            curent_list = curent_list.parent
        return seach_rank

    def true_size(self, list_object):
        """

        :param list_object: must be root
        :return:
        """
        if list_object is not self.nil:
            assert(list_object.size == list_object.left.size +
                                       list_object.right.size + 1), "{} {}".format(list_object.size,
                                                                                   list_object.left.size +
                                                                                   list_object.right.size + 1)
            self.true_size(list_object.left)
            self.true_size(list_object.right)

class ListObject(binary_tree.ListObject):
    """
    """

    def __init__(self, key=None):
        """

        :param key:
        :return:
        """
        super().__init__(key)
        self.color = None
        self.size = 1
