# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

        Return a deep copy of the list.

        :type head: RandomListNode
        :rtype: RandomListNode
        """

        cur = head
        node_dict = dict()
        while cur:
            node_dict[cur] = RandomListNode(cur.label)
            cur = cur.next

        cur = head
        while cur:
            n = cur.next
            r = cur.random
            node_dict[cur].next = node_dict.get(n, None)
            node_dict[cur].random = node_dict.get(r, None)
            cur = cur.next
        return node_dict.get(head, None)
