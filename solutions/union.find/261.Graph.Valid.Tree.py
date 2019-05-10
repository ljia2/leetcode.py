class UnionFindSolution:
    def validTree(self, n, edges):
        """
        Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
        write a function to check whether these edges make up a valid tree.

        Example 1:

        Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
        Output: true
        Example 2:

        Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
        Output: false

        Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected,
        [0,1] is the same as [1,0] and thus will not appear together in edges.

        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """

        if n == 1:
            return True
        if not edges:
            return False

        parents = [i for i in range(n)]
        ranks = [1] * n

        # for each edge, try to union s, d.
        # if s and d is already connected by sharing the parent.
        # then there is a circle.
        for e in edges:
            s, d = e
            ps = self.find(parents, s)
            pd = self.find(parents, d)

            if ps == pd:
                # there is an edge that forms a circle.
                return False

            if ranks[ps] > ranks[pd]:
                ps, pd = pd, ps
            parents[ps] = pd
            ranks[pd] += ranks[ps]

        # all nodes having a single parent, it must be a tree.
        ans = set()
        for i in range(len(parents)):
            ans.add(self.find(parents, parents[i]))
        return len(ans) == 1

    def find(self, parents, s):
        while s != parents[s]:
            parents[s] = parents[parents[s]]
            s = parents[s]
        return s
