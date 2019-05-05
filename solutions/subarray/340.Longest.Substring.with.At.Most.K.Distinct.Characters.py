class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        Given a string, find the length of the longest substring T that contains at most k distinct characters.

        Example 1:

        Input: s = "eceba", k = 2
        Output: 3
        Explanation: T is "ece" which its length is 3.
        Example 2:

        Input: s = "aa", k = 1
        Output: 2
        Explanation: T is "aa" which its length is 2.

        :type s: str
        :type k: int
        :rtype: int
        """
        if s is None or s == "" or k < 1:
            return 0

        max_len = 0
        start = 0
        end = start
        cloc = dict()
        while end < len(s):
            c = s[end]
            if c in cloc.keys():
                cloc[c] = end
                max_len = max(max_len, end - start + 1)
            else:
                if len(cloc.keys()) < k:
                    max_len = max(max_len, end - start + 1)
                else:
                    # find the char, kc, with the most front pos v.
                    kc, v = sorted(cloc.items(), key=lambda x: x[1])[0]
                    # delete kv from cloc
                    cloc.pop(kc)
                    # reset the start to v+1
                    start = v + 1
                # update the latest position of c.
                cloc[c] = end
            end += 1
        return max_len

s = Solution()
print(s.lengthOfLongestSubstringKDistinct("aba", 1))



class SolutionII:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        Given a string, find the length of the longest substring T that contains at most k distinct characters.

        Example 1:

        Input: s = "eceba", k = 2
        Output: 3
        Explanation: T is "ece" which its length is 3.
        Example 2:

        Input: s = "aa", k = 1
        Output: 2
        Explanation: T is "aa" which its length is 2.

        :type s: str
        :type k: int
        :rtype: int


        use a dictionary representing the sliding window where key is char and value is the biggest position.

        """
        if s is None or s == "" or k < 1:
            return 0

        max_len = 0
        start = 0
        end = start
        # a sliding window (dict) where key is char and val is the biggest pos of key
        cloc = dict()
        while end < len(s):
            c = s[end]
            if c in cloc.keys():
                cloc[c] = end
                max_len = max(max_len, end - start + 1)
            else:
                # there less than k distint keys in the window.
                if len(cloc.keys()) < k:
                    max_len = max(max_len, end - start + 1)
                else:
                    v = min(cloc.values())
                    # delete s[v] from cloc, to ensure the window has k - 1 distint keys.
                    cloc.pop(cloc[s[v]])
                    # reset the start to v+1
                    start = v + 1
                # update the latest position of c.
                cloc[c] = end
            end += 1
        return max_len