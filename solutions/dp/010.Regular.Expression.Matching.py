class Solution:
    def isMatch(self, s, p):
        """

        Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).

        Note:

        s could be empty and contains only lowercase letters a-z.
        p could be empty and contains only lowercase letters a-z, and characters like . or *.
        Example 1:

        Input:
        s = "aa"
        p = "a"
        Output: false
        Explanation: "a" does not match the entire string "aa".
        Example 2:

        Input:
        s = "aa"
        p = "a*"
        Output: true
        Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
        Example 3:

        Input:
        s = "ab"
        p = ".*"
        Output: true
        Explanation: ".*" means "zero or more (*) of any character (.)".
        Example 4:

        Input:
        s = "aab"
        p = "c*a*b"
        Output: true
        Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
        Example 5:

        Input:
        s = "mississippi"
        p = "mis*is*p*."
        Output: false

        :type s: str
        :type p: str
        :rtype: bool

        Idea:
        dynamtic programming for two strings:

        2-d boolean array dp = [[false] * (len(p) + 1) for s in range(len(s) + 1)] where dp[i][j] indicate whether s[:i+1] in s matches p[:j+1].
        For example dp[1][1] indicate if s[0] matches p[0]

        initialize base cases:
        dp[0][0] = true, because two empty prefix substrings from s and p matches.

        1) if p[j] == s[i] or p[j] == '.' : dp[i+1][j+1] = dp[i][j] # "aa" vs "aa" or "aa" vs "a."
        2) if p[j] == "*" and p[j-1] != s[i]:
                dp[i+1][j+1] = dp[i+1][j-1] # "a" vs "ab*", if p[2] == '*' and p[1] != s[0] (b != a):
                                            # set b* empty by dp[1][3] = dp[1][1] (check whether s[1] and p[1] match)
        3) if p[j] == "*" and (p[j-1] == s[i] or p[i-1] == '.'):
               dp[i+1][j+1] = dp[i+1][j] # in this case, a* count as a single a and * repeat zero times of a.
               dp[i+1][j+1] = dp[i][j+1] # in this case a* count as multiple a; for example "aaa" vs "a*" depends on whether "aa" matches "a*"
               dp[i+1][j+1] = dp[i+1][j-1] # in this case a* count as empty.
        """

        if s is None or p is None:
            return False

        sl = len(s)
        pl = len(p)
        dp = [[False] * (pl + 1) for i in range(sl + 1)]

        # Initialization.
        # because two empty prefix substrings from s and p matches.
        dp[0][0] = True
        # preprocessing: in case "aab" vs c*d*aab
        for i in range(len(p)):
            if i > 0 and p[i] == "*" and dp[0][i-1]:
                dp[0][i+1] = True

        for i in range(sl):
            for j in range(pl):
                # update dp[i+1][j+1]

                # "aa" match "a."
                if p[j] == s[i] or p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]

                # "a" matches "ab*"
                if p[j] == "*" and p[j-1] != s[i]:
                    dp[i+1][j+1] = dp[i+1][j-1]

                # a matches a* or a matches .* or a match aa*
                if p[j] == "*" and (p[j-1] == s[i] or p[i-1] == '.'):
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1]

        return dp[sl][pl]

s = Solution()
print(s.isMatch("aab", "c*d*aab"))