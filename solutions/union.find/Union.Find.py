"""
It is normally used to find the connected components in the graph or detect circle in the graph.
"""
class UnionFindSet:
    def __init__(self, n):
        # initialization: each node is their parent itself.
        self._parents = [i for i in range(n + 1)]
        # all have size of 1
        self._ranks = [1 for _ in range(n + 1)]

    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        # there is circle
        if pu == pv:
            return False

        # merge small into big.
        if self._ranks[pu] > self._ranks[pv]:
            pu, pv = pv, pu

        self._parents[pu] = pv
        self._size[pv] += self._size[pu]

        return True