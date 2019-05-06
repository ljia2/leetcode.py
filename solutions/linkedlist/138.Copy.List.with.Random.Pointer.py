# Definition for singly-linked list with a random pointer.
class Node(object):
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

        T: O(n)
        S: O(n)

        """
        cur = head
        node_dict = dict()
        while cur:
            node_dict[cur] = Node(cur.label)
            cur = cur.next

        cur = head
        while cur:
            n = cur.next
            r = cur.random
            node_dict[cur].next = node_dict.get(n, None)
            node_dict[cur].random = node_dict.get(r, None)
            cur = cur.next
        return node_dict.get(head, None)



class SolutionII(object):
    def copyRandomList(self, head):
        """
        A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

        Return a deep copy of the list.

        :type head: RandomListNode
        :rtype: RandomListNode

        Follow up: can you proposed an O(1) space method.

        1) for each node, insert its copy after it but before its next
        2) iterate the original node to set up random.

        T: O(N)
        S: O(1)

        """
        if not head:
            return head
        # insert node copy immediately after the original node.
        runner = head
        while runner:
            nnode = Node(runner.next)
            runner.next, nnode.next = nnode, runner.next
            runner = nnode.next
        # copy over the random pointer if any
        runner = head
        while runner and runner.next:
            rnode = runner.random
            if rnode:
                runner.next.random = rnode.next
            runner = runner.next.next

        # separate original and copy linklist.
        duphead = head.next
        runner = head
        while runner and runner.next:
            tmp = runner.next
            runner.next = runner.next.next
            runner = tmp
        return duphead






