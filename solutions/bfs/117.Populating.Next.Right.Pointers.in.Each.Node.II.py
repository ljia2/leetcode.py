# Definition for a Node.
class Node(object):
    def __init__(self, val, ):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

class BFSSolution(object):
    def connect(self, root):
        """
        Given a binary tree

        struct Node {
          int val;
          Node *left;
          Node *right;
          Node *next;
        }

        Populate each next pointer to point to its next right node.
        If there is no next right node, the next pointer should be set to NULL.

        Initially, all next pointers are set to NULL.

        Example:



        Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

        Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}

        Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.


        Note:

        You may only use constant extra space.
        Recursive approach is fine, implicit stack space does not count as extra space for this problem.

        :type root: Node
        :rtype: Node

        Clearly BFS is best. Can we leverage BFS with next?

        """
        if not root:
            return root

        prunner = root
        chead = ctail = None
        while prunner:
            if not ctail:
                if prunner.left:
                    chead = prunner.left
                    ctail = chead
                    if prunner.right:
                        ctail.next = prunner.right
                        ctail = ctail.next
                elif prunner.right:
                    chead = prunner.right
                    ctail = chead
            else:
                if prunner.left:
                    ctail.next = prunner.left
                    ctail = ctail.next
                    if prunner.right:
                        ctail.next = prunner.right
                        ctail = ctail.next
                elif prunner.right:
                    ctail.next = prunner.right
                    ctail = ctail.next

            prunner = prunner.next

            # when one level is exhausted, prunner points to chead; exit when there is no chead.
            if not prunner:
                prunner = chead
                chead = ctail = None
        return root


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.right.right = Node(8)

s = BFSSolution()
print(s.connect(root))


