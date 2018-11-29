# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root, V):
        """
        Input: root = [4,2,6,1,3,5,7], V = 2
        Output: [[2,1],[4,3,6,null,null,5,7]]
        Explanation:
        Note that root, output[0], and output[1] are TreeNode objects, not arrays.

        The given tree [4,2,6,1,3,5,7] is represented by the following diagram:

                  4
                /   \
              2      6
             / \    / \
            1   3  5   7

        while the diagrams for the outputs are:

                  4
                /   \
              3      6      and    2
                    / \           /
                   5   7         1
        Note:

        The size of the BST will not exceed 50.
        The BST is always valid and each node's value is different.

        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """

