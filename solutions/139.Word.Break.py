class DPSolution:
    # DP Solution
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
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
                    if the prefix from 0 to j (inclusive) is dict-represetned and segment from j to i (inclusive) are in dict and
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