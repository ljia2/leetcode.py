# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

        Note:

        Given target value is a floating point.
        You are guaranteed to have only one unique value in the BST that is closest to the target.
        Example:

        Input: root = [4,2,5,1,3], target = 3.714286

            4
           / \
          2   5
         / \
        1   3

        Output: 4
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root or target is None:
            raise Exception("Invalid Input")

        ans = [root.val]
        self.dfs(root, target, ans)
        return ans[0]

    def dfs(self, root, target, ans):
        if not root:
            return

        if abs(root.val - target) < abs(ans[0] - target):
            ans[0] = root.val

        if target <= root.val:
            self.dfs(root.left, target, ans)
        else:
            self.dfs(root.right, target, ans)
        return

