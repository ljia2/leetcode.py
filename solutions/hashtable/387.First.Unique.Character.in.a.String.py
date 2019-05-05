class Solution:
    def firstUniqChar(self, s):
        """
        Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

        Examples:

        s = "leetcode"
        return 0.

        s = "loveleetcode",
        return 2.
        Note: You may assume the string contain only lowercase letters.

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