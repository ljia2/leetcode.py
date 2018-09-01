class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        elif len(haystack) < len(needle):
            return -1
        else:
            for i in range(len(haystack) - len(needle) + 1):
                hi = i
                bi = 0
                while hi < len(haystack) and bi < len(needle):
                    if haystack[i + bi] != needle[bi]:
                        break
                    else:
                        hi += 1
                        bi += 1
                if bi == len(needle):
                    return i
                elif hi == len(haystack):
                    return -1
            return -1