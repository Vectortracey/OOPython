"""
runs tests
"""

import unittest
from unorderedlist import UnorderedList
from node import Node
from errors import NoIndexValue, ValueNotFound
from sort import recursive_sort

class TestList(unittest.TestCase):
    """
    tests the different methods in unorderedlist
    """

    ultest = UnorderedList()
    empty_list = UnorderedList()
    test_list = UnorderedList()

    def test_append(self):
        """
        tests the append method adding nodes
        """
        test_node = Node("testingtesting")
        test_node_two = Node("bestingbesting")
        TestList.ultest.append(test_node)
        TestList.ultest.append(test_node_two)
        self.assertEqual(TestList.ultest.size(), 2)

    def test_set(self):
        """
        tests the set method overriding data
        """
        test_node_three = Node("writemeover")
        TestList.ultest.append(test_node_three)
        self.assertEqual(TestList.ultest.set(0, "imoveryou"), "imoveryou")



    def test_set_fail(self):
        """
        tests the exception of set
        """
        with self.assertRaises(NoIndexValue) as _:
            self.ultest.set(6, "krocka")


    def test_get(self):
        """
        tests the get method
        """
        test_node_four = Node("getmeoutofhere")
        TestList.ultest.append(test_node_four.data)
        self.assertEqual(TestList.ultest.get(2), "getmeoutofhere")


    def test_get_fail(self):
        """
        tests the exception of get
        """
        with self.assertRaises(NoIndexValue) as _:
            self.ultest.get(10)

    def test_index_of(self):
        """
        tests index_of method
        """
        test_node_five = Node("whatismyindex")
        TestList.ultest.append(test_node_five.data)
        self.assertEqual(TestList.ultest.index_of("whatismyindex"), 3)


    def test_index_of_fail(self):
        """
        tests the exception of index of
        """
        with self.assertRaises(ValueNotFound) as _:
            self.ultest.index_of("tajmahal")

    def test_remove(self):
        """
        tests the remove function
        """
        TestList.ultest.remove("whatismyindex")
        self.assertEqual(TestList.ultest.size(), 3)



    def test_remove_fail(self):
        """
        tests the exception of remove
        """
        with self.assertRaises(ValueNotFound) as _:
            self.ultest.remove("mastodontfilmsmads")


    def test_rec_sort(self):
        """tests if the sort function works"""
        test_node_six = Node("rawr")
        test_node_seven = Node("1")
        TestList.test_list.append(test_node_six.data)
        TestList.test_list.append(test_node_seven.data)
        recursive_sort(self.test_list, n=2)
        self.assertEqual(TestList.test_list.get(0), "1")


    def test_recursive_empty(self):
        """
        checks returnvalue if list is empty
        """

        recursive_sort(self.empty_list, n=0)
        self.assertEqual(recursive_sort(TestList.empty_list, n=0), None)


if __name__ == '__main__':
    unittest.main()
