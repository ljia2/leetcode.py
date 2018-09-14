# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import utils.TreeNode as t

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.node_stack = []
        if root is not None:
            if root.right is not None:
                self.node_stack.append(root.right)
            self.node_stack.append(t.TreeNode(root.val))
            if root.left is not None:
                self.node_stack.append(root.left)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.node_stack) > 0

    def next(self):
        """
        :rtype: int
        """
        while self.node_stack:
            node = self.node_stack.pop()
            if node.left is None and node.right is None:
                return node.val
            else:
                if node.right is not None:
                    self.node_stack.append(node.right)
                self.node_stack.append(t.TreeNode(node.val))
                if node.left is not None:
                    self.node_stack.append(node.left)



# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

def main():
    node2 = t.TreeNode(2)
    node1 = t.TreeNode(1)
    node3 = t.TreeNode(3)
    node2.left = node1
    node2.right = node3
    node5 = t.TreeNode(5)
    node5.left = node2
    node6 = t.TreeNode(6)
    node7 = t.TreeNode(7)
    node8 = t.TreeNode(8)
    node9 = t.TreeNode(9)
    node10 = t.TreeNode(10)
    node11 = t.TreeNode(11)
    node12 = t.TreeNode(12)
    node7.left = node6
    node8.left = node7
    node9.left = node8
    node11.left = node10
    node11.right = node12
    node9.right = node11
    node5.right = node9

    i, v = BSTIterator(node5), []
    while i.hasNext():
        v.append(i.next())
    print(v)

if __name__ == "__main__":
    main()