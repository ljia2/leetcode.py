class Solution:
    def numDistinct(self, s, t):
        """

        Given a string S and a string T, count the number of distinct subsequences of S which equals T.

        A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
        of the characters without disturbing the relative positions of the remaining characters.
        (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

        Example 1:

        Input: S = "rabbbit", T = "rabbit"
        Output: 3
        Explanation:

        As shown below, there are 3 ways you can generate "rabbit" from S.
        (The caret symbol ^ means the chosen letters)

        rabbbit
        ^^^^ ^^
        rabbbit
        ^^ ^^^^
        rabbbit
        ^^^ ^^^
        Example 2:

        Input: S = "babgbag", T = "bag"
        Output: 5
        Explanation:

        As shown below, there are 5 ways you can generate "bag" from S.
        (The caret symbol ^ means the chosen letters)

        babgbag
        ^^ ^
        babgbag
        ^^    ^
        babgbag
        ^    ^^
        babgbag
          ^  ^^
        babgbag
            ^^^
        :type s: str
        :type t: str
        :rtype: int

         dp[i][j] = stores the number of unique substrings in s[:i] equal to t[:j]
         1) if i < j: dp[i][j] = 0
         2) if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] (the results of s[:i-1] vs t[:j-1] give match) + dp[i-1][j] (the results of s[:i-1] with t[j], not using the match)
         3) if s[i-1] != t[j-1]:
                dp[i][j] = dp[i-1][j] the results of s[:i-1] and t[:j]

        """

        if len(s) < len(t):
            return 0
        else:
            dp = [[0] * (len(t) + 1) for i in range(len(s) + 1)]

            dp[0][0] = 1

            # empty target string is a substring of source
            for i in range(1, len(s) + 1, 1):
                dp[i][0] = 1

            for i in range(1, len(s) + 1, 1):
                for j in range(1, len(t) + 1, 1):
                    if i < j:
                        dp[i][j] = 0
                    elif s[i-1] == t[j-1]:
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
            return dp[len(s)][len(t)]

s = Solution()
print(s.numDistinct("babgbag", "bag"))