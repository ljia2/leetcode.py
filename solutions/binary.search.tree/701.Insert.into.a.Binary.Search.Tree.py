# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST.
        Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

        Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
        You can return any of them.

        For example,

        Given the tree:
                4
               / \
              2   7
             / \
            1   3
        And the value to insert: 5

        You can return this binary search tree:

                 4
               /   \
              2     7
             / \   /
            1   3 5
        This tree is also valid:

                 5
               /   \
              2     7
             / \
            1   3
                 \
                  4

        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if not root:
            return TreeNode(val)

        if root.val > val:
            if root.left:
                _ = self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                _ = self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        return root
