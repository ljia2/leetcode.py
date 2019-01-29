# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """

        Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

        Example:

        Input: 3
        Output:
        [
          [1,null,3,2],
          [3,2,null,1],
          [3,1,null,null,2],
          [2,1,3],
          [1,null,2,null,3]
        ]
        Explanation:
        The above output corresponds to the 5 unique BST's shown below:

           1         3     3      2      1
            \       /     /      / \      \
             3     2     1      1   3      2
            /     /       \                 \
           2     1         2                 3

        :type n: int
        :rtype: List[TreeNode]
        """

        if n <= 0:
            return []
        elif n == 1:
            return [TreeNode(1)]

        results = []
        for r in range(1, n+1, 1):
            left_trees = self.dfs(1, r-1)
            right_trees = self.dfs(r+1, n)

            for lt in left_trees:
                for rt in right_trees:
                    root = TreeNode(r)
                    root.left, root.right = lt, rt
                    results.append(root)

            return results

    #return the list of subtrees.
    def dfs(self, start, end):
        if start > end:
            return [None]
        elif start == end:
            return [TreeNode(start)]
        else:
            results = []
            for r in range(start, end+1, 1):
                left_trees = self.dfs(start, r-1)
                right_trees = self.dfs(r+1, end)
                for lt in left_trees:
                    for rt in right_trees:
                        root = TreeNode(r)
                        root.left, root.right = lt, rt
                        results.append(root)
            return results
