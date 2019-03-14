# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class UnionFindSolution:
    def numComponents(self, head, G):
        """
        We are given head, the head node of a linked list containing unique integer values.
        We are also given the list G, a subset of the values in the linked list.
        Return the number of connected components in G,
        where two values are connected if they appear consecutively in the linked list.

        Example 1:
        Input:
        head: 0->1->2->3
        G = [0, 1, 3]
        Output: 2
        Explanation:
        0 and 1 are connected, so [0, 1] and [3] are the two connected components.
        Example 2:

        Input:
        head: 0->1->2->3->4
        G = [0, 3, 1, 4]
        Output: 2
        Explanation:
        0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
        Note:

        If N is the length of the linked list given by head, 1 <= N <= 10000.
        The value of each node in the linked list will be in the range [0, N - 1].
        1 <= G.length <= 10000.
        G is a subset of all values in the linked list.

        :type head: ListNode
        :type G: List[int]
        :rtype: int

        Union Find over edges whose nodes are in G.

        """
        if not head or not G:
            return 0

        parents = dict()
        sizes = dict()
        for d in G:
            parents[d] = d
            sizes[d] = 1

        while head.next:
            s, d = head.val, head.next.val
            if s in parents.keys() and d in parents.keys():
                self.union(parents, sizes, s, d)
            head = head.next

        components = set()
        for d in parents.keys():
            pd = self.find(parents, d)
            components.add(pd)
        return len(components)

    def union(self, parents, sizes, a, b):
        pa = self.find(parents, a)
        pb = self.find(parents, b)

        if pa == pb:
            return
        if sizes[pa] > sizes[pb]:
            pa, pb = pb, pa
        parents[pa] = pb
        sizes[pb] += sizes[pa]
        return

    def find(self, parents, a):
        while parents[a] != a:
            parents[parents[a]] = parents[a]
            a = parents[a]
        return a
