import numpy as np


class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        We partition a row of numbers A into at most K adjacent (non-empty) groups,
        then our score is the sum of the average of each group. What is the largest score we can achieve?

        Note that our partition must use every number in A, and that scores are not necessarily integers.

        Example:
        Input:
        A = [9,1,2,3,9]
        K = 3
        Output: 20
        Explanation:
        The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
        We could have also partitioned A into [9, 1], [2], [3, 9], for example.
        That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.


        Note:

        1 <= A.length <= 100.
        1 <= A[i] <= 10000.
        1 <= K <= A.length.
        Answers within 10^-6 of the correct answer will be accepted as correct.

        :type A: List[int]
        :type K: int
        :rtype: float

        dp[i][k]: the largest average score of spliting the first i elements in K ways.

        base case
        dp[i][0] = 0
        dp[i][k] = 0 if i < k

        for k in range(1, K):
            for i in range(k, len(A)+1):
                for j in range(i, len(A)-1)
                    dp[i][k] = dp[i][k-1] + mean(A[i+1:])

        return dp[len(A)][K]
        """

        if not A or K <= 0:
            raise Exception("Empty A or Non-Positive K!")

        maxAvg = [[0 for _ in range(len(A)+1)] for _ in range(K+1)]
        for a in range(1, len(A)+1):
            maxAvg[1][a] = sum(A[0:a]) / a

        for k in range(2, K+1):
            for i in range(2, len(A)+1):
                if i < k:
                    continue
                for j in range(k-1, i):
                    maxAvg[k][i] = max(maxAvg[k][i], maxAvg[k-1][j] + sum(A[j:i])/(i-j))
        return maxAvg[K][len(A)]

s = Solution()
print(s.largestSumOfAverages([9,1,2,3,9], 3))
