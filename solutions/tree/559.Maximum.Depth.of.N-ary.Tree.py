# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        Given a n-ary tree, find its maximum depth.

        The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

        For example, given a 3-ary tree:


        We should return its max depth, which is 3.

        :type root: Node
        :rtype: int

        typical usage of dfs and track the deepest length.

        """
        if not root:
            return 0

        ans = [0]
        self.dfs(root, 1, ans)
        return ans[0]

    def dfs(self, root, level, ans):
        if not root.children:
            ans[0] = max(ans[0], level)
            return

        for child in root.children:
            self.dfs(child, level + 1, ans)
        return
