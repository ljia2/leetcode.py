class Solution:
    def strStr(self, haystack, needle):
        """
        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Example 1:

        Input: haystack = "hello", needle = "ll"
        Output: 2

        Example 2:
        Input: haystack = "aaaaa", needle = "bba"
        Output: -1
        Clarification:

        What should we return when needle is an empty string? This is a great question to ask during an interview.

        For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

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
