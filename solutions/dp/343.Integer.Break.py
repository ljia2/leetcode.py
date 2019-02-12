class Solution:
    def integerBreak(self, n):
        """
        Given a positive integer n, break it into the sum of at least two positive integers
        and maximize the product of those integers. Return the maximum product you can get.

        Example 1:

        Input: 2
        Output: 1
        Explanation: 2 = 1 + 1, 1 × 1 = 1.
        Example 2:

        Input: 10
        Output: 36
        Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

        :type n: int
        :rtype: int


        dp[i] denotes the largest product of i

        for two number, j * (i-j)
        for multiple number, j * dp[i-j]
        where 1 <= j < i

        dp[i] = max { j * dp[i-j], j * (i-j) | where 1 <= j < i}

        dp[0] = 1
        dp[1] = 1


        """
        dp = [1] * (n + 1)
        for i in range(1, n+1):
            max_prod = 1
            for j in range(1, i):
                # length 2 and any length
                mp = max(j * (i-j), j * dp[i-j])
                if max_prod < mp:
                    max_prod = mp
            dp[i] = max_prod
        return dp[n]

s = Solution()
print(s.integerBreak(10))
