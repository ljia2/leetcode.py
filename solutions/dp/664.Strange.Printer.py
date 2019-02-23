class Solution(object):
    def strangePrinter(self, s):
        """
        There is a strange printer with the following two special requirements:

        The printer can only print a sequence of the same character each time.

        At each turn, the printer can print new characters starting from and ending at any places,
        and will cover the original existing characters.

        Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

        Example 1:

        Input: "aaabbb"
        Output: 2
        Explanation: Print "aaa" first and then print "bbb".

        Example 2:
        Input: "aba"
        Output: 2
        Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
        Hint: Length of the given string will not exceed 100.

        :type s: str
        :rtype: int

        dp[i][j] denotes the min turns of printing substring from i to j.
        """

        if not s:
            return 0
        n = len(s) + 1
        dp = [[10**9+7 for _ in range(n)] for _ in range(n)]
        for r in range(len(dp)):
            dp[r][r] = 1

        for l in range(2, n):
            for i in range(1, n-l+1):
                j = l + i - 1
                for k in range(i, j):
                    #ls = from i to k i.e. s[i-1:k]
                    #rs = from k + 1 to j, i.e. s[k:j]
                    #the first char of ls and the first char of rs are same or the last char of ls and the last of rs are same.
                    #we can concatenate them directly with one turn is substracted
                    #because the printing of that matching char in rs is doubly counted.
                    if s[i-1] == s[k] or s[k-1] == s[j-1]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] - 1)
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

        return dp[1][len(s)]

s = Solution()
print(s.strangePrinter("aba"))
print(s.strangePrinter("aaabbb"))