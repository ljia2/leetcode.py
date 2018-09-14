from utils.ListNode import ListNode

from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists:
            if len(lists) == 1:
                return lists[0]
            elif len(lists) == 2:
                return self.merge2Lists(lists[0], lists[1])
            else:
                # cast to integer, discard decimal points.
                mid = int(len(lists) / 2)
                return self.merge2Lists(self.mergeKLists(lists[0:mid]), self.mergeKLists(lists[mid:len(lists)]))
        else:
            return None

    def merge2Lists(self, slist, elist):
        s_curr = slist
        e_curr = elist
        r_head = ListNode(None)
        r_curr = r_head
        while s_curr is not None and e_curr is not None:
            if s_curr.val > e_curr.val:
                if r_curr is None: # result is Empty
                    r_curr = ListNode(e_curr.val)
                else:
                    r_curr.next = ListNode(e_curr.val)
                    r_curr = r_curr.next
                e_curr = e_curr.next
            else:
                if r_curr is None: # result is Empty
                    r_curr = ListNode(s_curr.val)
                else:
                    r_curr.next = ListNode(s_curr.val)
                    r_curr = r_curr.next
                s_curr = s_curr.next

        if e_curr is not None:
            while e_curr is not None:
                if r_curr is None:
                    r_curr = ListNode(e_curr.val)
                    r_head = r_curr
                else:
                    r_curr.next = ListNode(e_curr.val)
                    r_curr = r_curr.next
                e_curr = e_curr.next
        elif s_curr is not None:
            while s_curr is not None:
                if r_curr is None:
                    r_curr = ListNode(s_curr.val)
                    r_head = r_curr
                else:
                    r_curr.next = ListNode(s_curr.val)
                    r_curr = r_curr.next
                s_curr = s_curr.next

        return r_head.next


class Solution2:
    #
    def mergeKLists(self, lists):
        head = ListNode(None)
        curr = head
        q = PriorityQueue()
        for node in lists:
            if node: # node is not None
                # tuple of (priority, node); need to override __lt__ in ListNode
                # to use priorityQueue, when first priority (ListNode.val is tied)
                q.put((node.val, node))

        while q.qsize() > 0:
            curr.next = q.get()[1] # use the second item from tuple
            print(f"""queue next = {curr.next.val}""")
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))
        return head.next


def main():

    input1 = ListNode(1)
    input1.next = ListNode(4)
    input1.next.next = ListNode(5)

    input2 = ListNode(1)
    input2.next = ListNode(3)
    input2.next.next = ListNode(4)

    input3 = ListNode(2)
    input3.next = ListNode(6)

    s = Solution()
    results = s.mergeKLists([input1, input2, input3])
    print(results)

    s2 = Solution2()
    results = s2.mergeKLists([input1,input2,input3])
    print(results)


if __name__ == '__main__':
    main()