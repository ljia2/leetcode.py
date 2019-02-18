class Solution:
    def longestPalindrome(self, s):
        """
        Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

        Example 1:

        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.
        Example 2:

        Input: "cbbd"
        Output: "bb"
        :type s: str
        :rtype: str

        expansion at center 1) anana with a center a 2) abba with a center bb

        T: O(n^2)
        """
        if not s:
            return ""
        else:
            longest = ""
            for i in range(len(s)):
                p = self.expand(s, i, i)
                if len(p) > len(longest):
                    longest = p
                if i < len(s) - 1:
                    p = self.expand(s, i, i+1)
                    if len(p) > len(longest):
                        longest = p
            return longest

    def expand(self, s, start, end):
        while start >=0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end +=1
        return s[start+1:end]

class DPSolution:
    def longestPalindrome(self, s):
        """
        Given a string s, find the longest palindromic substring in s.
        You may assume that the maximum length of s is 1000. hint for O(n^2)

        Example 1:

        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.
        Example 2:

        Input: "cbbd"
        Output: "bb"
        :type s: str
        :rtype: str

        maximum length of s is 1000: hint for O(n^2)

        dynamic programming for a substring of a given string:

        dp[i][j] is true or false indicate the substring (starting the ith char and ending with the jth char) is a palindrome or not

        base case:
        dp[0][0] = True
        dp[i][i] = True
        dp[i][i+1] = s[i-1] == s[i]

        transition function by iterating the length of string starting i
        for l in range(3, len(s) + 1):
            j = i + l - 1

            dp[i][j] = dp[i+1][j-1] and s[i] == s[j] if j >= i + 2

        result: max(j-i s.t. dp[i][j] = True)

        """
        if not s:
            return ""

        # declare the 2-d DP array
        dp = [[False] * (len(s) + 1) for _ in range((len(s) + 1))]

        # base case initialization of substring length of 1 and 2
        for i in range(1, len(s)+1):
            dp[i][i] = True
            # if the ith char is the same as the i+1 char
            if i < len(s) and s[i-1] == s[i]:
                dp[i][i+1] = True

        # for DP expansion from i,j to i-1, j+1, we iterate over length l of substring
        # length of substring from 3 to len(s) inclusive
        for l in range(3, len(s)+1, 1):
            # start of substring at i
            for i in range(1, (len(s) + 1) - l + 1, 1):
                # j is the end point of substring of length l
                j = l + i - 1
                if s[i-1] == s[j-1]:
                    dp[i][j] = dp[i+1][j-1] and True

        longest = ""
        for i in range(1, len(s)+1):
            for j in range(i, len(s)+1):
                if dp[i][j]:
                    if len(longest) < j - i + 1:
                        longest = s[i-1:j]
        return longest

s = DPSolution()
print(s.longestPalindrome("abcba"))
print(s.longestPalindrome("babab"))
