# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root):
        """
        The thief has found himself a new place for his thievery again.
        There is only one entrance to this area, called the "root."
        Besides the root, each house has one and only one parent house.
        After a tour, the smart thief realized that "all houses in this place forms a binary tree".
        It will automatically contact the police if two directly-linked houses were broken into on the same night.

        Determine the maximum amount of money the thief can rob tonight without alerting the police.

        Example 1:

        Input: [3,2,3,null,3,null,1]

             3
            / \
           2   3
            \   \
             3   1

        Output: 7
        Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
        Example 2:

        Input: [3,4,5,1,3,null,1]

             3
            / \
           4   5
          / \   \
         1   3   1

        Output: 9
        Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
        :type root: TreeNode
        :rtype: int

        Very Typical Solution of Tree. Recursive call returns a set of different answers
        
        """
        if root is None:
            return 0

        include, exclude = self.dfs(root)
        return max(include, exclude)

    def dfs(self, root):
        if not root:
            return 0, 0

        linclude, lexclude = self.dfs(root.left)
        rinclude, rexclude = self.dfs(root.right)

        return root.val + lexclude + rexclude, max(linclude, lexclude) + max(rinclude, rexclude)

