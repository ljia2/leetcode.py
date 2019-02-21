class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball,
        you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right).
        However, you can at most move N times.

        Find out the number of paths to move the ball out of grid boundary.
        The answer may be very large, return it after mod 10^9 + 7.



        Example 1:

        Input: m = 2, n = 2, N = 2, i = 0, j = 0
        Output: 6
        Explanation:

        Example 2:

        Input: m = 1, n = 3, N = 3, i = 0, j = 1
        Output: 12
        Explanation:



        Note:

        Once you move the ball out of boundary, you cannot move it back.
        The length and height of the grid is in range [1,50].
        N is in range [0,50].

        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int

        dp[N][m][n] denotes # times of the ball visiting the position (m, n) after N steps

        dp[N][m][n] = dp[N-1][m-1][n-1] or dp[N-1][m+1][n+1] or dp[N-1][m-1][n+1] or dp[N-1][m+1][n-1]

        """

        if m <= 0 or n <= 0 or N <= 0:
            return 0

        dp = [[[0 for _ in range(n+2)] for _ in range(m+2)] for _ in range(N+1)]
        dp[0][i+1][j+1] = 1

        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for k in range(1, N+1):
            # only consider if ball is still within grid
            for x in range(1, m+1):
                for y in range(1, n+1):
                    for (dx, dy) in dirs:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx > m + 1 or ny > n + 1:
                            continue
                        dp[k][nx][ny] += dp[k-1][x][y]

        ans = 0
        for k in range(1, N+1):
            for x in range(m+2):
                ans += dp[k][x][0] + dp[k][x][n+1]
            for y in range(n+2):
                ans += dp[k][0][y] + dp[k][m+1][y]
        return ans % (10**9 + 7)

s = Solution()
print(s.findPaths(1, 3, 3, 0, 1))