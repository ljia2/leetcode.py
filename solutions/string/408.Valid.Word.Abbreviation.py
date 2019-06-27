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
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue

            # invalid abbr
            if abbr[j] == '0' or not abbr[j].isnumeric():
                return False

            k = j
            while k + 1 < m and abbr[k + 1].isnumeric():
                k += 1

            number = abbr[j:k+1]

            i += int(number)

        # Important!!!! only match if i == n and j == m
        return True if i == n and j == m else False
s = Solution()
print(s.validWordAbbreviation("internationalization", "i12iz4n"))
print(s.validWordAbbreviation("internationalization", "13i5n"))
print(s.validWordAbbreviation("internationalization", "112i10"))