# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        Given a Binary Search Tree (BST) with the root node root,
        return the minimum difference between the values of any two different nodes in the tree.

        Example :
        Input: root = [4,2,6,1,3,null,null]
        Output: 1

        Explanation:
        Note that root is a TreeNode object, not an array.
        The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

                  4
                /   \
              2      6
             / \
            1   3

        while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.

        Note:
        The size of the BST will be between 2 and 100.
        The BST is always valid, each node's value is an integer, and each node's value is different.

        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        ans = [2**31]
        lmax, _ = self.dfs(root.left, ans)
        _, rmin = self.dfs(root.right, ans)

        if lmax and rmin:
            newdiff = min(abs(lmax - root.val), abs(rmin - root.val))
        elif lmax:
            newdiff = abs(lmax - root.val)
        elif rmin:
            newdiff = abs(rmin - root.val)
        else:
            newdiff = 2**31

        return min(newdiff, ans[0])

    def dfs(self, root, ans):
        if root is None:
            return None, None

        lmax, lmin = self.dfs(root.left, ans)
        rmax, rmin = self.dfs(root.right, ans)

        if lmax and rmin:
            newdiff = min(abs(lmax - root.val), abs(rmin - root.val))
        elif lmax:
            newdiff = abs(lmax - root.val)
        elif rmin:
            newdiff = abs(rmin - root.val)
        else:
            newdiff = 2**31
        if ans[0] > newdiff:
            ans[0] = newdiff

        # return the max and min value in the tree root.
        return rmax if root.right else root.val, lmin if root.left else root.val
