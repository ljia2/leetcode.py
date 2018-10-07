class Solution:
    def longestPalindrome(self, s):
        """
        Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

        This is case sensitive, for example "Aa" is not considered a palindrome here.

        Note:
        Assume the length of given string will not exceed 1,010.

        Example:

        Input:
        "abccccdd"

        Output:
        7

        Explanation:
        One longest palindrome that can be built is "dccaccd", whose length is 7.
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        cfreq = dict()
        for c in s:
            cfreq[c] = cfreq.get(c, 0) + 1
        return self.calcLongestPalindromeLength(cfreq)

    def calcLongestPalindromeLength(self, cfreq):
        length = 0
        for (k, v) in cfreq.items():
            if v % 2 == 0:
                length += v
        odd = 0
        for (k, v) in cfreq.items():
            # if k has odd frequency, we use v-1 to build palidrome
            if v % 2 == 1:
                length += v - 1
                odd = 1

        # if we have a char with odd frequency, we can put it in the middle
        return length + odd



s = Solution()
print(s.longestPalindrome("abccccdd"))
print(s.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))