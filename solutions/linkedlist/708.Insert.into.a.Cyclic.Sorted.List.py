# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head, insertVal):
        """
        Given a node from a cyclic linked list which is sorted in ascending order,
        write a function to insert a value into the list such that it remains a cyclic sorted list.
        The given node can be a reference to any single node in the list,
        and may not be necessarily the smallest value in the cyclic list.

        If there are multiple suitable places for insertion, you may choose any place to insert the new value.
        After the insertion, the cyclic list should remain sorted.

        If the list is empty (i.e., given node is null),
        you should create a new single cyclic list and return the reference to that single node.
        Otherwise, you should return the original given node.

        The following example may help you understand the problem better:

        In the figure above, there is a cyclic sorted list of three elements.
        You are given a reference to the node with value 3, and we need to insert 2 into the list.

        The new node should insert between node 1 and node 3. After the insertion, the list should look like this,
        and we should still return node 3.


        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        # If the list is empty (i.e., given node is null),
        # you should create a new single cyclic list
        # return the reference to that single node.
        if not head:
            node = Node(insertVal, head)
            node.next = node
            return node

        if head.next == head:
            node = Node(insertVal, head)
            head.next = node
            return head

        prev = head
        succ = head.next
        tail = None

        # iterate over the circle link list.
        while True:
            # find the insert place for insertVal
            if prev.val <= insertVal <= succ.val:
                node = Node(insertVal, succ)
                prev.next = node
                return head

            # update the small and big node in the circle
            if not tail:
                tail = prev
            # have to use >= to avoid there are multiple nodes with max values.
            elif prev.val >= tail.val:
                tail = prev

            prev = succ
            succ = succ.next

            # exit when revisit head
            if prev == head:
                break

        # must be either smallest or biggest
        # or all nodes have the same values and insert before head.
        node = Node(insertVal, tail.next)
        tail.next = node
        return head


n1 = Node(1, None)
n2 = Node(2, None)
n3 = Node(3, None)
n1.next = n2
n2.next = n3
n3.next = n1

s = Solution()
print(s.insert(n1, 4))




