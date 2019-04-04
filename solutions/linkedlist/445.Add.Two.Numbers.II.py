# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """

        You are given two non-empty linked lists representing two non-negative integers.
        The most significant digit comes first and each of their nodes contain a single digit.
        Add the two numbers and return it as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        Follow up:
        What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

        Example:

        Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 8 -> 0 -> 7

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        nl1 = self.reverse(l1)
        nl2 = self.reverse(l2)
        # Note that when answer is a linklist, we need to maintain a head and a tail.
        # we need to always keep the head of ans for reference and a pointer of the tail of ans for insertion.
        ans_head = ans_tail = None
        carry = 0
        while nl1 and nl2:
            numsum = nl1.val + nl2.val + carry
            if not ans_head:
                ans_head = ListNode(numsum % 10)
                ans_tail = ans_head
            else:
                ans_tail.next = ListNode(numsum % 10)
                ans_tail = ans_tail.next

            carry = numsum // 10

            nl1 = nl1.next
            nl2 = nl2.next

        while nl1:
            numsum = nl1.val + carry
            ans_tail.next = ListNode(numsum % 10)
            ans_tail = ans_tail.next
            carry = numsum // 10
            nl1 = nl1.next
        while nl2:
            numsum = nl2.val + carry
            ans_tail.next = ListNode(numsum % 10)
            ans_tail = ans_tail.next
            carry = numsum // 10
            nl2 = nl2.next
        # do not forget the ultimate carry !!!! 
        if carry == 1:
            ans_tail.next = ListNode(1)

        rev_ans = self.reverse(ans_head)
        return rev_ans

    def reverse(self, head):
        prev = head
        succ = head.next
        prev.next = None
        while succ:
            newsucc = succ.next
            succ.next = prev
            prev = succ
            succ = newsucc
        return prev


l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
print(s.addTwoNumbers(l1, l2))

