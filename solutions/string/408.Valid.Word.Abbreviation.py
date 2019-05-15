class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

        A string such as "word" contains only the following valid abbreviations:

        ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
        Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

        Note:
        Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

        Example 1:
        Given s = "internationalization", abbr = "i12iz4n":

        Return true.
        Example 2:
        Given s = "apple", abbr = "a2e":

        Return false.

        :type word: str
        :type abbr: str
        :rtype: bool
        """

        if not word and not abbr:
            return True

        if not word or not abbr:
            return False

        i = j = 0
        n = len(word)
        m = len(abbr)
        while i < n and j < m:
            token, j = self.next_token(abbr, j)
            if token.isnumeric() and token[0] != '0':
                i += int(token)
            else:
                if word[i] == token:
                    i += 1
                else:
                    return False

        # Important!!!! only match if i == n and j == m
        return True if i == n and j == m else False

    def next_token(self, abbr, j):
        if abbr[j].isnumeric():
            k = j
            while k + 1 < len(abbr) and abbr[k+1].isnumeric():
                k += 1
            return abbr[j:k+1], k + 1
        else:
            return abbr[j], j + 1

s = Solution()
print(s.validWordAbbreviation("internationalization", "i12iz4n"))
print(s.validWordAbbreviation("internationalization", "13i5n"))
print(s.validWordAbbreviation("internationalization", "112i10"))