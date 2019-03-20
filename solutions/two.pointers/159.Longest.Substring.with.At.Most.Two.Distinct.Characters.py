# class Solution:
#     def lengthOfLongestSubstringTwoDistinct(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if s is None or s == "":
#             return 0
#
#         start = 0
#         end = start
#         cloc = dict()
#         max_len = -1
#         while end < len(s):
#             c = s[end]
#             if c not in cloc.keys():
#                 length  = end - start + 1
#                 if len(cloc.keys()) < 2:
#                     # an old char, update length from end to start
#                     if max_len < length:
#                         max_len = length
#                 else:
#                     # a new char, find the new start
#                     (k, v) = sorted(cloc.items(), key=lambda x: x[1])[0]
#                     start = v + 1
#                     cloc.pop(k)
#
#                 cloc[c] = end
#
#             else:
#                 cloc[c] = end
#                 length = end - start + 1
#                 if max_len < length:
#                     max_len = length
#             end += 1
#             return max_len
#
#
# s = Solution()
# print(s.lengthOfLongestSubstringTwoDistinct("abccbddddde"))


import collections

class BetterSolution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        Given a string s , find the length of the longest substring t
        that contains at most 2 distinct characters.

        Example 1:
        Input: "eceba"
        Output: 3
        Explanation: t is "ece" which its length is 3.

        Example 2:
        Input: "ccaabbb"
        Output: 5
        Explanation: t is "aabbb" which its length is 5.

        :type s: str
        :rtype: int

        an idea of typical sliding window.
        a window of two pointer from start to end.
        keep expanding the window by moving end to right as long as there are at most two chars between start and end.
        there are three elements in the window, keep shrinking start until there are two unique elements in the window.

        similar to LC713
        """
        if not s:
            return 0

        counters = collections.Counter()

        start = end = 0
        max_len = -1
        char_count = 0
        while end < len(s):
            if counters[s[end]] == 0:
                char_count += 1
            counters[s[end]] += 1

            while char_count > 2:
                counters[s[start]] -= 1
                if counters[s[start]] == 0:
                    char_count -= 1
                start += 1

            if max_len < end - start + 1:
                max_len = end - start + 1

        return max_len


s = BetterSolution()
print(s.lengthOfLongestSubstringTwoDistinct("abccbddddde"))