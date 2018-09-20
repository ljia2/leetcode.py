# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode


class Solution:
    def maxPathSum(self, root):
        """
        Given a non-empty binary tree, find the maximum path sum.

        For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
        The path must contain at least one node and does not need to go through the root.

        Example 1:

        Input: [1,2,3]

               1
              / \
             2   3

        Output: 6
        Example 2:

        Input: [-10,9,20,null,null,15,7]

           -10
           / \
          9  20
            /  \
           15   7

        Output: 42

        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return None
        elif not root.left and not root.right:
            return root.val
        else:
            if root.left:
                lsum, mlsum = self.traversePathSum(root.left)
            else:
                lsum, mlsum = 0, -2**31

            if root.right:
                rsum, mrsum = self.traversePathSum(root.right)
            else:
                rsum, mrsum = 0, -2**31

            msum = max([root.val, root.val + lsum, root.val + rsum, root.val + lsum + rsum])
            return max([mlsum, mrsum, msum])

    def traversePathSum(self, node):
        """"
        :param node:
        :return: sum ending with node, max_sum within substree of node
        """

        if not node.left and not node.right:
            return node.val, node.val
        else:
            if node.left:
                lsum, mlsum = self.traversePathSum(node.left)
            else:
                lsum, mlsum = 0, -2**31

            if node.right:
                rsum, mrsum = self.traversePathSum(node.right)
            else:
                rsum, mrsum = 0, -2**31

            msum = max([node.val, node.val + lsum, node.val + rsum, node.val + lsum + rsum])
            return max([node.val, node.val + lsum, node.val + rsum]), max([mlsum, mrsum, msum])





s = Solution()
root = TreeNode(-2)
l1 = TreeNode(5)
r1 = TreeNode(2)
l1l = TreeNode(4)
l1r = TreeNode(3)
r1l = TreeNode(1)
r1r = TreeNode(-3)
l1.left = l1l
l1.right = l1r
r1.left = r1l
r1.right = r1r
root.left = l1
root.right = r1
print(s.maxPathSum(root))

root2 = TreeNode(2)
root2.left = TreeNode(-1)
root2.right = TreeNode(-2)
print(s.maxPathSum(root2))

n7 = TreeNode(7)
n2 = TreeNode(2)
n11 = TreeNode(11)
n11.left = n7
n11.right = n2
n4 = TreeNode(4)
n4.left = n11
n13 = TreeNode(13)
n4II = TreeNode(4)
n8 = TreeNode(8)
n8.left = n13
n8.right = n4II
n5 = TreeNode(5)
n5.left = n4
n5.right = n8
print(s.maxPathSum(n5))