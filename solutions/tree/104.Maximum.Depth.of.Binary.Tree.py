# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        Given a binary tree, find its maximum depth.

        The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

        Note: A leaf is a node with no children.

        Example:

        Given binary tree [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        return its depth = 3.
        :type root: TreeNode
        :rtype: int

        see LC865

        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        lh = self.maxDepth(root.left) if root.left else 0
        rh = self.maxDepth(root.right) if root.right else 0
        return max(lh, rh) + 1

