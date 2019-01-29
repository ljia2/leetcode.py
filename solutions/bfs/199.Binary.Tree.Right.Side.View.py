# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

        Tree BFS via queue.

        """
        if not root:
            return []

        view = []
        # mimic queue to execute BFS
        q = [(0, root)]
        while q:
            size = len(q)
            while size > 0:
                l, node = q.pop(0)
                size -= 1

                # a right node is encountered.
                if size == 0:
                    view.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
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