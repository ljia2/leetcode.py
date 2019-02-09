class Solution:
    def countSubstrings(self, s):
        """

        Given a string, your task is to count how many palindromic substrings in this string.

        The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

        Example 1:
        Input: "abc"
        Output: 3
        Explanation: Three palindromic strings: "a", "b", "c".
        Example 2:
        Input: "aaa"
        Output: 6
        Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
        Note:
        The input string length won't exceed 1000. (HINT for O(N^2)

        :type s: str
        :rtype: int
        """

        if not s:
            return 0
        else:
            dp = [[False] * (len(s) + 1) for i in range(len(s) + 1)]

            for i in range(1, len(s)+1, 1):
                dp[i][i] = True
                if i < len(s) and s[i-1] == s[i]:
                    dp[i][i+1] = True

            for l in range(3, len(s)+1, 1):
                for i in range(1, len(s)+1-l+1, 1):
                    j = l + i - 1
                    if s[i-1] == s[j-1]:
                        dp[i][j] = dp[i+1][j-1] and True

            count = 0
            for i in range(1, len(s)+1, 1):
                for j in range(1, len(s)+1, 1):
                    if dp[i][j]:
                        count += 1
            return count