# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class RecursiveSolution(object):
    def isSymmetric(self, root):
        """
        Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

        For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

            1
           / \
          2   2
         / \ / \
        3  4 4  3


        But the following [1,2,2,null,3,null,3] is not:

            1
           / \
          2   2
           \   \
           3    3


        Note:
        Bonus points if you could solve it both recursively and iteratively.

        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.isMirrored(root.left, root.right)

    def isMirrored(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        return root1.val == root2.val \
               and self.isMirrored(root1.left, root2.right) \
               and self.isMirrored(root1.right, root2.left)


class IterativeSolution(object):
    def isSymmetric(self, root):
        """
        Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

        For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

            1
           / \
          2   2
         / \ / \
        3  4 4  3


        But the following [1,2,2,null,3,null,3] is not:

            1
           / \
          2   2
           \   \
           3    3


        Note:
        Bonus points if you could solve it both recursively and iteratively.

        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if not root.left and not root.right:
            return True

        queue = [(root, root)]
        while queue:
            node1, node2 = queue.pop(0)

            # skip None
            if not node1 and not node2:
                continue

            # not mirror
            if not node1 or not node2 or node1.val != node2.val:
                return False

            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))

        return True




