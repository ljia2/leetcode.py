# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        Sort a linked list in O(n log n) time using constant space complexity.

        Example 1:

        Input: 4->2->1->3
        Output: 1->2->3->4
        Example 2:

        Input: -1->5->3->4->0
        Output: -1->0->3->4->5

        :type head: ListNode
        :rtype: ListNode

        merge sort in O(nlogn)
        1) split linked list into two halves.
        2) sort each halves
        3) merge to sorted linked list.

        """
        if not head or not head.next:
            return head

        # split head into two halves.
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        h1 = head
        h2 = slow
        prev.next = None

        sl1 = self.sortList(h1)
        sl2 = self.sortList(h2)

        return self.merge(sl1, sl2)

    def merge(self, h1, h2):
        # generate a linked list use head pointing to the first node and curr pointing the last node.
        head = curr = None
        while h1 and h2:
            if h1.val < h2.val:
                if curr:
                    curr.next = h1
                    curr = curr.next
                else:
                    head = curr = h1

                h1 = h1.next
            else:
                if curr:
                    curr.next = h2
                    curr = curr.next
                else:
                    head = curr = h2
                h2 = h2.next

        if h1:
            curr.next = h1
        if h2:
            curr.next = h2

        return head

# [4, 1, 2, 3]
s = Solution()
head = ListNode(4)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
print(s.sortList(head))
