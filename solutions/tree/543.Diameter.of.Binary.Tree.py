# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        Given a binary tree, you need to compute the length of the diameter of the tree.
        The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
         This path may or may not pass through the root.

        Example:
        Given a binary tree
                  1
                 / \
                2   3
               / \
              4   5
        Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

        Note: The length of path between two nodes is represented by the number of edges between them.
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ans = [0]
        lh = self.dfs(root.left, ans)
        rh = self.dfs(root.right, ans)

        ans[0] = max(ans[0], lh + rh + 2)
        return ans[0]

    def dfs(self, root, ans):
        # None is -1 -> leaf node of height of 0
        if not root:
            return -1

        lh = self.dfs(root.left, ans)
        rh = self.dfs(root.right, ans)

        ans[0] = max(ans[0], lh + rh + 2)
        return max(lh, rh) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
s = Solution()
print(s.diameterOfBinaryTree(root))
