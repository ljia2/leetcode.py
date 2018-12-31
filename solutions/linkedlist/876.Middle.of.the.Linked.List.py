# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        """
        Given a non-empty, singly linked list with head node head, return a middle node of linked list.

        If there are two middle nodes, return the second middle node.



        Example 1:

        Input: [1,2,3,4,5]
        Output: Node 3 from this list (Serialization: [3,4,5])
        The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
        Note that we returned a ListNode object ans, such that:
        ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
        Example 2:

        Input: [1,2,3,4,5,6]
        Output: Node 4 from this list (Serialization: [4,5,6])
        Since the list has two middle nodes with values 3 and 4, we return the second one.


        Note:

        The number of nodes in the given list will be between 1 and 100.

        :type head: ListNode
        :rtype: ListNode
        """

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

s = Solution()
head = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
print(s.middleNode(head).val)