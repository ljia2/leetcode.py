class Solution:
    def minDistance(self, word1, word2):
        """
        Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same,
        where in each step you can delete one character in either string.

        Example 1:
        Input: "sea", "eat"
        Output: 2
        Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
        Note:
        The length of given words won't exceed 500.
        Characters in given words can only be lower-case letters.

        :type word1: str
        :type word2: str
        :rtype: int
        """
        # initialize the 2-d array
        min_del = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]
        # base cases:
        for i in range(1, len(word1)+1):
            min_del[i][0] = i
        for j in range(1, len(word2)+1):
            min_del[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    if i >= 2 and word1[i-2] == word2[j-1]:
                        min_del[i][j] = min(min_del[i-1][j-1], min_del[i-1][j] + 1)
                    elif j >= 2 and word1[i-1] == word2[j-2]:
                        min_del[i][j] = min(min_del[i-1][j-1], min_del[i][j-1] + 1)
                    else:
                        min_del[i][j] = min_del[i-1][j-1]
                else:
                    min_del[i][j] = min(min_del[i-1][j-1]+2, min(min_del[i-1][j] + 1, min_del[i][j-1]+1))
        return min_del[-1][-1]



class DPSolution:
    def minDistance(self, word1, word2):
        """
        Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

        Example 1:
        Input: "sea", "eat"
        Output: 2
        Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
        Note:
        The length of given words won't exceed 500.
        Characters in given words can only be lower-case letters.

        :type word1: str
        :type word2: str
        :rtype: int

        Find the minumum deletions of two strings is to equal to find the longest common substring S problem

        return len(word1) + len(word2) - 2 * len(S)

        dp[i][j] denotes the length of the longest substring between word1[:i] and word2[:j] (exclusive)

        dp[i][j] = if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
                   else max(dp[i-1][j], dp[i][j-1]

        """

        lcs = [[0] * (len(word2) + 1) for i in range(len(word1)) + 1]

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    lcs[i][j] = lcs[i-1][j-1] + 1
                else:
                    lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
        return len(word1) + len(word2) - 2 *lcs[-1][-1]


s = Solution()
print(s.minDistance("delete", "leet"))