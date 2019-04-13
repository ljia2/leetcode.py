class Solution(object):
    def rotatedDigits(self, N):

        """
        X is a good number if after rotating each digit individually by 180 degrees,
        we get a valid number that is different from X.
        Each digit must be rotated - we cannot choose to leave it alone.

        A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves;
        2 and 5 rotate to each other; 6 and 9 rotate to each other,
        and the rest of the numbers do not rotate to any other number and become invalid.

        Now given a positive number N, how many numbers X from 1 to N are good?

        Example:
        Input: 10
        Output: 4
        Explanation:
        There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
        Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

        Note:

        N  will be in range [1, 10000].
        :type N: int
        :rtype: int

        Let consider
        0 - 9: must have 2, 5, 6, 9
        10 - 99: consider XY: X and Y respectively.
        100 - 999: consider XXY: XX and Y respectively. .
        ....

        dp[i] = 0 invalid after rotation
                1 same number after rotation
                2 different number after rotation
        """
        ans = 0
        dp = [0] * (N + 1)
        for i in range(N + 1):
            if i < 10:
                if i == 1 or i == 0 or i == 8:
                    dp[i] = 1
                elif i == 2 or i == 5 or i == 6 or i == 9:
                    dp[i] = 2
                    ans += 1
            else:
                a = dp[i/10]
                b = dp[i % 10]
                if a == 1 and b == 1:
                    dp[i] = 1
                elif a >= 1 and b >= 1:
                    # a = 1 and b = 2
                    # a = 2 and b = 1
                    # a = 2 and b = 2
                    dp[i] = 2
                    ans += 1
        return ans

