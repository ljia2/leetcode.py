# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        A full binary tree is a binary tree where each node has exactly 0 or 2 children.

        Return a list of all possible full binary trees with N nodes.
        Each element of the answer is the root node of one possible tree.

        Each node of each tree in the answer must have node.val = 0.

        You may return the final list of trees in any order.

        Example 1:

        Input: 7
        Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
        Explanation:

        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []

        if N == 1:
            return [TreeNode(0)]
        ans = []
        for l in range(1, N-1, 2):
            ltrees = self.allPossibleFBT(l)
            rtrees = self.allPossibleFBT(N-l-1)
            if ltrees and rtrees:
                for ltree in ltrees:
                    for rtree in rtrees:
                        root = TreeNode(0)
                        root.left = ltree
                        root.right = rtree
                        ans.append(root)
        return ans
