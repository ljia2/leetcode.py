# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        Given a binary search tree and the lowest and highest boundaries as L and R,
        trim the tree so that all its elements lies in [L, R] (R >= L).
        You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

            Example 1:
            Input:
                1
               / \
              0   2

              L = 1
              R = 2

            Output:
                1
                  \
                   2
            Example 2:
            Input:
                3
               / \
              0   4
               \
                2
               /
              1

              L = 1
              R = 3

            Output:
                  3
                 /
               2
              /
             1
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        if not root:
            return root

        lt = self.trimBST(root.left, L, R)
        rt = self.trimBST(root.right, L, R)

        if L <= root.val <= R:
            root.left, root.right = lt, rt
            return root
        elif root.val < L:
            return rt
        else:
            return lt

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

s = Solution()
print(s.trimBST(root, 1, 2))