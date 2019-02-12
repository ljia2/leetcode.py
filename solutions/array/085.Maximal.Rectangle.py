class Solution:
    def maximalRectangle(self, matrix):
        """
        Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

        Example:

        Input:
        [
          ["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]
        ]
        Output: 6

        :type matrix: List[List[str]]
        :rtype: int

        dp[i][j] stores the number of 1s within the rectangle (0, 0) and (i-1, j-1)
        dp[0][0] == dp[0][j] == dp[i][0] == 0

        loop across (i, j) and (i', j') (i < i' and j < j') to fine a rectangle (i, j') and (i', j) are all 1's

        area = dp[i'][j'] - dp[i][j'] - dp[i'][j] + dp[i][j]

        if area == (j'-j + 1 ) * (i' - i + 1): then full of 1.

        keep track of biggest area
        """

        

s = Solution()
print(s.maximalRectangle([["1","0","1","0","0","1","1"]]))
print(s.maximalRectangle([["1"], ["1"], ["0"], ["1"]]))
print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(s.maximalRectangle([["1","1"]]))
print(s.maximalRectangle([["1","1"],["1","1"]]))