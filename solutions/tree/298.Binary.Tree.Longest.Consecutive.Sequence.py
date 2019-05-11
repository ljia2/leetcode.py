# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        """
        Given a binary tree, find the length of the longest consecutive sequence path.

        The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
        The longest consecutive path need to be from parent to child (cannot be the reverse).

        Example 1:

        Input:

           1
            \
             3
            / \
           2   4
                \
                 5

        Output: 3

        Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
        Example 2:

        Input:

           2
            \
             3
            /
           2
          /
         1

        Output: 2

        Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
        :type root: TreeNode
        :rtype: int

        Typical dfs over tree.

        """

        if not root:
            # edge case of None/invalid inputs
            return 0
        if not root.left and not root.right:
            # leaf node return 1 because it is a sequence of 1
            return 1

        return self.dfs(root, 1)
        
    # simply a restricted tree dfs, return the
    def dfs(self, node, level):
        if not node:
            return level

        if node.left and node.val + 1 == node.left.val:
            left_rs = self.dfs(node.left, level+1)
        else:
            left_rs = max(level, self.dfs(node.left, 1))

        if node.right and node.val + 1 == node.right.val:
            right_rs = self.dfs(node.right, level+1)
        else:
            right_rs = max(level, self.dfs(node.right, 1))
        return max(left_rs, right_rs)
