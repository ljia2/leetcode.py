class Solution(object):
    def isPalindrome(self, s):
        """
        Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

        Note: For the purpose of this problem, we define empty string as valid palindrome.

        Example 1:

        Input: "A man, a plan, a canal: Panama"
        Output: true
        Example 2:

        Input: "race a car"
        Output: false

        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) == 1:
            return True
        s = s.lower()
        l = 0
        r = len(s)-1
        while l < r:
            # skip non alphanumeric chars
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


