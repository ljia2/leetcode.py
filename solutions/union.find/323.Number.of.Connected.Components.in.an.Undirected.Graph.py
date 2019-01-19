class Solution:
    def countComponents(self, n, edges):
        """
        Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
        write a function to find the number of connected components in an undirected graph.

        Example 1:

        Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

             0          3
             |          |
             1 --- 2    4

        Output: 2

        Example 2:

        Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

             0           4
             |           |
             1 --- 2 --- 3

        Output:  1

        Note:
        You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
        [0, 1] is the same as [1, 0] and thus will not appear together in edges

        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        parents = [i for i in range(n)]
        ranks = [1] * n

        for e in edges:
            s, d = e
            ps = self.find(parents, s)
            pd = self.find(parents, d)

            if ps == pd:
                continue

            if ranks[ps] > ranks[pd]:
                ps, pd = pd, ps
            parents[ps] = pd
            ranks[pd] += ranks[ps]

        ans = set()
        for i in range(len(parents)):
            ans.add(self.find(parents, parents[i]))
        return len(ans)

    def find(self, parents, s):
        while s != parents[s]:
            parents[s] = parents[parents[s]]
            s = parents[s]
        return s