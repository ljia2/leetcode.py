
class Solution:
    def minDistance(self, word1, word2):
        """
        Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

        You have the following 3 operations permitted on a word:

        Insert a character
        Delete a character
        Replace a character

        Example 1:

        Input: word1 = "horse", word2 = "ros"
        Output: 3
        Explanation:
        horse -> rorse (replace 'h' with 'r')
        rorse -> rose (remove 'r')
        rose -> ros (remove 'e')
        Example 2:

        Input: word1 = "intention", word2 = "execution"
        Output: 5
        Explanation:
        intention -> inention (remove 't')
        inention -> enention (replace 'i' with 'e')
        enention -> exention (replace 'n' with 'x')
        exention -> exection (replace 'n' with 'c')
        exection -> execution (insert 'u')

        :type word1: str
        :type word2: str
        :rtype: int

        dynamtic programming for two strings:
        dp is a 2d array (len(word1)+1, len(word2)+1)
        dp[i][j] stores the minimum edit distance between word1[0:i] vs. word2[0:j]

        1) dp[0][0] = 0
        2) if i == 0 or j == 0: dp[0][j] = j  or dp[i][0] = i
        3) if word1[i] == word[j]:
                dp[i][j] = dp[i-1][j-1]
           else:
               # replace word1[i] with word2[j]
               # insert word2[j]
               # delete word2[j]
               dp[i][j] = min(dp[i-1][j-1], dp[i][j-]] + 1, dp[i-1][j] + 1)
        """

        if word1 == "" or word2 == "":
            return len(word1) if word2 == "" else len(word2)

        l1 = len(word1)
        l2 = len(word2)

        dp = [[0] * (l1 + 1) for _ in range(l2+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if i == j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(min(dp[i-1][j-1] + 1, dp[i][j-1] + 1), dp[i-1][j] + 1)
        return dp[-1][-1]
