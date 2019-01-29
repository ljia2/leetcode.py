# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """

        Given a binary tree, count the number of uni-value subtrees.

        A Uni-value subtree means all nodes of the subtree have the same value.

        Example :

        Input:  root = [5,1,5,5,5,null,5]

                      5
                     / \
                    1   5
                   / \   \
                  5   5   5

        Output: 4

        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        result = [0]
        self.isUnivalSubtree(root, result)
        return result[0]

    # traverse the tree
    # return a tuple of (whether it is a unival tree, the value of the unival tree).
    def isUnivalSubtree(self, root, count):
        if not root.left and not root.right:
            count[0] += 1
            return True, root.val

        if root.left:
            lrs, lval = self.isUnivailSubtree(root.left, count)
        else:
            lrs, lval = True, root.val

        if root.right:
            rrs, rval = self.isUnivailSubtree(root.right, count)
        else:
            rrs, rval = True, root.val

        if lrs and rrs and lval == rval == root.val:
            count[0] += 1
            return True, root.val
        else:
            return False, None
