# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        Given a binary tree, flatten it to a linked list in-place.

        For example, given the following tree:

            1
           / \
          2   5
         / \   \
        3   4   6
        The flattened tree should look like:

        1
         \
          2
           \
            3
             \
              4
               \
                5
                 \
                  6
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        ans, _ = self.tree2linkedlist(root)
        return ans

    def tree2linkedlist(self, root):
        if not root:
            return None, None

        if not root.left and not root.right:
            return root, root

        if not root.left:
            rhead, rtail = self.flatten(root.right)
            root.left = None
            root.right = rhead
            return root, rtail
        elif not root.right:
            lhead, ltail = self.flatten(root.left)
            root.left = None
            root.right = lhead
            return root, ltail
        else:
            lhead, ltail = self.tree2linkedlist(root.left)
            rhead, rtail = self.tree2linkedlist(root.right)
            root.left = None
            root.right = lhead
            ltail.right = rhead
            return root, rtail



