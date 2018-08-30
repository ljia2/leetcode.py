class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
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
                l = end - start + 1
                if max_len < l:
                    max_len = l
            else:
                if len(cloc.keys()) < k:
                    l = end - start + 1
                    if max_len < l:
                        max_len = l
                else:
                    kc, v = sorted(cloc.items(), key=lambda x: x[1])[0]
                    cloc.pop(kc)
                    start = v + 1
                cloc[c] = end
            end += 1
        return max_len

s = Solution()
print(s.lengthOfLongestSubstringKDistinct("aba", 1))