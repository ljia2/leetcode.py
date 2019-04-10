class Solution:
    def minPathSum(self, grid):
        """
        Given a m x n grid filled with non-negative numbers,
        find a path from top left to bottom right which minimizes the sum of all numbers along its path.

        Note: You can only move either down or right at any point in time.

        Example:

        Input:
        [
          [1,3,1],
          [1,5,1],
          [4,2,1]
        ]
        Output: 7
        Explanation: Because the path 1→3→1→1→1 minimizes the sum.

        :type grid: List[List[int]]
        :rtype: int

        dp[i][j] denotes the min summed path from grid[0][0] to grid[i][j]

        dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j]

        """
        if not grid or len(grid[0]) == 0:
            return 0

        r = len(grid)
        c = len(grid[0])
        msum = [[0] * (c + 1) for _ in range(r + 1)]

        for i in range(1, r+1):
            for j in range(1, c+1):
                if i == 1 and j == 1:
                    msum[i][j] = grid[i-1][j-1]
                elif i == 1:
                    msum[i][j] = msum[i][j-1] + grid[i-1][j-1]
                elif j == 1:
                    msum[i][j] = msum[i-1][j] + grid[i-1][j-1]
                else:
                    msum[i][j] = min(msum[i][j-1] + grid[i-1][j-1], msum[i-1][j] + grid[i-1][j-1])
        return msum[r][c]


s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))