class DPSolution(object):
    def wordBreak(self, s, wordDict):
        """

        Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

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
        """
        if s is None or s == "":
            return []

        # checked[i] is True means the prefix from 0 to i (inclusive) can be represented by dict
        valid_expressions = [False] * (len(s) + 1)
        # Assuming empty string can be dict-represented
        valid_expressions[0] = True
        # for each position in checked starting 1
        for i in range(1, len(s)+1):
            # calculate its prefix from 0 to j (inclusive) and segment from j to i (inclusive)
            for j in range(0, i):
                if valid_expressions[j] and s[j:i] in wordDict:
                    """
                    if the prefix from 0 to j (inclusive) is dict-represetned and segment from j to i (inclusive) are in dict and
                    then the prefix from 0 to i (inclusive) is dict-represented
                    """
                    valid_expressions[i] = True
                    break

        if valid_expressions[len(s)]:
            # to fix memory issue, only proceed when s is a valid expression
            explored_expressions = {0: []}
            for i in range(1, len(s)+1):
                i_results = []
                for j in range(0, i):
                    if j in explored_expressions.keys() and s[j:i] in wordDict:
                        if explored_expressions[j]:
                            for e in explored_expressions[j]:
                                i_results.append(e + " " + s[j:i])
                        else:
                            i_results.append(s[j:i])
                if i_results:
                    explored_expressions[i] = i_results
            if len(s) in explored_expressions.keys():
                return explored_expressions[len(s)]
            else:
                return []
        else:
            return []





def main():
    s = DPSolution()
    results = s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
    print(results)
    results = s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
    print(results)


if __name__ == "__main__":
    main()