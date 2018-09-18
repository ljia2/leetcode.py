class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

        Example 1:
        Input: s1 = "sea", s2 = "eat"
        Output: 231
        Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
        Deleting "t" from "eat" adds 116 to the sum.
        At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

        Example 2:
        Input: s1 = "delete", s2 = "leet"
        Output: 403
        Explanation: Deleting "dee" from "delete" to turn the string into "let",
        adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
        At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
        If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
        Note:

        0 < s1.length, s2.length <= 1000.

        :type s1: str
        :type s2: str
        :rtype: int

        """
        min_dp = [[0] * (len(s2) + 1) for r in  range((len(s1) + 1))]

        sum = 0
        for i in range(1, len(s1)+1):
            sum += ord(s1[i-1])
            min_dp[i][0] = sum
        sum = 0
        for j in range(1, len(s2)+1):
            sum += ord(s2[j-1])
            min_dp[0][j] = sum

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2) + 1):
                if s1[i-1] == s2[j-1]:
                    # when s1[i-1] matches s2[j-1], we need to check the s1[i-2] and s2[j-1] (or s1[i-1] vs s1[j-2])
                    if i >= 2 and s1[i-2] == s2[j-1]:
                        min_dp[i][j] = min(min_dp[i-1][j-1], min_dp[i-1][j] + ord(s1[i-1]))
                    elif j >= 2 and s1[i-1] == s2[j-2]:
                        min_dp[i][j] = min(min_dp[i-1][j-1], min_dp[i][j-1] + ord(s2[j-1]))
                    else:
                        min_dp[i][j] = min_dp[i-1][j-1]
                else:
                    min_dp[i][j] = min(min(min_dp[i-1][j-1] + ord(s1[i-1]) + ord(s2[j-1]), min_dp[i-1][j] + ord(s1[i-1])), min_dp[i][j-1] + ord(s2[j-1]))

        return min_dp[-1][-1]

s = Solution()
print(s.minimumDeleteSum("delete", "leet"))
#print(s.minimumDeleteSum("sea", "eat"))