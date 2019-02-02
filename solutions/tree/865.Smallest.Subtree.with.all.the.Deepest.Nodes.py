from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

        A node is deepest if it has the largest depth possible among any node in the entire tree.

        The subtree of a node is that node, plus the set of all descendants of that node.

        Return the node with the largest depth such that it contains all the deepest nodes in its subtree.



        Example 1:

        Input: [3,5,1,6,2,0,8,null,null,7,4]
        Output: [2,7,4]
        Explanation:



        We return the node with value 2, colored in yellow in the diagram.
        The nodes colored in blue are the deepest nodes of the tree.
        The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
        The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
        Both the input and output have TreeNode type.


        Note:

        The number of nodes in the tree will be between 1 and 500.
        The values of each node are unique.

        :type root: TreeNode
        :rtype: TreeNode

        Classic !!!!
        can you do it by one pass of tree?

        how about dfs return the height of root and current optimal solution so far.

        """
        if not root:
            return root

        _, ans = self.dfs(root)
        return ans

    def dfs(self, root):
        if not root.left and not root.right:
            return 0, root

        if root.left:
            lh, lopt = self.dfs(root.left)
        else:
            lh, lopt = -1, None

        if root.right:
            rh, ropt = self.dfs(root.right)
        else:
            rh, ropt = -1, None

        # when left and right subtree have the same height, the current root will be the deepest subtree containing all the deepest nodes
        if lh == rh:
            return lh + 1, root
        # if left tree is deeper than the right tree, lopt must be the solution (the deepest subtree containing all the deepest nodes.
        elif lh > rh:
            return lh + 1, lopt
        # otherwise, ropt must be the solution.
        elif lh < rh:
            return rh + 1, ropt


s = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
print(s.subtreeWithAllDeepest(root))

