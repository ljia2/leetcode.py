# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):

        """
        Given a binary tree, each node has value 0 or 1.
        Each root-to-leaf path represents a binary number starting with the most significant bit.
        For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

        For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

        Return the sum of these numbers.

        Example 1:

        Input: [1,0,1,0,1,0,1]
        Output: 22
        Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


        Note:

        The number of nodes in the tree is between 1 and 1000.
        node.val is 0 or 1.
        The answer will not exceed 2^31 - 1.

        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        ans = [0]
        self.dfs(root, 0, ans)
        return ans[0]

    def dfs(self, root, pathnum, ans):
        if not root.left and not root.right:
            pathnum = pathnum * 2 + root.val
            ans[0] += pathnum
            return

        pathnum = pathnum * 2 + root.val
        if root.left:
            self.dfs(root.left, pathnum, ans)
        if root.right:
            self.dfs(root.right, pathnum, ans)
        return

s = Solution()
root = TreeNode(1)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
print(s.sumRootToLeaf(root))

