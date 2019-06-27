class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Given a string, find the length of the longest substring without repeating characters.

        Example 1:

        Input: "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        Example 2:

        Input: "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.
        Example 3:

        Input: "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.

        Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

        :type s: str
        :rtype: int
        """

        if not s or len(s) < 2:
            return len(s)

        window = dict()

        l = r = 0
        ans = -1
        while r < len(s):
            c = s[r]

            # if an old char is met already
            if c in window.keys():
                # reset the start but window[c] may be out of current window.
                # we use max.
                l = max(l, window[c] + 1)

            window[c] = c

            ans = max(ans, r - l + 1)
            r += 1

        return ans

s = Solution()
print(s.lengthOfLongestSubstring("abba"))
print(s.lengthOfLongestSubstring("abcabcbb"))