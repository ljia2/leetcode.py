# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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


        Typical usage of stack to dfs!!!!

        How about use stack to push (root, root.right and root.left)

        T: O(n)
        S: O(n)

        LC 173.

        """

        if not root:
            return []

        # initialize the stack with root
        stack = []
        ans = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.right

            root = stack.pop()
            ans.append(root.val)
            root = root.left
        return ans


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
s = Solution()
print(s.postorderTraversal(root))
