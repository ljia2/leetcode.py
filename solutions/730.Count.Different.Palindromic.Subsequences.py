class Solution:
    def countPalindromicSubsequences(self, S):
        """
        Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.

        A subsequence of a string S is obtained by deleting 0 or more characters from S.

        A sequence is palindromic if it is equal to the sequence reversed.

        Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

        Example 1:
        Input:
        S = 'bccb'
        Output: 6
        Explanation:
        The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.

        Note that 'bcb' is counted only once, even though it occurs twice.

        Example 2:
        Input:
        S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
        Output: 104860361

        Explanation:
        There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.

        Note:

        The length of S will be in the range [1, 1000].
        Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.

        :type S: str
        :rtype: int


        The output of count hints for dynamtic programming and size of inputs hints O(n^2) at most.

        How to define 2D array for dp[i][j]? However, how to guarantee the unique (i.e. avoid duplication?)

        dp[i][j] = # of ways of unique palindromic subsequences
        Transitions:
                   1) if s[i] = s[j]:
                     # for each solution for dp[i-1][j-1], we can attach s[i] and s[j] to two sides for new solutions and thus 2*dp[i-1][j-1] plusing s[i] and s[i]s[j] are two additional solutions;

                     # for example given "cdc" => "bcdcb". padding the pair of b on all palindromic subsequences'
                     # two sides generates valid subsequences. Moreover "b" and "bb" are two addtitional

                     1.1) dp[i][j] = 2 * dp[i-1][j-1] + 2 if s[i] not in s[i+1:j-1]

                     # for example given "cbc" => "bcbcb". padding the pair of b on all palindromic subsequences'
                     # two sides generates valid subsequences. Moreover only one  "bb" are an additional subsequence, because "b" already exists in the answer of "cbc"

                     1.2) dp[i][j] = 2 * dp[i-1][j-1] + 1 if s[i] is the same as the center of s[i+1:j-1]

                     # for example given "bcab" => "bbcabb" where l is the first char = s[i] and r is the last char = s[i]
                     # because the solution that "b" + "ca" + "b" where "ca" is counted twice where one by s[i] and s[j] and the other by s[l] and s[r]
                     1.3) dp[i][j] = 2 * dp[i+1][j-1] - dp[l][r]

                   2) if s[i] != s[j]
                      # "bc" => "abcd", dp[abc] + dp[bcd] - dp[bc], because dp[bc] is counted twice.
                      dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i-1][j-1] if s[i] != s[j]

        """
        if not S:
            return 0

        ways = [[0] * len(S) for i in range(len(S))]

        # base cases: for subarray of length 1 and 2
        for i in range(len(S)):
            ways[i][i] = 1
            if i < len(S) - 1:
                ways[i][i+1] = 2

        for ll in range(3, len(S)+1):
            for i in range(len(S) - ll + 1):
                j = ll + i - 1
                if S[i] != S[j]:
                    ways[i][j] = ways[i+1][j] + ways[i][j-1] - ways[i+1][j-1]
                else:
                    l = i + 1
                    while l < j and S[l] != S[i]:
                        l += 1
                    r = j - 1
                    while r > i and S[r] != S[j]:
                        r -= 1

                    if l < r:
                        ways[i][j] = 2 * ways[i+1][j-1] - ways[l+1][r-1]
                    elif l ==r :
                        ways[i][j] = 2 * ways[i+1][j-1] + 1
                    else:
                        ways[i][j] = 2 * ways[i+1][j-1] + 2
        return ways[0][len(S)-1] % (10**9 + 7)

s = Solution()
print(s.countPalindromicSubsequences("dbcbaaacdcbabcbddaac"))