import math

class Solution:
    def largestComponentSize(self, A):
        """
        Given a non-empty array of unique positive integers A, consider the following graph:

        There are A.length nodes, labelled A[0] to A[A.length - 1];
        There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
        Return the size of the largest connected component in the graph.

        Example 1:

        Input: [4,6,15,35]
        Output: 4

        Example 2:
        Input: [20,50,9,63]
        Output: 2

        Example 3:
        Input: [2,3,6,7,4,12,21,39]
        Output: 8

        Note:
        1 <= A.length <= 20000
        1 <= A[i] <= 100000

        :type A: List[int]
        :rtype: int

        A.length <= 20000 hints O(n) or O(nlogn)

        Union all numbers with their factors. given a number W, there are at most sqrt(W) factors.

        Time: O(n*sqrt(W))

        """
        if not A:
            return 0
        parents = [i for i in range(max(A)+1)]
        sizes = [1 for i in range(max(A) + 1)]
        for a in A:
            for k in range(2, int(math.sqrt(a))+1):
                if a % k == 0:
                    self.union(parents, sizes, a, k)
                    self.union(parents, sizes, a, a // k)

        components = dict()
        for a in A:
            pa = self.find(parents, a)
            components[pa] = components.get(pa, 0) + 1

        return max(components.values())

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
        while a != parents[a]:
            parents[a] = parents[parents[a]]
            a = parents[a]
        return a

s = Solution()
print(s.largestComponentSize([1, 2, 3, 4, 5, 6, 7, 8, 9]))
