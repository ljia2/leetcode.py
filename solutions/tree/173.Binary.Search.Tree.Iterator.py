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

        Calling next() will return the next smallest 5 in the BST.

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
        # Initialize stack, push all the node on the leftmost path into stack.
        self.pushAll(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.node_stack

    def next(self):
        """
        :rtype: int
        """
        while self.node_stack:
            node = self.node_stack.pop()
            self.pushAll(node.right)
            return node.val

    def pushAll(self, node):
        while node:
            self.node_stack.append(node)
            node = node.left


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

###### what if a node with parent and do not use stack.

class ParentTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


class BSPTIterator(object):
    def __init__(self, root):
        """
        Implement an iterator over a binary search tree (BST).
        Your iterator will be initialized with the root node of a BST.

        Calling next() will return the next smallest 5 in the BST.

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
        self.curr = root

    def hasNext(self):
        """
        :rtype: bool
        """
        succ = self.findSuccessor(self.curr)
        self.curr = succ
        return succ is not None

    def next(self):
        """
        :rtype: int
        """
        return self.curr.val

    def findSuccssor(self, node):
        if not node:
            return None

        if node.right:
            tmp = node.right
            while tmp and tmp.left:
                tmp = tmp.left
            return tmp

        father = node.parent
        child = node
        while father and father.left != child:
            child = father
            father = father.parent
        return father



