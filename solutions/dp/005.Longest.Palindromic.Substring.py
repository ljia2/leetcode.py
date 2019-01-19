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
        Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000. (hint for O(n^2)

        Example 1:

        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.
        Example 2:

        Input: "cbbd"
        Output: "bb"
        :type s: str
        :rtype: str
        dp[i][j] is true or false indicate the substring s[i:j+1] is a palindrom or not
        """
        if not s:
            return ""
        else:
            # declare the dp array
            dp = [[False] * (len(s) + 1) for i in range((len(s) + 1))]
            # base case initialization of substring length of 1 and 2
            for i in range(len(s)):
                dp[i+1][i+1] = True
                if i < len(s)-1 and s[i] == s[i+1]:
                    dp[i+1][i+2] = True

            # for DP expansion from i,j to i-1, j+1, we iterate over length l of substring
            for l in range(3, len(s)+1, 1): # length of substring from 3 to len(s) inclusive
                for i in range(1, len(s)+1-l+1, 1): # start of substring at i
                    j = l + i - 1 # j is the end point of substring of length l
                    print(i, j, l)
                    if s[i-1] == s[j-1]:
                        dp[i][j] = dp[i+1][j-1] and True

            longest = ""
            for i in range(1, len(s)+1, 1):
                for j in range(1, len(s)+1, 1):
                    if dp[i][j]:
                        if len(longest) < len(s[i-1:j]):
                            longest = s[i-1:j]
            return longest

s = DPSolution()
print(s.longestPalindrome("abcba"))
