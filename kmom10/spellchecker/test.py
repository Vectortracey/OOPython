"""
test file
"""
import unittest
from trie import Trie
from errors import SearchMiss

class TestTrie(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """ Setup test """
        self.ttrie = Trie()



    def test_has_word_fail(self):
        """
        test the has_word function returning False since this word does not \
        exists  in the .txt
        """
        with self.assertRaises(SearchMiss) as _:
            self.ttrie.has_word("rektangel")

    def test_add_word(self):
        """
        tests to put in the word above into the Trie, so we later can check \
        it and return True
        """
        self.assertEqual(True, self.ttrie.add_word("rektangel"))

    def test_has_word(self):
        """
        checks if the has_word returns True if word is in Trie
        """
        self.ttrie.add_word("babian")
        self.assertEqual(True, self.ttrie.has_word("babian"))

    def test_search_prefix(self):
        """
        tests to search for a prefix that does not exists
        """
        self.assertEqual(False, self.ttrie.search_prefix("kla"))

    def test_remove_word_fail(self):
        """
        try to remove a word
        """
        with self.assertRaises(SearchMiss) as _:
            self.ttrie.delete_word("lalala")

    def test_printed_list(self):
        """
        tests to delete a word from trie
        """
        with self.assertRaises(FileNotFoundError) as _:
            self.ttrie.chose_wordlist("fellista")


if __name__ == '__main__':
    unittest.main(verbosity=3)
