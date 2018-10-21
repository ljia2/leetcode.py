# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode

class Solution:
    def longestUnivaluePath(self, root):
        """

        Given a binary tree, find the length of the longest path where each node in the path has the same value.
        This path may or may not pass through the root.

        Note: The length of path between two nodes is represented by the number of edges between them.

        Example 1:

        Input:

                      5
                     / \
                    4   5
                   / \   \
                  1   1   5
        Output:

        2
        Example 2:

        Input:

                      1
                     / \
                    4   5
                   / \   \
                  4   4   5
        Output:

        2
        Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

        :type root: TreeNode
        :rtype: int

        just recursively call on a tree and return a tuple of (the length of unival path using root)
        
        """

        if not root:
            return 0
        ans = [-1]
        _ = self.calcLongestUnivalPath(root, ans)
        return ans[0]

    def calcLongestUnivalPath(self, root, ans):
        # exit, a leaf node
        if not root.left and not root.right:
            if ans[0] < 0:
                ans[0] = 0
            return 0

        lup = self.calcLongestUnivalPath(root.left, ans) if root.left else 0
        rup = self.calcLongestUnivalPath(root.right, ans) if root.right else 0

        # the unival path by using root
        up = 0
        # the longest unival path within the subtree of root.
        new_answer = 0
        if root.left and root.val == root.left.val:
            up = max(up, lup + 1)
            new_answer += lup + 1
        if root.right and root.val == root.right.val:
            up = max(up, rup + 1)
            new_answer += rup + 1
        if ans[0] < new_answer:
            ans[0] = new_answer
        return up


s = Solution()
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)
print(s.longestUnivaluePath(root))
