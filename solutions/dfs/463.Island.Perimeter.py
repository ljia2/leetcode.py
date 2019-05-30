class Solution:
    def islandPerimeter(self, grid):
        """
        You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

        Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
        and there is exactly one island (i.e., one or more connected land cells).

        The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
        One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
        Determine the perimeter of the island.

        Example:

        Input:
        [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]

        Output: 16

        Explanation: The perimeter is the 16 yellow stripes in the image below:


        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        ans = [0]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] <= 0:
                    continue
                self.dfs(grid, r, c, ans)
        return ans[0]

    def dfs(self, grid, r, c, ans):
        # whenever out of box or meet water, Perimeter += 1
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
            ans[0] += 1
            return
        # if the grid is visited already.
        if grid[r][c] != 1:
            return

        # encounter a land at (r, c); mark (r,c) as visited by -1
        # (can not by 0 to avoid double counting perimeter)
        grid[r][c] = -1
        for nr, nc in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
            self.dfs(grid, nr, nc, ans)
        return

s = Solution()
print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))