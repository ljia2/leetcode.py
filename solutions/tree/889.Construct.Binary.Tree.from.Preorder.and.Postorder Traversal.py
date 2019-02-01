# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        Return any binary tree that matches the given preorder and postorder traversals.

        Values in the traversals pre and post are distinct positive integers.

        Example 1:

        Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
        Output: [1,2,3,4,5,6,7]

        Note:
        1 <= pre.length == post.length <= 30
        pre[] and post[] are both permutations of 1, 2, ..., pre.length.
        It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre and not post:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1 and len(post) == 1:
            return root
        else:
            if pre[1] == post[-2]:
                lpre, lpost = pre[1:], post[:len(post)-1]
                ltree = self.constructFromPrePost(lpre, lpost)
                root.left = ltree
            else:
                lpre = pre[1:pre.index(post[-2])]
                lpost = post[:post.index(pre[1]) + 1]
                rpre = pre[pre.index(post[-2]):]
                rpost = post[post.index(pre[1])+1:-1]
                ltree = self.constructFromPrePost(lpre, lpost)
                rtree = self.constructFromPrePost(rpre, rpost)
                root.left, root.right = ltree, rtree
            return root

