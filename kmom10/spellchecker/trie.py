"""
Trie holder
"""
from node import Node
from errors import SearchMiss
# pylint: disable=R1710

class Trie():
    """
    Trie
    """

    word_list = []


    def __init__(self):
        """
        init method
        """
        self.root = Node()

    def add_word(self, word):
        """
        puts word into Trie
        """
        count = 0
        temp = self.root
        for x in word:
            x = x.lower()
            count += 1
            if x in temp.children:
                temp = temp.children[x]
            else:
                temp.children[x] = Node(x)
                temp = temp.children[x]
            if count == len(word):
                temp.end = True
                return True

    def has_word(self, word):
        """
        check to see if the input word is in the trie
        """
        temp = self.root
        for x in word:
            x = x.lower()
            if x in temp.children:
                temp = temp.children[x]
            else:
                raise SearchMiss()
        return temp.end

    def search_prefix(self, prefix):
        """
        search for given prefix, words with same letters
        """
        temp = self.root
        for x in prefix:
            if x in temp.children:
                temp = temp.children[x]
            else:
                return False
        for x in temp.children:
            self._print_words_prefix(temp.children[x], prefix)

    def print_words(self):
        """
        print out the words in the list
        """
        for x in self.root.children:
            word = ""
            self._print_words(self.root.children[x], word)

    def _print_words(self, node, word):
        """
        print out the nodes adds nodes to list
        """
        word += node.value
        if node.end:
            if word not in Trie.word_list:
                Trie.word_list.append(word)
        for x in node.children:
            self._print_words(node.children[x], word)
        return Trie.word_list

    def _print_words_prefix(self, node, word):
        """
        used for the prefix print
        """
        word += node.value
        if node.end:
            print(word)
        for x in node.children:
            self._print_words_prefix(node.children[x], word)


    @staticmethod
    def print_sorted_list():
        """
        prints the sorted list
        """
        sorterad = Trie.word_list
        sorterad.sort()
        for word in sorterad:
            print(word)
        return sorterad


    def use_wordlist(self, filename):
        """
        when u start program, this starts to put wordlist in to the trie
        """
        Trie.word_list = []
        with open((filename + ".txt"), 'r') as file:
            for line in file:
                for word in line.split():
                    self.add_word(word)

    def chose_wordlist(self, filename):
        """
        change to another wordlist, create a new Trie and add all words into it\
        from the filename chosen
        """
        Trie.word_list = []
        self.root = Node()
        with open((filename + ".txt"), 'r') as file:
            for line in file:
                for word in line.split():
                    self.add_word(word)


    def delete_word(self, word):
        """
        deletes word in trie
        """

        Trie.word_list = []
        if self.has_word(word):
            self._delete_word(self.root, word, 0)
        else:
            raise SearchMiss()

    def _delete_word(self, dicts, word, i):
        """
        remove word from the list
        """
        if i == len(word):
            if dicts.children:
                dicts.end = False
                return False
            dicts.end = False
            return True
        if word[i] in dicts.children and self._delete_word(dicts.children \
        [word[i]], word, i + 1):
            if not dicts.children[word[i]].children:
                if not dicts.children[word[i]].end:
                    del dicts.children[word[i]]
                    return True
                return False
            return False

        return False
