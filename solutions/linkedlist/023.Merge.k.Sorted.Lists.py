# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, node):
        self.val < node.val


# class Solution:
#     def mergeKLists(self, lists):
#         """
#         Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
#         Example:
#
#         Input:
#         [
#           1->4->5,
#           1->3->4,
#           2->6
#         ]
#         Output: 1->1->2->3->4->4->5->6
#
#         :type lists: List[ListNode]
#         :rtype: ListNode
#
#         Divide and Conquer
#
#         """
#         if lists:
#             if len(lists) == 1:
#                 return lists[0]
#             elif len(lists) == 2:
#                 return self.merge2Lists(lists[0], lists[1])
#             else:
#                 # cast to integer, discard decimal points.
#                 mid = int(len(lists) / 2)
#                 return self.merge2Lists(self.mergeKLists(lists[0:mid]), self.mergeKLists(lists[mid:len(lists)]))
#         else:
#             return None
#
#     def merge2Lists(self, slist, elist):
#         s_curr = slist
#         e_curr = elist
#         r_head = ListNode(None)
#         r_curr = r_head
#         while s_curr is not None and e_curr is not None:
#             if s_curr.val > e_curr.val:
#                 if r_curr is None: # result is Empty
#                     r_curr = ListNode(e_curr.val)
#                 else:
#                     r_curr.next = ListNode(e_curr.val)
#                     r_curr = r_curr.next
#                 e_curr = e_curr.next
#             else:
#                 if r_curr is None: # result is Empty
#                     r_curr = ListNode(s_curr.val)
#                 else:
#                     r_curr.next = ListNode(s_curr.val)
#                     r_curr = r_curr.next
#                 s_curr = s_curr.next
#
#         if e_curr is not None:
#             while e_curr is not None:
#                 if r_curr is None:
#                     r_curr = ListNode(e_curr.val)
#                     r_head = r_curr
#                 else:
#                     r_curr.next = ListNode(e_curr.val)
#                     r_curr = r_curr.next
#                 e_curr = e_curr.next
#         elif s_curr is not None:
#             while s_curr is not None:
#                 if r_curr is None:
#                     r_curr = ListNode(s_curr.val)
#                     r_head = r_curr
#                 else:
#                     r_curr.next = ListNode(s_curr.val)
#                     r_curr = r_curr.next
#                 s_curr = s_curr.next
#
#         return r_head.next

from heapq import heappush, heappop

class Solution2:
    def mergeKLists(self, lists):
        """
        Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

        Example:

        Input:
        [
          1->4->5,
          1->3->4,
          2->6
        ]
        Output: 1->1->2->3->4->4->5->6

        :type lists: List[ListNode]
        :rtype: ListNode

        use priority queue

        """
        # curr points the node to insert its next value.
        head = None
        curr = head
        pq = []
        for i in range(len(lists)):
            node_curr = lists[i]
            # node is not None
            if node_curr:
                # tuple of (priority, node index);
                heappush(pq, (node_curr.val, i))

        while pq:
            # pop index of least value node from pq
            _, min_index = heappop(pq)
            if not head:
                head = lists[min_index]
                curr = head
            else:
                # update curr.next points to that least-valued node
                curr.next = lists[min_index]
                curr = curr.next

            if lists[min_index].next:
                heappush(pq, (lists[min_index].next.val, min_index))
                # move the point of min_index forward
                lists[min_index] = lists[min_index].next
        return head


input1 = ListNode(1)
input1.next = ListNode(4)
input1.next.next = ListNode(5)

input2 = ListNode(1)
input2.next = ListNode(3)
input2.next.next = ListNode(4)

input3 = ListNode(2)
input3.next = ListNode(6)

s = Solution2()
results = s.mergeKLists([input1, input2, input3])
print(results)
