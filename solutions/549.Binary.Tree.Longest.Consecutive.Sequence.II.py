# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode

class Solution:
    def longestConsecutive(self, root):
        """

        Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

        Especially, this path can be either increasing or decreasing.
        For example, [1,2,3,4] and [4,3,2,1] are both considered valid,
        but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order,
        where not necessarily be parent-child order.

        Example 1:
        Input:
                1
               / \
              2   3
        Output: 2
        Explanation: The longest consecutive path is [1, 2] or [2, 1].

        Example 2:
        Input:
                2
               / \
              1   3
        Output: 3
        Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
        Note: All the values of tree nodes are in the range of [-1e7, 1e7].

        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        longest = [0]
        self.dfs(root, longest)
        return longest[0]

    # return the increasing and decreasing consecutive path using root
    def dfs(self, root, ans):
        if not root.left and not root.right:
            if ans[0] < 1:
                ans[0] = 1
            return 1, 1
        else:
            if root.left:
                l1, l2 = self.dfs(root.left, ans)
            else:
                l1 = l2 = 0

            if root.right:
                r1, r2 = self.dfs(root.right, ans)
            else:
                r1 = r2 = 0

            rs1 = rs2 = 1
            longest1 = longest2 = 1

            if root.left:
                if root.val == root.left.val + 1:
                    rs1 += l1
                    longest1 += l1
                elif root.val == root.left.val - 1:
                    rs2 += l2
                    longest2 += l2

            if root.right:
                if root.val == root.right.val + 1:
                    rs1 = max(rs1, r1 + 1)
                    longest2 += r1
                elif root.val == root.right.val - 1:
                    rs2 = max(rs2, r2 + 1)
                    longest1 += r2

            longest = max(longest1, longest2)
            if ans[0] < longest:
                ans[0] = longest

            return rs1, rs2

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
print(s.longestConsecutive(root))