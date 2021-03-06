#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        Sort a linked list using insertion sort.


        A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
        With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list


        Algorithm of Insertion Sort:

        Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
        At each iteration, insertion sort removes one element from the input data,
        finds the location it belongs within the sorted list, and inserts it there.
        It repeats until no input elements remain.

        Example 1:

        Input: 4->2->1->3
        Output: 1->2->3->4
        Example 2:

        Input: -1->5->3->4->0
        Output: -1->0->3->4->5
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        tail = head
        # use head and tail to define sorted list
        # insert node next to tail into the list between head and tail
        while tail.next:
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
    input = ListNode(-1)
    input.next = ListNode(5)
    input.next.next = ListNode(3)
    input.next.next.next = ListNode(4)
    input.next.next.next.next = ListNode(0)
    print(s.insertionSortList(input))

    input1 = ListNode(4)
    input1.next = ListNode(0)
    input1.next.next = ListNode(1)
    input1.next.next.next = ListNode(3)
    print(s.insertionSortList(input1))



if __name__ == "__main__":
    main()