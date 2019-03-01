from heapq import heappush, heappop

class Solution:
    def minAbbreviation(self, target, dictionary):
        """
        A string such as "word" contains the following abbreviations:

        ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
        Given a target string and a set of strings in a dictionary,
        find an abbreviation of this target string with the smallest possible length
        such that it does not conflict with abbreviations of the strings in the dictionary.

        Each number or letter in the abbreviation is considered length = 1.
        For example, the abbreviation "a32bc" has length = 4.

        Note:

        In the case of multiple answers as shown in the second example below, you may return any one of them.
        Assume length of target string = m, and dictionary size = n.
        You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.

        Examples:

        "apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

        "apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").

        :type target: str
        :type dictionary: List[str]
        :rtype: str

        backtracking to get all abbreviations of a word.
        just check abbreviations of target with all abbreviations of dictionary words.

        """

        if not dictionary:
            return str(len(target))

        abbr_set = set()
        for w in dictionary:
            if len(w) != len(target):
                continue
            abbrs = self.generate_abbr(w)
            for abbr in abbrs:
                abbr_set.add(abbr)

        abbr_pq = []
        abbrs = self.generate_abbr(target)
        for abbr in abbrs:
            l = len(abbr)
            heappush(abbr_pq, (l, abbr))

        while abbr_pq:
            _, abbr = heappop(abbr_pq)
            if abbr not in abbr_set:
                return abbr

    def generate_abbr(self, word):
        ans = []
        cur_abbr = ""
        self.dfs(word, 0, 0, cur_abbr, ans)
        return ans

    def dfs(self, word, pos, count, cur_abbr, ans):
        if pos == len(word):
            abbr = (cur_abbr + str(count)) if count > 0 else cur_abbr
            ans.append(abbr)
            return

        # abbreviate the char at pos
        self.dfs(word, pos+1, count+1, cur_abbr, ans)
        # not abbreviate the char at pos; update the current abbreviation
        new_cur_abbr = (cur_abbr + str(count) + word[pos]) if count > 0 else (cur_abbr + word[pos])
        # reset count = 0 and keep search the remaining.
        self.dfs(word, pos+1, 0, new_cur_abbr, ans)
        return

s = Solution()
print(s.minAbbreviation("usaandchinaarefriends", []))