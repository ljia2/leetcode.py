# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        Implement an iterator over a binary search tree (BST).
        Your iterator will be initialized with the root node of a BST.

        Calling next() will return the next smallest number in the BST.

        Example:

        BSTIterator iterator = new BSTIterator(root);
        iterator.next();    // return 3
        iterator.next();    // return 7
        iterator.hasNext(); // return true
        iterator.next();    // return 9
        iterator.hasNext(); // return true
        iterator.next();    // return 15
        iterator.hasNext(); // return true
        iterator.next();    // return 20
        iterator.hasNext(); // return false

        Note:

        next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
        You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

        :type root: TreeNode

        Trick InOrderTravel.

        """
        self.node_stack = []
        # Initialize stack
        # Note that we recreate a "leaf" node valued as root.val.
        if root:
            if root.right:
                self.node_stack.append(root.right)
            self.node_stack.append(TreeNode(root.val))
            if root.left:
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
            # if it is a leaf node.
            if not node.left and not node.right:
                return node.val
            else:
                if node.right:
                    self.node_stack.append(node.right)
                # recreate a leaf node valued as node.val.
                self.node_stack.append(TreeNode(node.val))
                if node.left:
                    self.node_stack.append(node.left)



# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

def main():
    node2 = TreeNode(2)
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2.left = node1
    node2.right = node3
    node5 = TreeNode(5)
    node5.left = node2
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)
    node11 = TreeNode(11)
    node12 = TreeNode(12)
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