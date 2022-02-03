"""
functions for the program
"""

from node import Node
from errors import NoIndexValue, ValueNotFound

class UnorderedList():
    """
    class for my unorderedlist
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def append(self, data):
        """
        adds to list
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def set(self, index, data):
        """
        replaces data on index with new data
        """
        current = self.head
        counter = 0

        if current is not None:
            while current.next is not None and counter < index:
                current = current.next
                counter += 1
            if counter == index:
                current.data = data
                return data
            if counter < index:
                raise NoIndexValue()
        else:
            raise NoIndexValue()

    def size(self):
        """
        returns the number of elements in list
        """
        current_node = self.head
        res = "None"
        if current_node is not None:
            res = []
            while current_node is not None:
                res.append(current_node.data)
                current_node = current_node.next

        return len(res)

    def get(self, index):
        """
        returns the value of selected index
        """

        current = self.head
        if current is not None:
            counter = 0
            while current.next is not None and counter < index:
                current = current.next
                counter += 1
            if counter == index:
                return current.data
            if counter != index:
                raise NoIndexValue()
        else:
            raise NoIndexValue()

    def index_of(self, value):
        """
        returns the index of data in the list
        """
        current = self.head
        counter = 0

        if current is not None:
            while current is not None:
                if current.data == value:
                    return counter
                if current.data != value:
                    counter += 1
                    current = current.next
        else:
            raise ValueNotFound()

    def print_list(self):
        """
        write list
        """
        current = self.head
        if current:
            print("Lists contains of the following: ")
            while current:
                print(current.data)
                current = current.next
        else:
            print("Empty list!")


    def remove(self, data):
        """
        remove node
        """
        current = self.head
        previous = None

        if current is not None:
            while current.data != data:
                previous = current
                current = current.next
                if current is None:
                    raise ValueNotFound()

            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
        else:
            raise ValueNotFound()
