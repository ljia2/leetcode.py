# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def plusOne(self, head):
        """
        Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

        You may assume the integer do not contain any leading zero, except the number 0 itself.

        The digits are stored such that the most significant digit is at the head of the list.

        Example :

        Input: [1,2,3]
        Output: [1,2,4]

        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        node2parent = dict()
        parent = None
        while head:
            node2parent[head] = parent
            parent = head
            head = head.next

        # head is None ad parent pointing to the last node
        # reassign head and parent
        head = parent
        parent = node2parent[head]
        # add 1
        carry = 1
        while head:
            if head.val + carry < 10:
                head.val += carry
                carry = 0
                parent = head
                head = node2parent[head]

            else:
                head.val = (head.val + carry) % 10
                carry = 1
                parent = head
                head = node2parent[head]

        if carry == 0:
            return parent
        else:
            head = ListNode(carry)
            head.next = parent
            return head


