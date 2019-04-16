import math

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B
        where V = |A.val - B.val| and A is an ancestor of B.

        (A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

        Example 1:

        Input: [8,3,10,1,6,null,14,null,null,4,7,13]
        Output: 7
        Explanation:
        We have various ancestor-node differences, some of which are given below :
        |8 - 3| = 5
        |3 - 7| = 4
        |8 - 1| = 7
        |10 - 13| = 3
        Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.


        :type root: TreeNode
        :rtype: int


        how about dfs over tree with root r return a tuple, max val child whose ancestor is r , min val child whose ancestor is r

        """

        if not root:
            raise Exception("input root is invalid!")

        if not root.left and not root.right:
            return Exception("input root is invalid!")

        max_dist = [-10**9]
        _, _ = self.dfs(root, max_dist)

        return max_dist[0]

    def dfs(self, root, max_dist):
        if not root:
            return -10**9, 10**9

        if not root.left and not root.right:
            return root.val, root.val

        lmax, lmin = self.dfs(root.left, max_dist)
        rmax, rmin = self.dfs(root.right, max_dist)

        max_val = max(lmax, rmax)
        min_val = min(lmin, rmin)

        # update the max_distance.
        if root.val >= max_val:
            max_dist[0] = max(max_dist[0], root.val - min_val)
        elif root.val <= min_val:
            max_dist[0] = max(max_dist[0], max_val - root.val)
        else:
            max_dist[0] = max(max_dist[0], max(abs(root.val - min_val), abs(root.val - max_val)))

        return max(root.val, max_val), min(root.val, min_val)