class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        perimeter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] <= 0:
                    continue
                else:
                    perimeter += self.dfs(grid, r, c)
        return perimeter

    def updatePerimeter(self, grid, r, c):
        rn = len(grid)
        cn = len(grid[0])
        p = 0
        if r == 0 or grid[r-1][c] == 0:
            p += 1
        if c == 0 or grid[r][c-1] == 0:
            p += 1
        if r == rn-1 or grid[r+1][c] == 0:
            p += 1
        if c == cn-1 or grid[r][c+1] == 0:
            p += 1
        return p

    def dfs(self, grid, r, c):
        rn = len(grid)
        cn = len(grid[0])
        p = self.updatePerimeter(grid, r, c)
        grid[r][c] = -1
        if r > 0 and grid[r-1][c] == 1:
            p += self.dfs(grid, r-1, c)
        if r < rn - 1 and grid[r+1][c] == 1:
            p += self.dfs(grid, r+1, c)
        if c > 0 and grid[r][c-1] == 1:
            p += self.dfs(grid, r, c-1)
        if c < cn - 1 and grid[r][c+1] == 1:
            p += self.dfs(grid, r, c+1)
        return p

def main():
    s = Solution()
    print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))

if __name__ == "__main__":
    main()