# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class IterativeSolution(object):
    def reverseBetween(self, head, m, n):
        """
        Reverse a linked list from position m to n. Do it in one-pass.

        Note: 1 ≤ m ≤ n ≤ length of list.

        Example:

        Input: 1->2->3->4->5->NULL, m = 2, n = 4
        Output: 1->4->3->2->5->NULL

        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        if m == n:
            return head

        if m > n:
            raise Exception("Invalid Input")

        mprev = mnode = None
        prev = None
        runner = head
        pos = 1
        while runner:
            if pos < m:
                if pos == m - 1:
                     mprev = runner
                runner = runner.next
            elif m <= pos <= n:
                if not prev:
                    # mark the mth node.
                    mnode = runner
                    # keep moving
                    prev, runner = runner, runner.next
                else:
                    # store the succ node
                    tmp = runner.next
                    # point runner's next to prev
                    runner.next = prev
                    # keep moving
                    prev, runner = runner, tmp
                if pos == n:
                    break
            pos += 1

        mnode.next = runner
        if mprev:
            mprev.next = prev

        return head if mprev else prev


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

s = IterativeSolution()
print(s.reverseBetween(l, 3, 4))



