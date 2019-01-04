"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        """

        You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer,
        which may or may not point to a separate doubly linked list.
        These child lists may have one or more children of their own, and so on, to produce a multilevel data structure,
        as shown in the example below.

        Flatten the list so that all the nodes appear in a single-level, doubly linked list.
        You are given the head of the first level of the list.


        Example:

        Input:
         1---2---3---4---5---6--NULL
                 |
                 7---8---9---10--NULL
                     |
                     11--12--NULL

        Output:
        1-2-3-7-8-11-12-9-10-4-5-6-NULL

        :type head: Node
        :rtype: Node

        DFS + left pointing to parent.

        """
        if not head:
            return head
        head, _ = self.dfs(head)
        return head

    def dfs(self, root):
        """
        :param root:
        :return: head and tail of flatten list of root
        """
        # leaf node
        if not root.next and not root.child:
            return root, root

        if root.child and root.next:
            lh, lt = self.dfs(root.child)
            rh, rt = self.dfs(root.next)

            root.child = None
            root.next = lh
            lh.prev = root
            lt.next = rh
            rh.prev = lt
            return root, rt
        elif root.child:
            lh, lt = self.dfs(root.child)
            root.child = None
            root.next = lh
            lh.prev = root
            return root, lt
        else:
            rh, rt = self.dfs(root.next)
            root.child = None
            root.next = rh
            rh.prev = root
            return root, rt
