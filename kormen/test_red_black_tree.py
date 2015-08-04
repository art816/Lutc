__author__ = 'art'

import unittest
import random

import red_black_tree


class Test(unittest.TestCase):
    """

    """
    @classmethod
    def setUpClass(cls):
        cls.tree = red_black_tree.Tree()
        cls.create_random_tree(cls, 10**6)

    def create_random_tree(self, num_element):
        """дфшра дфруша фжцуазэуцаоуцаушрафушар666дшо6фу6дшфудша2уар2цуа5а◘уа8ибфцуоиафцуиа

        :return:
        """
        list_value = []
        for i in range(num_element):
            list_value.append(random.randint(1, 100))
            list_object = red_black_tree.ListObject(list_value[-1])
            self.tree.tree_insert(list_object)
        return list_value

    def test_tree(self):
        self.assertEqual(self.tree.root.color, 'black')
        self.assertEqual(self.tree.nil.color, 'black')

    def test_red_black(self):
        """
        :param list_object must be root
        :return:
        """
        if self.tree.root is not self.tree.nil:
            self.red_list_have_black_child(self.tree.root)

    def red_list_have_black_child(self, list_object):
        """
        :param list_object:
        :return:
        """
        if list_object is not self.tree.nil:
            if list_object.color == 'red':
                self.assertEqual(list_object.left.color, 'black')
                self.assertEqual(list_object.right.color, 'black')
            self.red_list_have_black_child(list_object.left)
            self.red_list_have_black_child(list_object.right)

    def test_len_simple_road(self):
        """
        :return:
        """
        # TODO patern
        rez_string = str(self.len_sub_tree(self.tree.root))
        # print(rez_string)
        centr = rez_string.find('root')
        # print(rez_string[centr])
        count = -1
        max_count = 0
        for i in range(centr):
            if rez_string[i] == '(':
                count += 1
            elif rez_string[i] == ')':
                count -= 1
            if count > max_count:
                max_count = count
        print('left = ', max_count)
        count = 1
        max_count = 0
        open_tree = False
        depth_tree = 0
        rb_depth_tree = 0
        for i in range(centr, len(rez_string)):
            if rez_string[i] == '(':
                count += 1
                if open_tree:
                    depth_tree += 1
            elif rez_string[i] == ')':
                count -= 1
                if open_tree:
                    depth_tree -= 1
                    if depth_tree == 0:
                        open_tree = False
            if rez_string[i:i + 1] == '(1' and open_tree is False:
                open_tree = True
            elif rez_string[i:i + 1] == '(1' and open_tree is True:
                rb_depth_tree += 1
            if count > max_count:
                max_count = count
        print('right = ', max_count, 'red_black_tree = ', rb_depth_tree)


    def len_sub_tree(self, list_object):
        """

        :param list_object:
        :return:
        """
        if list_object is not self.tree.nil:
            return (self.len_sub_tree(list_object.left),
                    (
                        'root' if list_object == self.tree.root else 1 if list_object.color == 'black' else 0,
                        list_object.key),
                    self.len_sub_tree(list_object.right))

    def test_transplant(self):
        list_value = self.create_random_tree(100)
        curr_value = list_value[10]
        list_object = self.tree.tree_search(self.tree.root, curr_value)
        sub_tree1 = self.tree.inorder_tree_walk(list_object.right)
        # проверка, что можем заменить поддерево с корневым узлом list_object
        # поддеревом с корневым узлом list)object.right
        if list_object == list_object.parent.right:
            self.tree.transplant(list_object, list_object.right)
            self.assertEqual(list_object.right, list_object.parent.right)
            sub_tree2 = self.tree.inorder_tree_walk(list_object.parent.right)
        else:
            self.tree.transplant(list_object, list_object.right)
            self.assertEqual(list_object.right, list_object.parent.left)
            sub_tree2 = self.tree.inorder_tree_walk(list_object.parent.left)
        self.assertEqual(sub_tree1, sub_tree2)

    def test_delete(self):
        list_value = self.create_random_tree(100)
        curr_value = list_value[10]
        list_object = self.tree.tree_search(self.tree.root, curr_value)
        self.tree.delete_list(list_object)
        # TODO
        # не знаю как нормально проверить, что правильно удалили элемент,
        # кроме как проверить, что возвращается сортированый список значений.
        res_value = self.tree.inorder_tree_walk(self.tree.root)
        print(res_value)
        string_res = str(res_value)
        list_with_string = string_res.replace('(', ''). \
            replace(')', ''). \
            replace('None', ''). \
            replace(',', ''). \
            rsplit('  ')
        list_value = [int(num) for num in list_with_string]
        print('list_value = ', list_value)
        self.assertEqual(list_value, sorted(list_value))
        # self.assertTrue(False)
