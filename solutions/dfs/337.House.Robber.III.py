# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root):
        """

        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            include, exclude = self.treeRob(root)
            return max(include, exclude)

    def treeRob(self, root):
        if root.left is None and root.right is None:
            return root.val, 0
        elif root.left is None:
            rinclude, rexclude = self.treeRob(root.right)
            return root.val + rexclude, max(rinclude, rexclude)
        elif root.right is None:
            linclude, lexclude = self.treeRob(root.left)
            return root.val + lexclude, max(linclude, lexclude)
        else:
            linclude, lexclude = self.treeRob(root.left)
            rinclude, rexclude = self.treeRob(root.right)
            return root.val + lexclude + rexclude, max(linclude, lexclude) + max(rinclude, rexclude)
