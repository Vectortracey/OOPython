"""
node holder
"""

class Node():
    """
    node class
    """

    def __init__(self, key, value, parent=None):
        """
        init method
        """
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def has_left_child(self):
        """
        if the node has a left child
        """
        return self.left is not None

    def has_right_child(self):
        """
        checks for right child
        """
        return self.right is not None

    def has_both_children(self):
        """
        checks for both childs
        """
        return self.right is not None and self.left is not None

    def has_parent(self):
        """
        checks for parent
        """
        return self.parent is not None

    def is_left_child(self):
        """
        checks if it is left child
        """
        return self.key < self.parent.key

    def is_right_child(self):
        """
        checks if it is right child
        """
        return self.key > self.parent.key

    def is_leaf(self):
        """
        checks if it has childs
        """
        return self.left is None and self.right is None

    def __lt__(self, other):
        """
        lt method
        """
        if isinstance(other, Node):
            return self.key < other.key
        return self.key < other

    def __gt__(self, other):
        """
        gt method
        """
        if isinstance(other, Node):
            return self.key > other.key
        return self.key > other


    def __eq__(self, other):
        """
        eq method
        """
        if isinstance(other, Node):
            return self.key == other.key
        return self.key == other
