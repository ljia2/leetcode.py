# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

        For example:
        Given binary tree [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
        return its zigzag level order traversal as:
        [
          [3],
          [20,9],
          [15,7]
        ]
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        ans = []
        queue = [root]
        level = 0
        while queue:
            size = len(queue)
            lans = []
            while size > 0:
                node = queue.pop(0)
                size -= 1

                lans.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 0:
                ans.append(lans)
            else:
                lans.reverse()
                ans.append(lans)
            level += 1
        return ans

