class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == "":
            return -1
        char_dict = dict()
        for c in s:
            if c in char_dict.keys():
                char_dict[c] += 1
            else:
                char_dict[c] = 1
        for i in range(len(s)):
            if char_dict[s[i]] == 1:
                return i
        return -1