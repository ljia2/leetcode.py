# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        Given an n-ary tree, return the postorder traversal of its nodes' values.

        For example, given a 3-ary tree:
        Return its postorder traversal as: [5,6,3,2,4,1].


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
                stack.append(node.val)
                for i in range(len(node.children)-1, -1, -1):
                    stack.append(node.children[i])
        return ans



