class DFSSolution:
    def numIslands(self, grid):
        """

        Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        You may assume all four edges of the grid are all surrounded by water.

        Example 1:

        Input:
        11110
        11010
        11000
        00000

        Output: 1
        Example 2:

        Input:
        11000
        11000
        00100
        00011

        Output: 3

        :type grid: List[List[str]]
        :rtype: int
        Note:
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    result += 1
                    self.dfs(grid, r, c)
        return result

    def dfs(self, grid, r, c):
        """
        :param grid:
        :param r:
        :param c:
        :return:

        """
        if not self.inbound(grid, r, c):
            return
        elif grid[r][c] == '0':
            return
        else:
            # Depth First Search
            # Flip current lands in grid to water to prevent their contributions to future island counting
            # Then DFS Top, Down, L, R.

            # flip the land to water to mark the already visited
            grid[r][c] = '0'
            # dfs in four directions
            self.dfs(grid, r-1, c)
            self.dfs(grid, r+1, c)
            self.dfs(grid, r, c-1)
            self.dfs(grid, r, c+1)

    def inbound(self, grid, r, c):
        return -1 < r < len(grid) and -1 < c < len(grid[0])

s = DFSSolution()
print(s.numIslands([['0', '1', '1', '0'], ['0', '0', '1', '0'], ['1', '0', '1', '0'], ['0', '1', '1', '0']]))
print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
print(s.numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))
