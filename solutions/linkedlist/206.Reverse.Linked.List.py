# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class RecursiveSolution(object):
    def reverseList(self, head):
        """
        Reverse a singly linked list.

        Example:

        Input: 1->2->3->4->5->NULL
        Output: 5->4->3->2->1->NULL
        Follow up:

        A linked list can be reversed either iteratively or recursively. Could you implement both?


        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head
        nhead, _ = self.reverseTail(head)
        return nhead

    def reverseTail(self, head):
        if not head:
            return None, None

        nhead, ntail = self.reverseList(head.next)

        if ntail:
            ntail.next = head
            head.next = None
            return nhead, head
        else:
            return head, head


# class IterativeSolution(object):
#     def reverseList(self, head):
#         """
#         Reverse a singly linked list.
#
#         Example:
#
#         Input: 1->2->3->4->5->NULL
#         Output: 5->4->3->2->1->NULL
#         Follow up:
#
#         A linked list can be reversed either iteratively or recursively. Could you implement both?
#
#
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head or not head.next:
#             return head
#
#         stack = []
#         while head:
#             stack.append(head)
#             head = head.next
#
#         newhead = stack.pop()
#         newtail = newhead
#         while stack:
#             node = stack.pop()
#             newtail.next = node
#             node.next = None
#             newtail = node
#         return newhead


class IterativeSolution(object):
    def reverseList(self, head):
        """
        Reverse a singly linked list.

        Example:

        Input: 1->2->3->4->5->NULL
        Output: 5->4->3->2->1->NULL
        Follow up:

        A linked list can be reversed either iteratively or recursively. Could you implement both?


        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        succ = head

        while succ:
            tmp = succ.next
            succ.next = prev
            prev, succ = succ, tmp
        return prev




l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
s = IterativeSolution()
print(s.reverseList(l))