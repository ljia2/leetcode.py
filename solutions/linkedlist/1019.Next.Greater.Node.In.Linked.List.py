# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def nextLargerNodes(self, head):
        """
        We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

        Each node may have a next larger value:
        for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val,
        and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

        Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

        Note that in the example inputs (not outputs) below, arrays such as [2,1,5]
        represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

        Example 1:

        Input: [2,1,5]
        Output: [5,5,0]
        Example 2:

        Input: [2,7,4,3,5]
        Output: [7,0,5,5,0]
        Example 3:

        Input: [1,7,5,1,9,2,5,1]
        Output: [7,9,9,9,0,5,0,0]

        Note:

        1 <= node.val <= 10^9 for each node in the linked list.
        The given list has length in the range [0, 10000].

        :type head: ListNode
        :rtype: List[int]

        from the tail to the head of the linked list, given a node_i
           keep track of num to smallest position dictionary
           keep track of unique numbers in monotone stack

           binary search of monotonic stack over node_i.val.

           update the position dictionary.
        """

        if not head:
            return []

        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        l = len(vals)
        ms = []
        ans = []
        for i in range(l-1, -1, -1):
            ans.append(self.popMonotoneStack(ms, vals[i]))
        return ans[::-1]

    def popMonotoneStack(self, ms, val):
        ans = 0
        while ms:
            if ms[-1] <= val:
                ms.pop()
            else:
                ans = ms[-1]
                break
        ms.append(val)
        return ans


s = Solution()
#[2,7,4,3,5]
head = ListNode(2)
head.next = ListNode(7)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)
print(s.nextLargerNodes(head))
