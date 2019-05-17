# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        Given a singly linked list L: L0→L1→…→Ln-1→Ln,
        reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

        You may not modify the values in the list's nodes, only nodes itself may be changed.

        Example 1:

        Given 1->2->3->4, reorder it to 1->4->2->3.
        Example 2:

        Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.


        divide, reverse and merge.

        """
        if not head or not head.next or not head.next.next:
            return head

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        runner1 = head # from head to slow

        # from slow.next to tail
        runner2 = self.reverse(slow.next)

        # slow become the last node, set its next to None
        slow.next = None

        # merge two linkedlists.
        nhead = tail = None
        while runner1 and runner2:
            if not nhead:
                nhead = runner1
            else:
                tail.next = runner1
            tmp = runner1.next
            runner1.next = runner2
            tail = runner2
            runner1 = tmp
            runner2 = runner2.next

        # there might be an element more in runner.
        if runner1:
            tail.next = runner1
        return nhead

    def reverse(self, head):
        prev = None
        runner = head
        while runner:
            tmp = runner.next
            runner.next = prev
            prev = runner
            runner = tmp
        return prev








