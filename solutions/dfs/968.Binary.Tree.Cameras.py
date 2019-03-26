# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class GreedySolution(object):
    def minCameraCover(self, root):
        """
        Given a binary tree, we install cameras on the nodes of the tree.

        Each camera at a node can monitor its parent, itself, and its immediate children.

        Calculate the minimum number of cameras needed to monitor all nodes of the tree.

        Example 1:

        Input: [0,0,null,0,0]
        Output: 1
        Explanation: One camera is enough to monitor all nodes if placed as shown.
        Example 2:


        Input: [0,0,null,0,null,0,null,null,0]
        Output: 2
        Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

        Note:

        The number of nodes in the given tree will be in the range [1, 1000].
        Every node has value 0.

        :type root: TreeNode
        :rtype: int


        Consider a node in the tree. It can be covered by its parent, itself, its two children. Four options.

        Consider the root of the tree. It can be covered by left child, or right child, or itself. Three options.

        Consider one leaf of the tree. It can be covered by its parent or by itself. Two options.

        If we set a camera at the leaf, the camera can cover the leaf and its parent.
        If we set a camera at its parent, the camera can cover the leaf, its parent and its sibling.

        We can see that the second plan is always better than the first.
        Now we have only one option, set up camera to all leaves' parent.

        Here is our greedy solution:

        Set cameras on all leaves' parents, thenremove all covered nodes.
        Repeat step 1 until all nodes are covered.
        Explanation:

        Apply a recursive function dfs.

        Return 0 if it's a leaf.
        Return 1 if it's a parent of a leaf, with a camera on this node.
        Return 2 if it's covered, without a camera on this node.

        For each node,
        if it has a child, which is leaf (node 0), then it needs camera.
        if it has a child, which is the parent of a leaf (node 1), then it's covered.

        If it needs camera, then res++ and we return 1.
        If it's covered, we return 2.
        Otherwise, we return 0.

        """
        ans = [0]
        return (self.dfs(root, ans) == 0) + self.res

    def dfs(self, root, ans):
        if not root:
            return 2

        l, r = self.dfs(root.left), self.dfs(root.right)

        if l == 0 or r == 0:
            ans[0] += 1
            return 1

        return 2 if l == 1 or r == 1 else 0


class DPSolution(object):
    def minCameraCover(self, root):
        """
        Intuition

        Let's try to cover every node, starting from the top of the tree and working down.
        Every node considered must be covered by a camera at that node or some neighbor.

        Because cameras only care about local state, we can hope to leverage this fact for an efficient solution.
        Specifically, when deciding to place a camera at a node, we might have placed cameras to cover some subset
        of this node, its left child, and its right child already.

        Algorithm

        Let solve(node) be some information about how many cameras it takes to cover the subtree at this node in various states. There are essentially 3 states:

        [State 0] Strict subtree: All the nodes below this node are covered, but not this node.
        [State 1] Normal subtree: All the nodes below and including this node are covered, but there is no camera here.
        [State 2] Placed camera: All the nodes below and including this node are covered, and there is a camera here (which may cover nodes above this node).
        Once we frame the problem in this way, the answer falls out:

        To cover a strict subtree, the children of this node must be in state 1.
        To cover a normal subtree without placing a camera here, the children of this node must be in states 1 or 2, and at least one of those children must be in state 2.
        To cover the subtree when placing a camera here, the children can be in any state.
        :param root:
        :return:
        """
        def dfs(node):
            # given a tree, return a tuple of three values:
            # 0: Strict ST; the minimum number of cameras that all nodes below this are covered, but not this one
            # 1: Normal ST; the minimum number of cameras that all nodes below and incl this are covered - no camera
            # 2: Placed camera; the minimum number of cameras that all nodes below this are covered, plus camera here

            # base case
            if not node:
                return 0, 0, float('inf')

            L = dfs(node.left)
            R = dfs(node.right)

            # transitions
            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)

            return dp0, dp1, dp2

        return min(dfs(root)[1:])