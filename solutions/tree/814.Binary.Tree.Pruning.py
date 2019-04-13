# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root):
        """
        We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

        Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

        (Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

        Example 1:
        Input: [1,null,0,0,1]
        Output: [1,null,0,null,1]

        Explanation:
        Only the red nodes satisfy the property "every subtree not containing a 1".
        The diagram on the right represents the answer.


        Example 2:
        Input: [1,0,1,0,0,0,1]
        Output: [1,null,1,null,1]



        Example 3:
        Input: [1,1,0,1,1,0,1,0]
        Output: [1,1,0,1,1,null,1]

        Note:

        The binary tree will have at most 100 nodes.
        The value of each node will only be 0 or 1.
        :type root: TreeNode
        :rtype: TreeNode

        dfs(root) return whether root is pruned or not.
        """
        if self.dfs(root):
            return None
        else:
            return root

    def dfs(self, root):
        if not root:
            return True

        lprune = self.dfs(root.left)
        rprune = self.dfs(root.right)

        if lprune:
            root.left = None
        if rprune:
            root.right = None

        if root.val == 0 and lprune and rprune:
            return True
        else:
            return False
