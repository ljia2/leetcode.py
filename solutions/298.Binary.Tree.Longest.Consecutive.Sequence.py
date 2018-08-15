# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            # edge case of None/invalid inputs
            return 0
        elif root.left is None and root.right is None:
            # leaf node return 1 because it is a sequence of 1
            return 1
        else:
            return self.DFS(root, 1)
        
    # simply a restricted tree DFS
    def DFS(self, node, level):
        if node is None:
            return level

        if node.left is not None and node.val + 1 == node.left.val:
            left_rs = self.DFS(node.left, level+1)
        else:
            left_rs = max(level, self.DFS(node.left, 1))

        if node.right is not None and node.val + 1 == node.right.val:
            right_rs = self.DFS(node.right, level+1)
        else:
            right_rs = max(level, self.DFS(node.right, 1))
        return max(left_rs, right_rs)
