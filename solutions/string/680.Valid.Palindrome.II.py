class Solution(object):
    def validPalindrome(self, s):
        """
        Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

        Example 1:
        Input: "aba"
        Output: True
        Example 2:
        Input: "abca"
        Output: True
        Explanation: You could delete the character 'c'.

        Note:
        The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

        :type s: str
        :rtype: bool
        """

        if not s:
            return True

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                s1 = s[:l] + s[l+1:]
                s2 = s[:r] + s[r+1:]
                return self.isPalindrome(s1) or self.isPalindrome(s2)
        return True

    def isPalindrome(self, s):
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

###### Follow up: if inset/del/swap is one operation, ask the minimum ops to make s a palindrome.
###### DP dp[i][j] stores the minimum ops to make s[i to j] palindrome
###### Base case length 1 and 2.
###### Transition Function 1) if