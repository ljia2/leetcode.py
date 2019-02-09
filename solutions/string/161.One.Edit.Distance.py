class Solution:
    def isOneEditDistance(self, s, t):
        """

        Given two strings s and t, determine if they are both one edit distance apart.

        Note:

        There are 3 possiblities to satisify one edit distance apart:

        Insert a character into s to get t
        Delete a character from s to get t
        Replace a character of s to get t
        Example 1:

        Input: s = "ab", t = "acb"
        Output: true

        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) == len(t):
            diff = 0
            if s == t:
                return False
            else:
                for i in range(len(s)):
                    if s[i] != t[i]:
                        diff += 1
                    if diff > 1:
                        return False
                return True
        elif len(s) == len(t) + 1:
            for i in range(len(s)):
                new_s = s[:i] + s[i+1:]
                if t == new_s:
                    return True
            return False
        elif len(s) + 1 == len(t):
            for i in range(len(t)):
                new_t = t[:i] + t[i+1:]
                if s == new_t:
                    return True
            return False
        else:
            return False