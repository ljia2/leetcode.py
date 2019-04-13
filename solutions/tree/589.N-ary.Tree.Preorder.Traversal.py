# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        Given an n-ary tree, return the preorder traversal of its nodes' values.

        For example, given a 3-ary tree:

        Return its preorder traversal as: [1,3,5,6,2,4].

        Note:

        Recursive solution is trivial, could you do it iteratively?
        :type root: Node
        :rtype: List[int]
        """

        if not root:
            return []

        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            if not node.children:
                ans.append(node.val)
            else:
                ans.append(Node(node.val))
                for i in range(len(node.children)-1, -1, -1):
                    stack.append(node.children[i])
        return ans

