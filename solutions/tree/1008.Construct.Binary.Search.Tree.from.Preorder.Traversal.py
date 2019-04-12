# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        Return the root node of a binary search tree that matches the given preorder traversal.

        (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val,
        and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first,
        then traverses node.left, then traverses node.right.)

        Example 1:

        Input: [8,5,1,7,10,12]
        Output: [8,5,10,1,7,null,12]

        Note:

        1 <= preorder.length <= 100
        The values of preorder are distinct.

        :type preorder: List[int]
        :rtype: TreeNode
        """

        if not preorder:
            return None

        root = preorder[0]

        left = []
        right = []
        for i in range(1, len(preorder)):
            if preorder[i] < root:
                left.append(preorder[i])
            else:
                right.append(preorder[i])
        ltree = self.bstFromPreorder(left)
        rtree = self.bstFromPreorder(right)

        ans = TreeNode(root)
        ans.left, ans.right = ltree, rtree
        return ans

s = Solution()
print(s.bstFromPreorder([8,5,1,7,10,12]))