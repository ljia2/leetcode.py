# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flipMatchVoyage(self, root, voyage):
        """
        Given a binary tree with N nodes, each node has a different value from {1, ..., N}.
        A node in this binary tree can be flipped by swapping the left child and the right child of that node.
        Consider the sequence of N values reported by a preorder traversal starting from the root.
        Call such a sequence of N values the voyage of the tree.
        (Recall that a preorder traversal of a node means we report the current node's value,
        then preorder-traverse the left child, then preorder-traverse the right child.)

        Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.
        If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.
        If we cannot do so, then return the list [-1].



        Example 1:
        Input: root = [1,2], voyage = [2,1]
        Output: [-1]

        Example 2:
        Input: root = [1,2,3], voyage = [1,3,2]
        Output: [1]

        Example 3:
        Input: root = [1,2,3], voyage = [1,2,3]
        Output: []


        Note: 1 <= N <= 100
        https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/description/

        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]

        use dfs to preorder traverse and compare:
        """
        ans = []
        # indicate which position of voyage it should compare.
        # initialize the start position of root.
        pos = [0]
        return ans if self.dfs(root, voyage, pos, ans) else [-1]

    # return boolean whether root match voyage[start:] via flipping or not
    def dfs(self, root, voyage, pos, ans):
        if not root:
            return True
        if root.val != voyage[pos[0]]:
            return False

        pos[0] += 1
        if root.left and root.left.val != voyage[pos[0]]:
            ans.append(root.val)
            root.left, root.right = root.right, root.left

        return self.dfs(root.left, voyage, pos, ans) and self.dfs(root.right, voyage, pos, ans)

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(s.flipMatchVoyage(root, [1,3,2]))










