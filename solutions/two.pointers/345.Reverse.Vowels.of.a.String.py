class Solution(object):
    def reverseVowels(self, s):
        """
        Write a function that takes a string as input and reverse only the vowels of a string.

        Example 1:

        Input: "hello"
        Output: "holle"
        Example 2:

        Input: "leetcode"
        Output: "leotcede"


        :type s: str
        :rtype: str
        """
        if not s:
            return s

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        c = list(s)
        l, r = 0, len(c)-1

        while l < r:
            while l < len(c) and c[l] not in vowels:
                l += 1
            while r > -1 and c[r] not in vowels:
                r -= 1

            if l < r:
                # c MUST BE A LIST!!!!
                c[l], c[r] = c[r], c[l]
                l += 1
                r -= 1
        return "".join(c)

s = Solution()
print(s.reverseVowels("leetcode"))