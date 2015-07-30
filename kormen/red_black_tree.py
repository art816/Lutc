__author__ = 'art'


import binary_tree

class Tree(binary_tree.Tree):
    """

    """
    def __init__(self):
        """

        :return:
        """
        self.nil = ListObject()
        self.nil.color = 'black'
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
                        self.left_rotate(list_object)
                    list_object.parent.color = 'black'
                    list_object.parent.parent.color = 'red'
                    self.right_rotate(list_object.parent.parent)
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

                
                    
        

class ListObject(binary_tree.ListObject):
    """

    """
    def __init__(self, key=None):
        super().__init__(key)
        self.color = None
