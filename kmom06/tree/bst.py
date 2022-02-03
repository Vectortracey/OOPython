"""
bst file
"""
# pylint: disable=R1710
# pylint: disable=R1720
# pylint: disable=R0912
# pylint: disable=R0915

from node import Node
class BinarySearchTree:
    """
    searching methods
    """

    def __init__(self):
        """
        init holder
        """
        self.root = None
        self.size = 0

    def insert(self, key, value):
        """
        inserts
        """
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(key, value, self.root)

    @staticmethod
    def _insert(key, value, node):
        """
        private insert
        """
        if key < node:
            if node.has_left_child():
                BinarySearchTree._insert(key, value, node.left)
            else:
                node.left = Node(key, value, node)
        elif key > node:
            if node.has_right_child():
                BinarySearchTree._insert(key, value, node.right)
            else:
                node.right = Node(key, value, node)
        else:
            node.value = value


    def inorder_traversal_print(self):
        """
        prints the nodes in order
        """
        self._print_nodes(self.root)

    @staticmethod
    def _print_nodes(node):
        """
        prints in order
        """
        if node is None:
            return
        if node.has_left_child():
            BinarySearchTree._print_nodes(node.left)
        print(node.value)
        if node.has_right_child():
            BinarySearchTree._print_nodes(node.right)

    def get(self, key):
        """ Method to get certain node """
        if self.root is None:
            raise KeyError
        else:
            val = self._get(self.root, key)
            return val.value

    @staticmethod
    def _get(node, key):
        """ Private method to get certain node """
        if node is None:
            raise KeyError
        if node.__eq__(key):
            return node
        if node.__gt__(key):
            return BinarySearchTree._get(node.left, key)
        if node.__lt__(key):
            return BinarySearchTree._get(node.right, key)

    @staticmethod
    def _find_successor(successor):
        if successor.left is None:
            return successor
        return BinarySearchTree._find_successor(successor.left)

    def _give_root(self, child):
        self.root = child

    def remove(self, key):
        """ Method to remove node """
        if self.root is None:
            raise KeyError
        if self.root is not None:
            return self._remove(self.root, key)

    def _remove(self, node1, key):
        """ Private method to remove node """
        node = BinarySearchTree._get(node1, key)
        old_val = node.value

        if node.is_leaf():
            if node == self.root:
                self.root = None
            elif node.is_left_child():
                node.parent.left = None
            elif node.is_right_child():
                node.parent.right = None

        elif node.has_both_children():
            successor = BinarySearchTree._find_successor(node.right)
            node.key = successor.key
            node.value = successor.value

            if node == self.root:
                self.root = node.right
                self.root.left = node.left
                node.left.parent = node.right
                node.right.parent = None

            elif successor.is_left_child():
                if successor.has_right_child():
                    successor.parent.left = successor.right
                    successor.right.parent = successor.parent
                elif successor.is_leaf():
                    successor.parent.left = None

            else:
                if successor.is_leaf():
                    successor.parent.right = None
                else:
                    successor.parent.right = successor.right
                    successor.right.parent = successor.parent

        elif node.has_right_child():
            if node.has_parent():
                if node.is_left_child():
                    node.parent.left = node.right
                    node.right.parent = node.parent
                else:
                    node.parent.right = node.right
                    node.right.parent = node.parent
            else:
                self.root = node.right
                node.right.parent = None

        elif node.has_left_child():
            if node.has_parent():
                if node.is_left_child():
                    node.parent.left = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.right = node.left
                    node.left.parent = node.parent
            else:
                self.root = node.left
                node.right.parent = None

        return old_val

if __name__ == "__main__":
    bst = BinarySearchTree()
