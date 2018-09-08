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

        if not matrix or not matrix[0]:
            return 0
        elif len(matrix) == 1:
            return self.maxLineArea(matrix[0])
        elif len(matrix[0]) == 1:
            return self.maxLineArea([r[0] for r in matrix])
        else:
            row = len(matrix)
            col = len(matrix[0])

            dp = [[0] * (col + 1) for r in range(row + 1)]

            for r in range(1, row+1, 1):
                for c in range(1, col+1, 1):
                    dp[r][c] = dp[r][c-1] + dp[r-1][c] - dp[r-1][c-1] + (1 if matrix[r-1][c-1] == "1" else 0)


            max_area = 0
            for r1 in range(1, row+1, 1):
                for c1 in range(1, col+1, 1):
                        for r2 in range(r1, row+1, 1):
                            for c2 in range(c1, col+1, 1):
                                if r1 == r2 and c1 == c2:
                                    area = (1 if matrix[r1-1][c1-1] == "1" else 0)
                                else:
                                    area = dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1]
                                if area == (c2-c1+1)*(r2-r1+1) and max_area < area:
                                    max_area = area

            return max_area


    def maxLineArea(self, list):
        max_area = 0
        area = 0
        for i in list:
            if i == "0":
                if max_area < area:
                    max_area = area
                area = 0
            else:
                area += 1
        if max_area < area:
            max_area = area
        return max_area

s = Solution()
print(s.maximalRectangle([["1","0","1","0","0","1","1"]]))
print(s.maximalRectangle([["1"], ["1"], ["0"], ["1"]]))
print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(s.maximalRectangle([["1","1"]]))
print(s.maximalRectangle([["1","1"],["1","1"]]))