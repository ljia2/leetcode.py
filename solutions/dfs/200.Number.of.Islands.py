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

        Depth First Search
        Flip current lands in grid to water to prevent their contributions to future island counting
        Then DFS Top, Down, L, R.
        """
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return

        if grid[r][c] == "0":
            return

        # mark (r,c) as visited
        grid[r][c] = "0"

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            self.dfs(grid, nr, nc)
        return

s = DFSSolution()
print(s.numIslands([['0', '1', '1', '0'], ['0', '0', '1', '0'], ['1', '0', '1', '0'], ['0', '1', '1', '0']]))
print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
print(s.numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))


#### Follow up: what if to find the number of lakes.
#### Similar idea but when search around the bound, the number of lakes - 1.

class VarationSolution:
    def numLakes(self, grid):

        if not grid or not grid[0]:
            return 0
        ans = 0
        rnum, cnum = len(grid), len(grid[0])
        for r in range(rnum):
            for c in range(cnum):
                if grid[r][c] == '1':
                    continue

                if self.dfs(grid, r, c):
                    ans += 1
        return ans

    def dfs(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return False

        if grid[r][c] == "1":
            return True

        ans = True
        # mark it as visited
        grid[r][c] = "1"
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            ans = ans and self.dfs(grid, nr, nc)
        return ans

s = VarationSolution()
print(s.numLakes([['0', '0', '1', '0'], ['0', '1', '0', '1'], ['0', '1', '0', '1'], ['0', '0', '1', '0']]))
print(s.numLakes([['0', '0', '1', '0'], ['0', '1', '0', '1'], ['0', '1', '0', '1'], ['0', '0', '0', '1']]))