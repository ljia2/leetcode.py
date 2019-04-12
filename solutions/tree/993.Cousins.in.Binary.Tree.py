# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

        Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

        We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

        Return true if and only if the nodes corresponding to the values x and y are cousins.



        Example 1:


        Input: root = [1,2,3,4], x = 4, y = 3
        Output: false
        Example 2:


        Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
        Output: true
        Example 3:


        Input: root = [1,2,3,null,4], x = 2, y = 3
        Output: false


        Note:

        The number of nodes in the tree will be between 2 and 100.
        Each node has a unique integer value from 1 to 100.

        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

        if not root:
            return False

        if x == y:
            return False

        node_dict = dict()
        self.dfs(root, None, 0, node_dict)

        lx, px = node_dict[x]
        ly, py = node_dict[y]

        return lx == ly and px != py

    def dfs(self, root, pval, level, node_dict):
        if not root.left and not root.right:
            node_dict[root.val] = (level, pval)
            return

        node_dict[root.val] = (level, pval)

        if root.left:
            self.dfs(root.left, root.val, level + 1, node_dict)
        if root.right:
            self.dfs(root.right, root.val, level + 1, node_dict)
        return 

