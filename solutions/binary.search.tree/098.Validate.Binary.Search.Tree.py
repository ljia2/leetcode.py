# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# post order check
class PostOrderSolution(object):
    def isValidBST(self, root):
        """
        Given a binary tree, determine if it is a valid binary search tree (BST).

        Assume a BST is defined as follows:

        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.
        Example 1:

        Input:
            2
           / \
          1   3
        Output: true
        Example 2:

            5
           / \
          1   4
             / \
            3   6
        Output: false
        Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
                     is 5 but its right child's value is 4.
                     
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        lres, lmin, lmax = self.dfs(root.left)
        rres, rmin, rmax = self.dfs(root.right)

        return lres and rres and lmax < root.val < rmin

    def dfs(self, root):
        if not root:
            return True, float('inf'), float('-inf')

        lres, lmin, lmax = self.dfs(root.left)
        rres, rmin, rmax = self.dfs(root.right)

        return lres and rres and lmax < root.val < rmin, min(lmin, root.val), max(root.val, rmax)


class PreOrderSolution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        return self.dfs(root, float("-inf"), float('inf'))

    # preorder use root.val to bound verification of left/right tree.
    def dfs(self, root, minv, maxv):
        if not root:
            return True

        if root.val >= maxv or root.val <= minv:
            return False

        return self.dfs(root.left, minv, root.val) and self.dfs(root.right, root.val, maxv)


class InOrderSolution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.dfs(root, None)

    # prev store the previous node of root; keep updating it when processing root.
    def dfs(self, root, prev):
        if not root:
            return True

        # check left
        if not self.dfs(root.left, prev):
            return False

        # check root
        if prev and prev.val > root.val:
            return False
        prev = root

        # check right
        return self.dfs(root.right, prev)


class IterativeInOrderSolution(object):
    def isValidBST(self, root):
        """
        Given a binary tree, determine if it is a valid binary search tree (BST).

        Assume a BST is defined as follows:

        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.
        Example 1:

        Input:
            2
           / \
          1   3
        Output: true
        Example 2:

            5
           / \
          1   4
             / \
            3   6
        Output: false
        Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
                     is 5 but its right child's value is 4.

        :type root: TreeNode
        :rtype: bool

        # InOrderTravel of BST by Stack
        public List<Integer> inorderTraversal(TreeNode root) {
            List<Integer> list = new ArrayList<>();
            if(root == null) return list;
            Stack<TreeNode> stack = new Stack<>();
            while(root != null || !stack.empty()){
                while(root != null){
                    stack.push(root);
                    root = root.left;
                }
                root = stack.pop();
                list.add(root.val);
                root = root.right;
            }
            return list;
        }
        """

        if not root:
            return True
        stack = []
        prev = None
        while root or stack:
            # push root and all left children into stack
            while root:
                stack.append(root)
                root = root.left
            # pop the node
            root = stack.pop()

            if prev and root.val <= prev.val:
                return False
            prev = root

            # reset node to its right children.
            root = root.right
        return True