class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

        Example:

        Input: 2
        Output: 91
        Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
                     excluding 11,22,33,44,55,66,77,88,99

        :type n: int
        :rtype: int

        dp[i] denotes # of all numbers with unique digits 0 <= x < 10^n

        for i < 11 digits, # of unique digits number with i-1 digits (dp[i-1] + # of unique digits with i digits, (9*9*8*7....)
        if i > 10 digits, # of unique digits numbers with 10 digits (i.e. dp[i-1]

        """

        dp = [1] * (n + 1)
        for i in range(1, n+1):
            if i < 11:
                m = 9
                cnt = m
                for d in range(1, i):
                    cnt *= m
                    m -= 1
                dp[i] = dp[i-1] + cnt
            else:
                dp[i] = dp[i-1]
        return dp[n]

s = Solution()
for p in range(12):
    print(p, s.countNumbersWithUniqueDigits(p))
