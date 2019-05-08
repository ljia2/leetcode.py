class Solution(object):
    def numDistinctIslands(self, grid):
        """
        Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

        Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

        Example 1:
        11000
        11000
        00011
        00011
        Given the above grid map, return 1.
        Example 2:
        11011
        10000
        00001
        11011
        Given the above grid map, return 3.

        Notice that:
        11
        1
        and
         1
        11
        are considered different island shapes, because we do not consider reflection / rotation.
        Note: The length of each dimension in the given grid does not exceed 50.

        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid or not grid[0]:
            return 0

        rnum, cnum = len(grid), len(grid[0])
        cnt = 0
        shapes = set()
        for r in range(rnum):
            for c in range(cnum):
                if grid[r][c] == 1:
                    shape = []
                    self.dfs(grid, r, c, r, c, shape)
                    shapeStr = ",".join(shape)
                    if shapeStr not in shapes:
                        cnt += 1
                        shapes.add(shapeStr)
        return cnt

    def dfs(self, grid, sr, sc, r, c, shape):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
            return

        # we use the string of the sequence of deltas to represent the shapes of islands
        shape.append(str(sr-r)+"|"+str(sc-c))

        grid[r][c] = 0
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            self.dfs(grid, sr, sc, nr, nc, shape)
        return

s = Solution()
print(s.numDistinctIslands([[1,1,0,1,1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]))
print(s.numDistinctIslands([[1,1,0],[0,1,1],[0,0,0],[1,1,1],[0,1,0]]))