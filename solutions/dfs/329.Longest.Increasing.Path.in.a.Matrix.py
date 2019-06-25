class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        Given an integer matrix, find the length of the longest increasing path.

        From each cell, you can either move to four directions: left, right, up or down.
        You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

        Example 1:

        Input: nums =
        [
          [9,9,4],
          [6,6,8],
          [2,1,1]
        ]
        Output: 4
        Explanation: The longest increasing path is [1, 2, 6, 9].

        Example 2:

        Input: nums =
        [
          [3,4,5],
          [3,2,6],
          [2,2,1]
        ]
        Output: 4

        Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

        :type matrix: List[List[int]]
        :rtype: int

        dfs + memorization

        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        # dp[i][j] stores the longest increasing path start (i, j)
        dp = [[0] * n for _ in range(m)]

        ans = 1
        for r in range(m):
            for c in range(n):
                l = self.dfs(matrix, r, c, m, n, dp)
                ans = max(l, ans)
        return ans

    # top down dfs with memorization!!!!
    def dfs(self, matrix, r, c, m, n, dp):
        if dp[r][c] != 0:
            return dp[r][c]

        maxl = 1
        for nr, nc in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
            if nr < 0 or nc < 0 or nr >= m or nc >= n or matrix[r][c] >= matrix[nr][nc]:
                continue
            l = 1 + self.dfs(matrix, nr, nc, m, n, dp)
            maxl = max(maxl, l)

        # record the memory of (r, c)
        dp[r][c] = maxl
        return maxl

s = Solution()
print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))