class Solution(object):
    def numTilings(self, N):
        """
        We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

        XX  <- domino

        XX  <- "L" tromino
        X

        Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.

        (In a tiling, every square must be covered by a tile.
        Two tilings are different if and only if there are two 4-directionally adjacent cells on the board
        such that exactly one of the tilings has both squares occupied by a tile.)

        Example:
        Input: 3
        Output: 5

        Explanation:
        The five different ways are listed below, different letters indicates different tiles:
        XYZ XXZ XYY XXY XYY
        XYZ YYZ XZZ XYY XXY
        Note:

        N will be in range [1, 1000].

        :type N: int
        :rtype: int

        dp[i][0]: the number of tilings with no empty space
        dp[i][1]: the number of tilings with last top empty
        dp[i][2]: the number of tilings with last bottom empty
        """
        if N == 1:
            return 1
        if N == 2:
            return 2
        dp = [[0 for _ in range(3)] for _ in range(N+1)]
        # base cases
        dp[1][0] = 1
        dp[1][1] = 0
        dp[1][2] = 0
        dp[2][0] = 2
        dp[2][1] = 1
        dp[2][2] = 1

        for n in range(3, N+1):
            # dp[n-1][0] attached X
            #                     X
            # dp[n-2][0] attached XX
            #                     XX
            # dp[n-1][1] filled with XX
            #                         X
            # dp[n-1][2] filled with  X
            #                        XX
            dp[n][0] = dp[n-1][0] + dp[n-2][0] + dp[n-1][1] + dp[n-1][2]
            # dp[n-2][0] with a X
            #                   XX
            # dp[n-1][2] inserted with YY:  XX
            #                               XYY
            dp[n][1] = dp[n-2][0] + dp[n-1][2]
            dp[n][2] = dp[n-2][0] + dp[n-1][1]
        return dp[n][0] % (10**9+7)

s = Solution()
print(s.numTilings(4))

