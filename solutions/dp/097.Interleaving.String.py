class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

        Example 1:

        Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
        Output: true
        Example 2:

        Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
        Output: false

        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool

        dp[i][j] whether the first i chars of s1 and and the first j chars of s2 can interleave as the first i+j chars of s3.

        """
        if len(s3) != len(s1) + len(s2):
            return False
        l1 = len(s1)
        l2 = len(s2)
        dp = [[False] * (l2 + 1) for i in range(l1+1)]

        # base case, padding is needed.
        # two empty strings can interleaving as another empty prefix string of
        dp[0][0] = True

        for i in range(0, len(s1)+1):
            for j in range(0, len(s2)+1):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    # use no chars of s1 and only first j chars of s2
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    # use first i chars of s1 and no chars of s2
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1+j]
                else:
                    # use first i chars of s1 and j chars of s2
                    dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i-1+j])

        return dp[l1][l2]

s = Solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
