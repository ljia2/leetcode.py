class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        slength = len(s)
        if slength < 2:
            return False
        else:
            for i in range(slength//2, 0, -1):
                if slength % i != 0:
                    continue
                subs = s[:i]
                expandS = subs
                while len(expandS) < slength:
                    expandS += subs
                if expandS == s:
                    return True
            return False