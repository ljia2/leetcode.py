# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode

class Solution:
    def postorderTraversal(self, root):
        """
        Given a binary tree, return the postorder traversal of its nodes' values.

        Example:

        Input: [1,null,2,3]
           1
            \
             2
            /
           3

        Output: [3,2,1]
        Follow up: Recursive solution is trivial, could you do it iteratively?
        
        :type root: TreeNode
        :rtype: List[int]

        How about use stack to push (root, root.right and root.left)


        T: O(n)
        S: O(n)

        """

        if not root:
            return []

        # intialize the stack with root
        stack = [root.val] + ([root.right] if root.right else []) + ([root.left] if root.left else [])

        ans = []
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.append(node.val)
                if node.left and node.right:
                    stack.append(node.right)
                    stack.append(node.left)
                elif node.left:
                    stack.append(node.left)
                elif node.right:
                    stack.append(node.right)
            else:
                ans.append(node)
        return ans


