# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        p and q must be in the tree?

        """
        if root in [None, p, q]:
            return root

        lroot = self.lowestCommonAncestor(root.left, p, q)
        rroot = self.lowestCommonAncestor(root.right, p, q)
        return root if lroot and rroot else lroot or rroot


s = Solution()
root = TreeNode(1)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.right = TreeNode(3)
print(s.lowestCommonAncestor(root, root.left, root.left.left))


class SolutionII(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        What if a node not in the tree? we can use nodes to print path.

        """
        if not root:
            return root

        ans = []
        node_set = self.dfs(root, p, q, ans)
        if ans:
            return ans[0]
        elif p in node_set and q in node_set:
            return root
        else:
            return None

    # postorder dfs
    def dfs(self, root, p, q, ans):
        if not root:
            return set()

        lnodes = self.dfs(root.left, p, q, ans)
        rnodes = self.dfs(root.right, p, q, ans)

        # union nodes from left and right substress
        nodes = lnodes & rnodes
        nodes.add(root)

        if not ans:
            if p in nodes and q in nodes:
                ans.append(root)

        return nodes

s = SolutionII()
root = TreeNode(1)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.right = TreeNode(3)
print(s.lowestCommonAncestor(root, root.left.left, TreeNode(4)))

### Follow up, what is we want to print the path from root to that LCA?
import copy

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: List[Int]

        print path from root to LCA

        """
        if not root:
            return

        paths = []
        self.dfs(root, p, q, [], paths)

        if len(paths) != 2:
            raise Exception("Invalid Input! No LCA")
        else:
            i = 0
            while i < len(paths[0]) and j < len(paths[1]) and paths[0][i] == paths[1][j]:
                i += 1
                j += 1
            return paths[0][:i]

    def dfs(self, node, p, q, path, paths):
        if node in [p, q]:
            # store a path from root to p/q.
            paths.append(copy.copy(path))
            return

        # backtracking
        if node.left:
            path.append(node.left.val)
            self.dfs(node.left, p, q, path, paths)
            path.pop()

        if node.right:
            path.append(node.right.val)
            self.dfs(node.right, p, q, path, paths)
            path.pop()
        return


## Follow up: can we use iteratively?

class IterativeSolution:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)

            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q