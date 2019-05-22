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

        # either reverse the input or use stack to store values, then add them up.

        """

        nl1 = self.reverse(l1)
        nl2 = self.reverse(l2)
        # Note that when answer is a linklist, we need to maintain a head and a tail.
        # we need to always keep the head of ans for reference and a pointer of the tail of ans for insertion.
        ans_head = ans_tail = None
        carry = 0
        while nl1 or nl2:
            v1 = nl1.val if nl1 else 0
            v2 = nl2.val if nl2 else 0
            numsum = v1 + v2 + carry
            if not ans_head:
                ans_head = ListNode(numsum % 10)
                ans_tail = ans_head
            else:
                ans_tail.next = ListNode(numsum % 10)
                ans_tail = ans_tail.next

            carry = numsum // 10

            nl1 = nl1.next
            nl2 = nl2.next

        # do not forget the ultimate carry !!!!
        if carry == 1:
            ans_tail.next = ListNode(1)

        rev_ans = self.reverse(ans_head)
        return rev_ans

    def reverse(self, head):
        prev = None
        succ = head
        while succ:
            tmp = succ.next
            succ.next = prev
            prev = succ
            succ = tmp
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

