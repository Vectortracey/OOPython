"""
function holder for Queue class
"""
from node import Node
from errors import EmptyQueueException

class Queue:
    """
    function holder for node handling
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def is_empty(self):
        """
        checks if the list is empty or not
        """
        return self.head is None

    def enqueue(self, data):
        """Add to the queue."""
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

        self._length += 1

    def dequeue(self):
        """
        removes from the list
        """
        if self.head is None:
            raise EmptyQueueException
        current_head = self.head
        if self.head is self.tail:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next
        self._length -= 1
        return current_head.data


    def peek(self):
        """
        checks if head is empty, else returns the value of it
        """
        if self.head is not None:
            return self.head.data
        raise EmptyQueueException


    def size(self):
        """
        counts the number linked items in the list
        """

        return len(self)

    def __len__(self):
        """method __len__."""
        return self._length
