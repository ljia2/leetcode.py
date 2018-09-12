import math


class Solution:
    def numSquares(self, n):
        """
        Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

        Example 1:

        Input: n = 12
        Output: 3
        Explanation: 12 = 4 + 4 + 4.
        Example 2:

        Input: n = 13
        Output: 2
        Explanation: 13 = 4 + 9.

        :type n: int
        :rtype: int

        dp stores the least number of perfect square numbers

        dp[i] stores the least number of perfect square numbers summing to i

        iterate j from 1 to sqrt(i):

        dp[i] = min{dp[i-j] + 1 | j is perfect sqaure less than i}

        TO MUCH REPEAT COMPUTATION!!!

        """

        if not n:
            return 0
        else:
            dp = [0] * (n + 1)
            for i in range(1, n+1, 1):
                j, min_res = 1, n
                while i - j * j >= 0:
                    min_res = min(min_res, dp[i-j * j] + 1)
                    j += 1
                dp[i] = min_res
            return dp[n]


class DPSolution:
    def numSquares(self, n):
        """
        Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

        Example 1:

        Input: n = 12
        Output: 3
        Explanation: 12 = 4 + 4 + 4.
        Example 2:

        Input: n = 13
        Output: 2
        Explanation: 13 = 4 + 9.

        :type n: int
        :rtype: int

        dp stores the least number of perfect square numbers

        dp[i] stores the least number of perfect square numbers summing to i

        """
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(n+1):
            if i*i <= n:
                dp[i] = 1

        for i in range(n+1):
            for j in range(1, i+1, 1):
                if i + j * j <= n:
                    dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
        return dp[n]



s = DPSolution()
print(s.numSquares(12))