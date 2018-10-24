class Solution:
    def canPermutePalindrome(self, s):
        """

        Given a string, determine if a permutation of the string could form a palindrome.

        Example 1:

        Input: "code"
        Output: false
        Example 2:

        Input: "aab"
        Output: true
        Example 3:

        Input: "carerac"
        Output: true

        :type s: str
        :rtype: bool

        calculate the frequency of chars,
        allowing at most 1 odd frequency char.

        """

        if not s:
            return True

        cfreq = dict()
        for c in s:
            cfreq[c] = cfreq.get(c, 0) + 1
        odd_count = 0
        for c in cfreq.keys():
            if cfreq[c] % 2 == 1:
                odd_count += 1
                if odd_count > 1:
                    break

        return True if odd_count <= 1 else False