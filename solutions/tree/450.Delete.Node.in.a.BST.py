# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root, key):
        """

        Given a root node reference of a BST and a key, delete the node with the given key in the BST.
        Return the root node reference (possibly updated) of the BST.

        Basically, the deletion can be divided into two stages:

        Search for a node to remove.
        If the node is found, delete the node.

        Note: Time complexity should be O(height of tree).

        Example:

        root = [5,3,6,2,4,null,7]
        key = 3

            5
           / \
          3   6
         / \   \
        2   4   7

        Given key to delete is 3. So we find the node with value 3 and delete it.

        One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

            5
           / \
          4   6
         /     \
        2       7

        Another valid answer is [5,2,6,null,4,null,7].

            5
           / \
          2   6
           \   \
            4   7

        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        if not root:
            return root
        if root.val == key:
            lt = root.left
            rt = root.right
            if lt and rt:
                # find the largest leaf node (new_root) in the left sub-tree
                # copy its value to original root
                # delete that node (new_root) from left sub-tree.
                # it will keep the tree balanced
                new_root = lt
                while new_root.right:
                    new_root = new_root.right
                root.val = new_root.val
                root.left = self.deleteNode(lt, new_root.val)
                return root
            elif lt or rt:
                return lt if lt else rt
            else:
                return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            root.left = self.deleteNode(root.left, key)
            return root

s = Solution()
root = TreeNode(0)
print(s.deleteNode(root, 0))
