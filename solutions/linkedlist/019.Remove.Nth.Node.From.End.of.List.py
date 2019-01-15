# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        Given a linked list, remove the n-th node from the end of list and return its head.

        Example:

        Given linked list: 1->2->3->4->5, and n = 2.

        After removing the second node from the end, the linked list becomes 1->2->3->5.
        Note:Given n will always be valid.
        Follow up: Could you do this in one pass?

        :type head: ListNode
        :type n: int
        :rtype: ListNode

        two pointer: first and second. After first moves nsteps, then second and first move together
        when first reaches the end, second points to the last n + 1 node and then remove the last n node.

        """
        if not head or n <= 0:
            return head

        step = 0
        first = second = head
        while first.next:
            first = first.next
            if step >= n:
                second = second.next
            step += 1

        # for example remove the 6th node from the end for a linked list of 5 node only.
        if step + 1 < n:
            return head
        elif step + 1 == n:
            return head.next
        else:
            second.next = second.next.next
            return head

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

#print(s.removeNthFromEnd(head, 6))
print(s.removeNthFromEnd(head, 2))