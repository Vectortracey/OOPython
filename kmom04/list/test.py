"""
runs tests
"""

import unittest
from unorderedlist import UnorderedList
from node import Node
from errors import NoIndexValue, ValueNotFound

class TestList(unittest.TestCase):
    """
    tests the different methods in unorderedlist
    """

    ultest = UnorderedList()

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




if __name__ == '__main__':
    unittest.main()
