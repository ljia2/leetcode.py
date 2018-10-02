# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode

class Solution:
    def rightSideView(self, root):
        """

        Given a binary tree, imagine yourself standing on the right side of it,
        return the values of the nodes you can see ordered from top to bottom.

        Example:

        Input: [1,2,3,null,5,null,4]
        Output: [1, 3, 4]
        Explanation:

           1            <---
         /   \
        2     3         <---
         \     \
          5     4       <---
        :type root: TreeNode
        :rtype: List[int]

        BFS + (node, level) in queue.

        """
        if not root:
            return []
        else:
            view = []
            # mimic queue to execute BFS
            q = [(0, root)]
            while q:
                l, node = q.pop(0)
                if not q:
                    view.append(node.val)
                else:
                    nl, nn = q[0]
                    if l < nl:
                        view.append(node.val)
                if node.left:
                    q.append((l+1, node.left))
                if node.right:
                    q.append((l+1, node.right))
            return view


s = Solution()
root = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
root.left, root.right = n2, n3
n4 = TreeNode(4)
n5 = TreeNode(5)
n2.right = n5
n3.right = n4
print(s.rightSideView(root))