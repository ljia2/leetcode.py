# class DPSolution: # Time Limit Exceeded
#     def numSquares(self, n):
#         """
#         Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
#         Example 1:
#
#         Input: n = 12
#         Output: 3
#         Explanation: 12 = 4 + 4 + 4.
#         Example 2:
#
#         Input: n = 13
#         Output: 2
#         Explanation: 13 = 4 + 9.
#
#         :type n: int
#         :rtype: int
#
#         dp stores the least number of perfect square numbers
#
#         dp[i] stores the least number of perfect square numbers summing to i
#
#         """
#         dp = [n] * (n + 1)
#         dp[0] = 0
#         for i in range(n+1):
#             if i*i <= n:
#                 dp[i*i] = 1
#
#         for i in range(n+1):
#             for j in range(1, int(i**0.5)+1, 1):
#                 dp[i] = min(dp[i], dp[i-j*j] + 1)
#         return dp[n]


class StaticDPSolution:
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

        """
        # base case: 0 has zero perfect square
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            min_val = n
            for j in range(1, int(i**0.5)+1):
                min_val = min(min_val, dp[i-j*j] + 1)
            dp[i] = min_val
        return dp[n]

s = StaticDPSolution()
print(s.numSquares(8328))