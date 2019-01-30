# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root):
        """
        Given a binary tree, determine if it is a complete binary tree.

        Definition of a complete binary tree from Wikipedia:

        In a complete binary tree every level, except possibly the last, is completely filled,
        and all nodes in the last level are as far left as possible.
        It can have between 1 and 2h nodes inclusive at the last level h.

        Example 1:
        Input: [1,2,3,4,5,6]
        Output: true
        Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.


        Example 2:



        Input: [1,2,3,4,5,null,7]
        Output: false
        Explanation: The node with value 7 isn't as far left as possible.

        Note:

        The tree will have between 1 and 100 nodes.
        :type root: TreeNode
        :rtype: bool
        dfs(root) return (full tree, complete tree, hight of the tree).
        """
        _, ans, _ = self.dfs(root, 0)
        return ans

    def dfs(self, root, level):
        if not root:
            return True, True, level - 1

        lf, lc, ll = self.dfs(root.left, level + 1)
        rf, rc, rl = self.dfs(root.right, level + 1)

        isfull = lf and rf and ll == rl
        isComplete = (lf and rc and ll == rl) or (lc and rf and ll == rl + 1)
        return isfull, isComplete, max(ll, rl)

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print(s.isCompleteTree(root))