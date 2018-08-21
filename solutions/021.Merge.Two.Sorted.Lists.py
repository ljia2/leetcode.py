# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            head = None
            tail = head
            while l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    if head:
                        # head is not empty, expand tail
                        tail.next = l1
                        tail = l1
                        l1 = l1.next
                    else:
                        head = l1
                        tail = head
                        l1 = l1.next
                else:
                    if head:
                        tail.next = l2
                        tail = l2
                        l2 = l2.next
                    else:
                        head = l2
                        tail = head
                        l2 = l2.next

            if l1:
                while l1:
                    tail.next = l1
                    tail = l1
                    l1 = l1.next
            elif l2:
                while l2:
                    tail.next = l2
                    tail = l2
                    l2 = l2.next

            return head

