# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

        For example, given a 3-ary tree:

        We should return its level order traversal:

        [
             [1],
             [3,2,4],
             [5,6]
        ]


        Note:

        The depth of the tree is at most 1000.
        The total number of nodes is at most 5000.
        :type root: Node
        :rtype: List[List[int]]
        """

        if not root:
            return []

        queue = [root]
        ans = []
        while queue:
            size = len(queue)
            local_ans = []
            while size > 0:
                node = queue.pop(0)
                size -= 1
                local_ans.append(node.val)

                if node.children:
                    for child in node.children:
                        queue.append(child)
            ans.append(local_ans)
        return ans