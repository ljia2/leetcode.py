# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        A binary tree is univalued if every node in the tree has the same value.

        Return true if and only if the given tree is univalued.



        Example 1:


        Input: [1,1,1,1,1,null,1]
        Output: true
        Example 2:


        Input: [2,2,2,5,2]
        Output: false


        Note:

        The number of nodes in the given tree will be in the range [1, 100].
        Each node's value will be an integer in the range [0, 99].

        :type root: TreeNode
        :rtype: bool

        dfs(root) return a tuple of (bool, val)
        bool inddicates whether root is a unival tree
        val is the unival of the tree if bool is true.
        """

        if not root:
            return True

        if root.left:
            if root.val != root.left.val:
                return False

        if root.right:
            if root.val != root.right.val:
                return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

s = Solution()
root = TreeNode(5)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.left.right = TreeNode(0)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(5)
print(s.isUnivalTree(root))
