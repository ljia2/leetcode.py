class DPSolution: # TLE
    def longestPalindromeSubseq(self, s):
        """
        Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

        Example 1:
        Input:
        "bbbab"
        Output:
        4
        One possible longest palindromic subsequence is "bbbb".

        Example 2:
        Input:

        "cbbd"
        Output:
        2
        One possible longest palindromic subsequence is "bb".

        :type s: str
        :rtype: int

        Note that subseq is not substring, given "bbbab", strip the left/right most chars we have "bba" where
        the longest palindromic subsequnce length is 2 ("bb"). Then the longest subsequence of "bbbab" is 2 + 2


        l[i][j]: denote the length of longest palindrome subseq where i is the start and j is the end

        base cases:

        l[i][j] = 0 if i < j(empty string)
                  1 if i = j

        generalized cases (i < j)
        l[i][j] = 2 + l[i+1][j-1] if s[i] == s[j]
                  max(l[i][j-1], l[i+1][j]) otherwise s[i] != s[j]

        dynamic programming length from 2 to len(s) + 1 and i from 0 to len(s) - l + 1 (i.e j = l +i - 1)

        T: O(n^2)
        S: O(n^2)
        """
        if not s:
            return 0
        lpss = [[0] * len(s) for i in range(len(s))]

        for i in range(len(s)):
            lpss[i][i] = 1
        # length from 2 to len(s)
        for l in range(2, len(s)+1):
            for i in range(0, len(s) - l + 1):
                j = l + i - 1
                if s[i] == s[j]:
                    lpss[i][j] = 2 + lpss[i+1][j-1]
                else:
                    lpss[i][j] = max(lpss[i+1][j], lpss[i][j-1])
        return lpss[0][len(s)-1]

class DPSolution2:
    def longestPalindromeSubseq(self, s):
        """
        Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

        Example 1:
        Input:
        "bbbab"
        Output:
        4
        One possible longest palindromic subsequence is "bbbb".

        Example 2:
        Input:

        "cbbd"
        Output:
        2
        One possible longest palindromic subsequence is "bb".

        :type s: str
        :rtype: int

        Note that subseq is not substring, given "bbbab", strip the left/right most chars we have "bba" where
        the longest palindromic subsequnce length is 2 ("bb"). Then the longest subsequence of "bbbab" is 2 + 2


        l[i][j]: denote the length of longest palindrome subseq where i is the start and j is the end

        base cases:

        l[i][j] = 0 if i < j(empty string)
                  1 if i = j

        generalized cases (i < j)
        l[i][j] = 2 + l[i+1][j-1] if s[i] == s[j]
                  max(l[i][j-1], l[i+1][j]) otherwise s[i] != s[j]

        dynamic programming i from down to up and j from left to right

        T: O(n^2)
        S: O(n^2)
        """
        if not s:
            return 0
        lpss = [[0] * len(s) for i in range(len(s))]

        for i in range(len(s)):
            lpss[i][i] = 1

        # length from 2 to len(s)
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    lpss[i][j] = 2 + lpss[i+1][j-1]
                else:
                    lpss[i][j] = max(lpss[i][j-1], lpss[i+1][j])
        return lpss[0][len(s)-1]

class BestSolution: #Space O(n)
    def longestPalindromeSubseq(self, s):
        """
        Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

        Example 1:
        Input:
        "bbbab"
        Output:
        4
        One possible longest palindromic subsequence is "bbbb".

        Example 2:
        Input:

        "cbbd"
        Output:
        2
        One possible longest palindromic subsequence is "bb".

        :type s: str
        :rtype: int

        Note that subseq is not substring, given "bbbab", strip the left/right most chars we have "bba" where
        the longest palindromic subsequnce length is 2 ("bb"). Then the longest subsequence of "bbbab" is 2 + 2


        l[i][j]: denote the length of longest palindrome subseq where i is the start and j is the end

        base cases:

        l[i][j] = 0 if i < j(empty string)
                  1 if i = j

        generalized cases (i < j)
        l[i][j] = 2 + l[i+1][j-1] if s[i] == s[j]
                  max(l[i][j-1], l[i+1][j]) otherwise s[i] != s[j]

        l[i][j] only use l[i+1][j-1], l[i][j-1], l[i+1][j]
        """
        if not s:
            return 0
        lpss = [0] * len(s) # lpss[k] = lpss[i][j] if k < j
                            #           lpss[i+1][j] k >= j

        for i in range(len(s)-1, -1, -1):
            lpss[i] = 1 # single char string is 1
            iplus1jminus1 = 0 # empty string is 0
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    iplus1jminus1, lpss[j] = lpss[j], 2 + iplus1jminus1
                else:
                    iplus1jminus1, lpss[j] = lpss[j], max(lpss[j-1], lpss[j])
        return lpss[-1]


s = BestSolution()
print(s.longestPalindromeSubseq("aaa"))