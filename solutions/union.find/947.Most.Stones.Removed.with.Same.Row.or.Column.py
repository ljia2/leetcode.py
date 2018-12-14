class Solution:
    def removeStones(self, stones):
        """
        On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

        Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

        What is the largest possible number of moves we can make?

        Example 1:

        Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
        Output: 5
        Example 2:

        Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
        Output: 3
        Example 3:

        Input: stones = [[0,0]]
        Output: 0

        Note:

        1 <= stones.length <= 1000
        0 <= stones[i][j] < 10000

        :type stones: List[List[int]]
        :rtype: int

        for each stone, it has a virual edge with another store sharing the same column/row
        """

        if not stones or len(stones) == 1:
            return 0

        parents = [i for i in range(len(stones))]
        sizes = [1 for i in range(len(stones))]

        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union(parents, sizes, i, j)

        moves = 0
        visited = set()
        for i in range(len(stones)):
            pi = self.find(parents, i)
            if pi not in visited:
                moves += sizes[pi] - 1
                visited.add(pi)
        return moves

    def union(self, parents, sizes, i, j):
        pi = self.find(parents, i)
        pj = self.find(parents, j)
        if pi == pj:
            return
        if sizes[pi] > sizes[pj]:
            pi, pj = pj, pi
        parents[pi] = pj
        sizes[pj] += sizes[pi]
        return

    def find(self, parents, i):
        while i != parents[i]:
            parents[i] = parents[parents[i]]
            i = parents[i]
        return i

s = Solution()
print(s.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))