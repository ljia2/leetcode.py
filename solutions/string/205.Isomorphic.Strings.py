class Solution(object):
    def isIsomorphic(self, s, t):
        """
        Given two strings s and t, determine if they are isomorphic.

        Two strings are isomorphic if the characters in s can be replaced to get t.

        All occurrences of a character must be replaced with another character while preserving the order of characters.
        No two characters may map to the same character but a character may map to itself.

        Example 1:

        Input: s = "egg", t = "add"
        Output: true
        Example 2:

        Input: s = "foo", t = "bar"
        Output: false
        Example 3:

        Input: s = "paper", t = "title"
        Output: true
        Note:
        You may assume both s and t have the same length.

        :type s: str
        :type t: str
        :rtype: bool

       """

        if not s and not t:
            return True

        if not s or not t:
            return False

        if len(s) != len(t):
            raise Exception("Invalid Input!")

        # to ensure the mapping is one to one.
        maping = dict()
        # to avoid two characters to one character
        values = set()
        for i in range(len(s)):
            a, b = s[i], t[i]
            # a new mapping from a to b;
            if a not in maping.keys():
                if b not in values:
                    maping[a] = b
                    values.add(b)
                else:
                    return False
            # there is a mapping involving a and/or b;
            else:
                # there must be an existing mapping from a to b.
                if maping[a] == b:
                    continue
                else:
                    return False
        return True


s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("paper", "title"))