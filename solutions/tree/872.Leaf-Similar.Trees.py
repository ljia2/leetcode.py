# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

        For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

        Two binary trees are considered leaf-similar if their leaf value sequence is the same.

        Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1 = []
        self.dfs(root1, leaf1)

        leaf2 = []
        self.dfs(root2, leaf2)

        return leaf1 == leaf2

    def dfs(self, root, leaf):
        if not root.left and not root.right:
            leaf.append(root.val)
            return

        if root.left:
            self.dfs(root.left, leaf)
        if root.right:
            self.dfs(root.right, leaf)
        return

s = Solution()
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

root2 = TreeNode(3)
root2.left=TreeNode(1)
root2.right = TreeNode(2)

print(s.leafSimilar(root1, root2))