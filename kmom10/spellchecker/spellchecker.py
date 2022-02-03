"""
mainfile, contains spellchecker class and it's functions
"""
# pylint: disable=R0912
from trie import Trie
from errors import SearchMiss

class SpellChecker():
    """
    spellchecker Class
    """

    def __init__(self):
        """
        init method
        """
        self.trie = Trie()

    def begin(self):
        """
        Spellchecker menu
        """
        self.trie.use_wordlist("tiny_dictionary")
        self.print_menu()
        while True:
            choice = input("Chose from the menu.\n")
            if choice == "1":
                word = input("Write in a word to check if it is in wordlist, returns True/false \
                \n")
                try:
                    print(self.trie.has_word(word))
                except SearchMiss:
                    print("Not in wordlist!")
            elif choice == "2":
                prefix = input("Write your prefix three letters minimum. \n")
                if len(prefix) == 3:
                    while True:
                        self.trie.search_prefix(prefix)
                        input_prefix = input("Write prefix (q to exit): \
" + prefix)
                        if input_prefix == "q":
                            break
                        prefix += input_prefix
                else:
                    print("Prefix has to be minimum of 3 letters.")
            elif choice == "3":
                wordlist = input("Which list would you like to use?: \n")
                self.trie.chose_wordlist(wordlist)
            elif choice == "4":
                self.trie.print_words()
                Trie.print_sorted_list()
            elif choice == "5":
                input_remove = input("Which word would you you like to remove?: \n")
                try:
                    self.trie.delete_word(input_remove)
                except SearchMiss:
                    print("That word is not in the list.")
            elif choice == "menu":
                self.print_menu()
            elif choice == "exit":
                break
            else:
                print("Not an menu option, choose from the menu.!\n")


    @staticmethod
    def print_menu():
        """
        spellcheckers menu
        """
        print("1) Input word and returns True/False for the chosen dict, tiny dict is standard.")
        print("2) Search for a chosen prefix, q to quite.")
        print("3) Change the Wordlist.")
        print("4) Prints all the words in the chosen list.")
        print("5) Remove a word from the list.")
        print("menu) Prints the menu.")
        print("exit) Exits program.")


if __name__ == "__main__":
    spellchecker = SpellChecker()
    spellchecker.begin()
