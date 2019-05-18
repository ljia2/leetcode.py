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

class SolutionII:
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
        ns = len(s)
        nt = len(t)
        if abs(ns-nt) >= 2:
            return False
        l = min(ns, nt)
        for i in range(l):
            if s[i] != t[i]:
                if ns == nt:
                    # whether match by replace
                    return s[:i] == t[:i] and s[i+1:] == t[i+1:]
                elif ns + 1 == nt:
                    # whether match by remove one from t
                    return s[:i] == t[:i] and s[i:] == t[i+1:]
                else:
                    # ns == nt + 1
                    # whether match by remove one from s
                    return s[:i] == t[:i] and s[i+1:] == t[i:]
        return True