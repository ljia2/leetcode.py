class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

        The robot can only move either down or right at any point in time.
        The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

        Now consider if some obstacles are added to the grids. How many unique paths would there be?

        An obstacle and empty space is marked as 1 and 0 respectively in the grid.

        Note: m and n will be at most 100.

        Example 1:

        Input:
        [
          [0,0,0],
          [0,1,0],
          [0,0,0]
        ]
        Output: 2
        Explanation:
        There is one obstacle in the middle of the 3x3 grid above.
        There are two ways to reach the bottom-right corner:
        1. Right -> Right -> Down -> Down
        2. Down -> Down -> Right -> Right


        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0] == 1:
            return 0
        # base case 1
        dp[0][0] = 1
        # base case 2
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
        # base case 2
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0

        # transition
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) if obstacleGrid[i][j] == 0 else 0

        return dp[m-1][n-1]