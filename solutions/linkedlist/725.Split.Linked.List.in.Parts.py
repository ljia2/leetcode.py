# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive
        linked list "parts".

        The length of each part should be as equal as possible: no two parts should have a size differing by more than 1.
        This may lead to some parts being null.

        The parts should be in order of occurrence in the input list, and parts occurring earlier
        should always have a size greater than or equal parts occurring later.

        Return a List of ListNode's representing the linked list parts that are formed.

        Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
        Example 1:

        Input:  root = [1, 2, 3], k = 5 Output: [[1],[2],[3],[],[]]
        Explanation: The input and each element of the output are ListNodes, not arrays.
        For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
        The first element output[0] has output[0].val = 1, output[0].next = null. The last element output[4] is null,
        but it's string representation as a ListNode is [].

        Example 2:

        Input:
        root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
        Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
        Explanation:
        The input has been split into consecutive parts with size difference at most 1,
        and earlier parts are a larger size than the later parts.

        Note:

        The length of root will be in the range [0, 1000].
        Each value of a node in the input will be an integer in the range [0, 999].
        k will be an integer in the range [1, 50]
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        if not root:
            return [None] * k

        l = 1
        runner = root
        while runner.next:
            runner = runner.next
            l += 1

        div = l // k
        mod = l % k

        ans = []
        runner = root
        local_l = 1
        while runner.next:
            if len(ans) < mod:
                if local_l == div + 1:
                    tmp = runner.next
                    runner.next = None
                    runner = tmp

                    ans.append(root)
                    root = runner
                    local_l = 1
                else:
                    runner = runner.next
                    local_l += 1
            else:
                if local_l == div:
                    tmp = runner.next
                    runner.next = None
                    runner = tmp

                    ans.append(root)
                    root = runner
                    local_l = 1
                else:
                    runner = runner.next
                    local_l += 1
        # add the last one
        ans.append(root)

        while len(ans) < k:
            ans.append(None)
        return ans


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
s = Solution()
print(s.splitListToParts(root, 2))
