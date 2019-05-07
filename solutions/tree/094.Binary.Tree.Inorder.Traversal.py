# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        Given a binary tree, return the inorder traversal of its nodes' values.

        Example:

        Input: [1,null,2,3]
           1
            \
             2
            /
           3

        Output: [1,3,2]
        Follow up: Recursive solution is trivial, could you do it iteratively?


        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = []
        while root or stack:
            # keep pushing all node in the left most branch into stack
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            ans.append(node.val)
            root = node.right
        return ans