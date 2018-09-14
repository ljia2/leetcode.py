# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import utils.ListNode as l

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        tail = head
        # use head and tail to define sorted list
        # insert node next to tail into the list between head and tail
        while tail.next is not None:
            head, tail = self.insertList(head, tail)
        return head

    def insertList(self, head, tail):
        # use p to iterate the sorted list between head and tail
        p = head
        node = tail.next

        if node.val < p.val:
            # put insert on the top of list; set node the new head
            tail.next = node.next
            node.next = head
            return node, tail
        else:
            while p != tail:
                if p.val <= node.val < p.next.val:
                    # put insert between p and p.next
                    tail.next = node.next
                    node.next = p.next
                    p.next = node
                    return head, tail
                else:
                    p = p.next

            # node should be its original place; set node as the new tail
            return head, node

def main():
    s = Solution()
    # [-1,5,3,4,0]
    input = l.ListNode(-1)
    input.next = l.ListNode(5)
    input.next.next = l.ListNode(3)
    input.next.next.next = l.ListNode(4)
    input.next.next.next.next = l.ListNode(0)
    print(s.insertionSortList(input))

    input1 = l.ListNode(4)
    input1.next = l.ListNode(0)
    input1.next.next = l.ListNode(1)
    input1.next.next.next = l.ListNode(3)
    print(s.insertionSortList(input1))



if __name__ == "__main__":
    main()