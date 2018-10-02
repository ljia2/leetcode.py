from utils.TreeNode import TreeNode

class Solution: # Brute Force (TLE)
    def findDuplicateSubtrees(self, root):
        """
        Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

        Two trees are duplicate if they have the same structure with same node values.

        Example 1:

                1
               / \
              2   3
             /   / \
            4   2   4
               /
              4
        The following are two duplicate subtrees:

              2
             /
            4
        and

            4
        Therefore, you need to return above trees' root in the form of a list.

        :type root: TreeNode
        :rtype: List[TreeNode]


        Note: recursively determine whether two tree are identical.

        DFS first and then for each pair of nodes determine whether they are identical.

        T: O(n^3)
        S: O(n)


        """
        if not root:
            return []

        s = [root]
        nodes = []
        while s:
            n = s.pop()
            if n.right:
                s.append(n.right)
            if n.left:
                s.append(n.left)
            nodes.append(n)

        result = []
        paired = []
        for i in range(len(nodes)-1):
            if nodes[i] in paired:
                continue
            for j in range(i+1, len(nodes)):
                if self.isSameTree(nodes[i], nodes[j]):
                    if nodes[i] not in result:
                        result.append(nodes[i])
                    paired.append(nodes[j])
        return result

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class SolutionII:
    def findDuplicateSubtrees(self, root):
        """
        Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

        Two trees are duplicate if they have the same structure with same node values.

        Example 1:

                1
               / \
              2   3
             /   / \
            4   2   4
               /
              4
        The following are two duplicate subtrees:

              2
             /
            4
        and

            4
        Therefore, you need to return above trees' root in the form of a list.

        :type root: TreeNode
        :rtype: List[TreeNode]


        DFS first and then serialize each node

        # encoding all nodes of tree. Encode a node in the tree is O(n) and then encoding all nodes is O(n^2)
        T: O(n^2)
        # an key might be O(n) and there might be n keys and thus space is O(n^2)
        S: O(n^2)
        """

        if not root:
            return []

        # key: serialization string; value the list of nodes
        node_dict = dict()
        s = [root]
        while s:
            n = s.pop()
            encode = self.encodeNode(n)
            node_dict[encode] = node_dict.get(encode, []) + [n]
            if n.right:
                s.append(n.right)
            if n.left:
                s.append(n.left)

        result = []
        for k, v in node_dict.items():
            if len(v) > 1:
                result.append(v[0])
        return result

    def encodeNode(self, n):
        if not n:
            return ""
        else:
            return "(" + str(n.val) + "," + self.encodeNode(n.left) + "," + self.encodeNode(n.right) + ")"

class BestSolution:
    def findDuplicateSubtrees(self, root):
        """
        Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

        Two trees are duplicate if they have the same structure with same node values.

        Example 1:

                1
               / \
              2   3
             /   / \
            4   2   4
               /
              4
        The following are two duplicate subtrees:

              2
             /
            4
        and

            4
        Therefore, you need to return above trees' root in the form of a list.

        :type root: TreeNode
        :rtype: List[TreeNode]


        Post order traverse the tree and express each node by a tuple (node.val, id of left, id of right) where id the order of such a distict node's expression is created.
        For a leaf node, we use (node.val, 0, 0) as the expression.

        """

        if not root:
            return []

        # key: node; value is the value of its expression given in exprs
        node2expr = dict()
        # key: tuple and value the order of its appears in post order traverse
        exprs = dict()
        # encode the node with expression by post order traverse
        self.potEncoding(root, node2expr, exprs)

        expr2nodes = dict()
        for (k, v) in node2expr.items():
            expr2nodes[v] = expr2nodes.get(v, []) + [k]

        result = []
        for nodes in expr2nodes.values():
            if len(nodes) > 1:
                result.append(nodes[0])
        return result

    def potEncoding(self, root, n2e, exprs):
        if root and not root.left and not root.right:
            expr = (root.val, 0, 0)
            if expr not in exprs.keys():
                exprs[expr] = len(exprs) + 1
            n2e[root] = exprs[expr]
        else:
            if root.left:
                self.potEncoding(root.left, n2e, exprs)
            if root.right:
                self.potEncoding(root.right, n2e, exprs)

            lexpr = n2e[root.left] if root.left else 0
            rexpr = n2e[root.right] if root.right else 0
            expr = (root.val, lexpr, rexpr)

            if expr not in exprs.keys():
                exprs[expr] = len(exprs) + 1
            n2e[root] = exprs[expr]
        return
