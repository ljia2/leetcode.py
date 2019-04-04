class Solution:
    def generateAbbreviations(self, word):
        """
        Write a function to generate the generalized abbreviations of a word.

        Note: The order of the output does not matter.

        Example:

        Input: "word"
        Output:
        ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

        :type word: str
        :rtype: List[str]

        typical bracktracking problem

        for each position of a word:
            1) abbreviate it with a number (count + 1)
            2) or not to abbreviate it and keep it alphabetically.
        """

        ans = []
        cur_abbr = ""
        self.dfs(word, 0, cur_abbr, 0, ans)
        return ans

    def dfs(self, word, pos, cur_abbr, count, ans):
        if len(word) == pos:
            # Once we reach the end, append current to the result
            abbr = cur_abbr + str(count) if count > 0 else cur_abbr
            ans.append(abbr)
            return

        # Skip current position (abbreviate by count + 1), and increment count
        self.dfs(word, pos + 1, cur_abbr, count + 1, ans)
        # Include current position, and zero-out count
        new_cur_abbr = cur_abbr + (str(count) if count > 0 else '') + word[pos]
        self.dfs(word, pos + 1, new_cur_abbr, 0, ans)

        return
