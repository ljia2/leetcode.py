class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        else:
            row_num = len(grid)
            col_num = len(grid[0])
            row_kill = [0] * row_num # updated row count of elemies between walls if any
            col_kill = [0] * col_num # updated col count of elemies between walls if any
            max_kill = 0
            for r in range(row_num):
                for c in range(col_num):
                    # Count column-wise in the row r; We only count when either 1) first column
                    # or 2) last column in the same row is a Wall to avoid recount.
                    if c == 0 or grid[r][c-1] == "W":
                        row_kill[r] = 0
                        for k in range(c, col_num, 1):
                            if grid[r][k] == "E":
                                row_kill[r] += 1
                            elif grid[r][k] == "W":
                                break
                    # Count row-wise in the column c; We only count when either 1) first row
                    # or 2) last row in the same column is a Wall to avoid recount.
                    if r == 0 or grid[r-1][c] == "W":
                        col_kill[c] = 0
                        for k in range(r, row_num, 1):
                            if grid[k][c] == "E":
                                col_kill[c] += 1
                            elif grid[k][c] == "W":
                                break
                    if grid[r][c] == "0":
                        if max_kill < row_kill[r] + col_kill[c]:
                            max_kill = row_kill[r] + col_kill[c]
            return max_kill

s = Solution()
print(s.maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))

