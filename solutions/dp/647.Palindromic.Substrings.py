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

        dp[i][j] indicates whether substring s[i:j+1] is a palidromic

        """

        if not s:
            return 0

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # base case
        for i in range(n):
            dp[i][i] = True
            if i + 1 < n and s[i] == s[i+1]:
                dp[i][i+1] = True

        # transition
        for l in range(3, n+1, 1):
            for i in range(n-l+2):
                j = l + i - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] and True

        count = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    count += 1
        return count