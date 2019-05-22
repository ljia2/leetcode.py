import collections

class Solution(object):
    def longestSubstring(self, s, k):
        """
        Find the length of the longest substring T of a given string (consists of lowercase letters only)
        such that every character in T appears no less than k times.

        Example 1:

        Input:
        s = "aaabb", k = 3

        Output:
        3

        The longest substring is "aaa", as 'a' is repeated 3 times.
        Example 2:

        Input:
        s = "ababbc", k = 2

        Output:
        5

        The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

        :type s: str
        :type k: int
        :rtype: int

        use a dictionary to representing the sliding window where key is char and value is its frequency

        we need to use numLessThan, record the number of unique chars whose frequency less than K.

        a qualified window is when numLessThan is zero.

        """
        if not s or len(s) < k:
            return 0

        n = len(s)
        start = 0
        ssdict = dict()
        for end, c in enumerate(s):
            # given the left boundary i, moving right boundary until form a valid substring
            while not self.valid(ssdict) and j < len(s):
                ssdict[c] = ssdict.get(c, 0) + 1
                j += 1



