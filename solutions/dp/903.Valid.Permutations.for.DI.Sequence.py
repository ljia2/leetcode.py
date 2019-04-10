class Solution:
    def numPermsDISequence(self, S):
        """
        We are given S, a length n string of characters from the set {'D', 'I'}.
        (These letters stand for "decreasing" and "increasing".)

        A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:

        If S[i] == 'D', then P[i] > P[i+1], and;
        If S[i] == 'I', then P[i] < P[i+1].
        How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.

        Example 1:

        Input: "DID"
        Output: 5
        Explanation:
        The 5 valid permutations of (0, 1, 2, 3) are:
        (1, 0, 3, 2)
        (2, 0, 3, 1)
        (2, 1, 3, 0)
        (3, 0, 2, 1)
        (3, 1, 2, 0)

        Note:

        1 <= S.length <= 200
        S consists only of characters from the set {'D', 'I'}.

        :type S: str
        :rtype: int

        dp[i][j] represents the number of permutation of number 0, 1, ... , i,
        satisfying DI-rule S.substr(0, i) and ending with digit j

        if S[i-1] == 'D':
           dp[i][j] = dp[i-1][j] + dp[i-1][j+1] + ... + dp[i-1][i-1]

        So, why start with j, not j + 1, since the sequence is decreasing to j?
        Thought Experiment: In the sequence with length of i-1, the largest number in this sequence should be i-1.
        However, when we are dealing with length i and end with j, the previous sequence has already another j and we should also add i to the sequence.
        What we can do is, add one to all those numbers greater than or equal to j.
        This operation will make the largest number to be i without breaking the sequence property, also, it will free the j so that we can use it at the end of the sequence.
        By this thought experiment, we can easily get the result of X.
        For example, if the sequence is {3,4,1,2,5} and we want to expand it to be of length 6 and end with 3.
        We first make it to be {3->4,4->5,1,2,5->6}, and then, add 3 to the end of the sequence.

        if(S[i-1] == 'I')
           dp[i][j] = dp[i-1][0] + dp[i-1][1] + ... + dp[i-1][j-1]

        """
        if not S:
            return 0
        N = len(S) + 1
        dp = [[0] * N for _ in range(N)]
        # base case
        for c in range(N):
            dp[0][c] = 1

        # transition
        for i in range(1, N):
            # length of i
            for j in range(i+1):
                # ending with number j
                if S[i-1] == 'D':
                    # if j in the last position i, one of j, j+1, .. i-1 must be in second last position
                    for k in range(j, i):
                        dp[i][j] += dp[i-1][k]
                elif S[i-1] == 'I':
                    # if j in the last position i, 0, 1, ..., j-1 must be in second last position
                    for k in range(0, j):
                        dp[i][j] += dp[i-1][k]
        ans = 0
        mod = 10**9 + 7
        for k in range(N):
            ans += dp[N-1][k]
        return ans % mod


s = Solution()
print(s.numPermsDISequence("DID"))