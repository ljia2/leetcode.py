class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == "":
            return 0

        start = 0
        end = start
        cloc = dict()
        max_len = -1
        while end < len(s):
            c = s[end]
            if c not in cloc.keys():
                length  = end - start + 1
                if len(cloc.keys()) < 2:
                    # an old char, update length from end to start
                    if max_len < length:
                        max_len = length
                else:
                    # a new char, find the new start
                    (k, v) = sorted(cloc.items(), key=lambda x: x[1])[0]
                    start = v + 1
                    cloc.pop(k)

                cloc[c] = end

            else:
                cloc[c] = end
                length = end - start + 1
                if max_len < length:
                    max_len = length
            end += 1
            return max_len


s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct("abccbddddde"))
