"""
Holds the node class
"""

class Node():
    """
    A class node
    """

    def __init__(self, value=None):
        """
        init method, creates the node
        """
        self.children = {}
        self.end = False
        self.value = value
