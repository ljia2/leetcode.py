class UnionFindSolution: # TLE
    def numIslands2(self, m, n, positions):
        """
        A 2d grid map of m rows and n columns is initially filled with water.
        We may perform an addLand operation which turns the water at position (row, col) into a land.
        Given a list of positions to operate, count the number of islands after each addLand operation.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        You may assume all four edges of the grid are all surrounded by water.

        Example:

        Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
        Output: [1,1,2,3]
        Explanation:

        Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

        0 0 0
        0 0 0
        0 0 0
        Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

        1 0 0
        0 0 0   Number of islands = 1
        0 0 0
        Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

        1 1 0
        0 0 0   Number of islands = 1
        0 0 0
        Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

        1 1 0
        0 0 1   Number of islands = 2
        0 0 0
        Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

        1 1 0
        0 0 1   Number of islands = 3
        0 1 0

        Follow up:

        Can you do it in time complexity O(k log mn), where k is the length of the positions?

        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """

        size = m * n
        # whether a cell is land
        lands = [[0] * n for _ in range(m)]
        # initialization
        # all cells are their own parents
        parents = [i for i in range(size)]
        # all cells have the same size of 1.
        sizes = [1] * size

        ans = []
        # tracking the count the connected components.
        count = 0
        for p in positions:
            r, c = p
            i = r * n + c
            lands[r][c] = 1
            # a new land
            count += 1
            # search four directions to ensure it is a new island
            for rr, cc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                ii = rr * n + cc

                # out of bound
                if rr < 0 or rr > m - 1 or cc < 0 or cc > n - 1 or lands[rr][cc] == 0:
                    continue

                # There is an new edge between ii (existing land) and i (new land).
                pi = self.find(parents, i)
                pii = self.find(parents, ii)
                # these two lands already sharing the same parent.
                if pi == pii:
                    continue

                # union two islands by ranks
                if sizes[pi] > sizes[pii]:
                    pi, pii = pii, pi
                parents[pi] = pii
                sizes[pii] += sizes[pi]

                # the new edge merges two components and the total number of connected components minus 1
                count -= 1

            ans.append(count)
        return ans

    def find(self, parents, s):
        while s != parents[s]:
            parents[s] = parents[parents[s]]
            s = parents[s]
        return s