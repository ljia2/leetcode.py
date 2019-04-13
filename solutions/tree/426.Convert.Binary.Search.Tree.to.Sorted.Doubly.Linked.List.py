# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root):
        """

        Convert a BST to a sorted circular doubly-linked list in-place.
        Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

        Let's take the following BST as an example, it may help you understand the problem better:



        We want to transform this BST into a circular doubly linked list.
        Each node in a doubly linked list has a predecessor and successor.
        For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
        The figure below shows the circular doubly linked list for the BST above.
        The "head" symbol means the node it points to is the smallest element of the linked list.

        Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor,
        and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.
        The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

        :type root: Node
        :rtype: Node
        """

        if not root:
            return None

        lhead = self.treeToDoublyList(root.left)
        rhead = self.treeToDoublyList(root.right)

        if not lhead and not rhead:
            root.left = root
            root.right = root
            return root
        elif lhead and rhead:
            lmax_node = lhead.left
            rmax_node = rhead.left
            # insert root into the doubly linked list.
            root.left = lmax_node
            lmax_node.right = root
            root.right = rhead
            rhead.left = root

            # make the circular
            lhead.left = rmax_node
            rmax_node.right = lhead
            return lhead
        elif lhead:
            lmax_node = lhead.left
            root.left = lmax_node
            lmax_node.right = root
            lhead.left = root
            root.right = lhead
            return lhead
        elif rhead:
            rmax_node = rhead.left
            root.right = rhead
            rhead.left = root
            root.left = rmax_node
            rmax_node.right = root
            return root




