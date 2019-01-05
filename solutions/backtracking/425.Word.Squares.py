from collections import defaultdict
class Solution:
    def wordSquares(self, words):
        """
        Given a set of words (without duplicates), find all word squares you can build from them.

        A sequence of words forms a valid word square if the kth row and column read the exact same string,
        where 0 ≤ k < max(numRows, numColumns).

        For example, the word sequence ["ball","area","lead","lady"] forms a word square
        because each word reads the same both horizontally and vertically.

        b a l l
        a r e a
        l e a d
        l a d y

        Note:

        There are at least 1 and at most 1000 words.
        All words will have the exact same length.
        Word length is at least 1 and at most 5.
        Each word contains only lowercase English alphabet a-z.

        Example 1:

        Input:
        ["area","lead","wall","lady","ball"]

        Output:
        [
          [ "wall",
            "area",
            "lead",
            "lady"
          ],
          [ "ball",
            "area",
            "lead",
            "lady"
          ]
        ]

        Explanation:
        The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

        Example 2:

        Input:
        ["abat","baba","atan","atal"]

        Output:
        [
          [ "baba",
            "abat",
            "baba",
            "atan"
          ],
          [ "baba",
            "abat",
            "baba",
            "atal"
          ]
        ]

        Explanation:
        The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

        :type words: List[str]
        :rtype: List[List[str]]

        1) build a suffix dictionary where key is suffix and value is the list of words with the suffix
        2) dfs over suffix dictionary with early pruning by suffix.

        """

        if not words:
            return []

        suffix_dict = defaultdict(set)
        for w in words:
            for i in range(1, len(w)+1):
                suffix = w[:i]
                suffix_dict[suffix].add(w)
        suffix_dict[""] = set(words)
        word_length = len(words[0])
        ans = []
        word_square = []
        self.dfs(0, word_length, suffix_dict, word_square, ans)

        return ans

    def dfs(self, level, target_level, suffix_dict, word_square, ans):
        if level == target_level:
            ans.append(word_square.copy())
            return

        suffix = ""
        for w in word_square:
            suffix += w[level]

        for w in suffix_dict[suffix]:
            word_square.append(w)
            self.dfs(level+1, target_level, suffix_dict, word_square, ans)
            word_square.pop()
        return


s = Solution()
print(s.wordSquares(["area","lead","wall","lady","ball"]))
print(s.wordSquares(["abat","baba","atan","atal"]))