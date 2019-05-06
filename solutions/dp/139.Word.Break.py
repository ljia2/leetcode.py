class DPSolution:
    # DP Solution
    def wordBreak(self, s, wordDict):
        """

        Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

        Note:

        The same word in the dictionary may be reused multiple times in the segmentation.
        You may assume the dictionary does not contain duplicate words.
        Example 1:

        Input: s = "leetcode", wordDict = ["leet", "code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".
        Example 2:

        Input: s = "applepenapple", wordDict = ["apple", "pen"]
        Output: true
        Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
                     Note that you are allowed to reuse a dictionary word.
        Example 3:

        Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
        Output: false

        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        T: O(n^2)
        S: O(n^2)

        """
        if not wordDict or s is None or s == "":
            return False

        # checked[i] is True means the prefix from 0 to i (inclusive) can be represented by dict
        checked = [False] * (len(s) + 1)
        # Assuming empty string can be dict-represented
        checked[0] = True
        # for each position in checked starting 1
        for i in range(1, len(s)+1):
            # calculate its prefix from 0 to j (inclusive) and segment from j to i (inclusive)
            for j in range(0, i):
                if checked[j] and s[j:i] in wordDict:
                    """
                    if the prefix from 0 to j (inclusive) is dict-represented and segment from j to i (inclusive) are in dict and
                    then the prefix from 0 to i (inclusive) is dict-represented
                    """
                    checked[i] = True
                    break
        return checked[len(s)]


def main():
    s = DPSolution()
    print(s.wordBreak("leetcode", ["leet", "code"]))


if __name__ == "__main__":
    main()


## Follow up: what is asking for the minimum number of segments in the dictionary.

class DPSolution:
    # DP Solution
    def wordBreak(self, s, wordDict):
        """

        Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

        Note:

        The same word in the dictionary may be reused multiple times in the segmentation.
        You may assume the dictionary does not contain duplicate words.
        Example 1:

        Input: s = "leetcode", wordDict = ["leet", "code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".
        Example 2:

        Input: s = "applepenapple", wordDict = ["apple", "pen"]
        Output: true
        Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
                     Note that you are allowed to reuse a dictionary word.
        Example 3:

        Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
        Output: false

        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        T: O(n^2)
        S: O(n^2)

        """
        if not wordDict or s is None or s == "":
            return False

        n = len(s) + 1
        # checked[i] is  means the prefix from 0 to i (inclusive) can be represented by dict
        dp = [n] * n

        # Assuming empty string can be dict-represented
        dp[0] = 0
        # for each position in checked starting 1
        for i in range(1, len(s)+1):
            # calculate its prefix from 0 to j (inclusive) and segment from j to i (inclusive)
            for j in range(0, i):
                if s[j:i] in wordDict:
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[n]