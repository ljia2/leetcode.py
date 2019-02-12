class Solution:
    def repeatedSubstringPattern(self, s):
        """
         appending multiple copies of the substring together.
         You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
        Example 1:

        Input: "abab"
        Output: True
        Explanation: It's the substring "ab" twice.
        Example 2:

        Input: "aba"
        Output: False
        Example 3:

        Input: "abcabcabcabc"
        Output: True
        Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

        :type s: str
        :rtype: bool
        """

        if len(s) < 2:
            return False
        for i in range(len(s)//2, 0, -1):
            if len(s) % i != 0:
                continue
            subs = s[:i]
            expandS = subs
            while len(expandS) < len(s):
                expandS += subs
            if expandS == s:
                return True
        return False