class DFSSolution(object): # DFS + Memorization

    def __init__(self):
        self.memory = dict()

    def wordBreak(self, s, wordDict):
        """

        Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
        add spaces in s to construct a sentence where each word is a valid dictionary word.
        Return all such possible sentences.

        Note:

        The same word in the dictionary may be reused multiple times in the segmentation.
        You may assume the dictionary does not contain duplicate words.
        Example 1:

        Input:
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        Output:
        [
          "cats and dog",
          "cat sand dog"
        ]
        Example 2:

        Input:
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        Output:
        [
          "pine apple pen apple",
          "pineapple pen apple",
          "pine applepen apple"
        ]
        Explanation: Note that you are allowed to reuse a dictionary word.

        Example 3:
        Input:
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        Output:
        []

        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]

        return all possibilities -> hints for backtracking
        However simple dfs TLE, we should leverage the DP for early pruning.

        """

        if not s or not wordDict:
            return []

        return self.dfs(s, set(wordDict))

    def dfs(self, s, wordDict):
        if s in self.memory.keys():
            return self.memory[s]

        ans = []
        if s in wordDict:
            ans.append(s)
        for i in range(1, len(s)):
            s_left, s_right = s[:i], s[i:]
            if s_right not in wordDict:
                continue

            lans = self.dfs(s_left, wordDict)
            lans = map(lambda x: x + " " + s_right, lans)
            ans.extend(lans)

        # use memory to store the full answer for s to avoid the duplication
        self.memory[s] = ans

        return ans

s = DFSSolution()
print(s.wordBreak("aaaaaaa", ["aaaa","aa","a"]))