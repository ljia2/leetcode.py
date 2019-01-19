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
        lands = [0] * size
        parents = [i for i in range(size)]
        ranks = [1] * size
        ans = []
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        count = 0
        for p in positions:
            r, c = p
            i = r * n + c
            lands[i] = 1
            count += 1
            for dir in directions:
                rr = r + dir[0]
                cc = c + dir[1]
                ii = rr * n + cc
                # out of bound
                if rr < 0 or rr > m - 1 or cc < 0 or cc > n - 1 or lands[ii] == 0:
                    continue

                    # there is an edge between i and ni
                pi = self.find(parents, i)
                pii = self.find(parents, ii)

                if pi == pii:
                    continue

                # whenever there is a union of two components, the total nubmer of connected compontents minusing 1
                if pii != pi:
                    # union two islands by ranks, thus island number minus 1
                    if ranks[pi] > ranks[pii]:
                        pi, pii = pii, pi
                    parents[pi] = pii
                    ranks[pii] += ranks[pi]
                    count -= 1
            ans.append(count)
        return ans

    def find(self, parents, s):
        while s != parents[s]:
            parents[s] = parents[parents[s]]
            s = parents[s]
        return s

