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

        1) build a prefix dictionary where key is suffix and value is the list of words with the suffix
        2) dfs over prefix dictionary with early pruning by suffix.

        note that word square is symmetric.

        """

        if not words:
            return []

        prefix_dict = defaultdict(set)
        for w in words:
            for i in range(1, len(w)+1):
                prefix = w[:i]
                prefix_dict[prefix].add(w)

        prefix_dict[""] = set(words)
        word_length = len(words[0])
        ans = []
        word_square = []
        self.dfs(0, word_length, prefix_dict, word_square, ans)

        return ans

    def dfs(self, level, target_level, prefix_dict, word_square, ans):
        if level == target_level:
            ans.append(word_square.copy())
            return

        # build up the prefix of the ith word in word_square
        prefix = ""
        for w in word_square:
            prefix += w[level]

        for w in prefix_dict[prefix]:
            word_square.append(w)
            self.dfs(level+1, target_level, prefix_dict, word_square, ans)
            word_square.pop()
        return




s = Solution()
print(s.wordSquares(["area","lead","wall","lady","ball"]))
print(s.wordSquares(["abat","baba","atan","atal"]))


#############
import copy

class Trie:
    def __init__(self):
        self.next = dict()
        self.word = None

class TrieSolution:
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

        """
        if not words:
            return []

        root = self.buildTrie(words)
        ans = []
        for word in words:
            self.search(root, 1, len(word), [word], ans)
        return ans

    def search(self, root, level, target, ws, ans):
        if level == target:
            ans.append(copy.copy(ws))
            return

        prefix = ""
        for w in ws:
            prefix += w[level]

        words = self.findByPrefix(root, prefix)
        for w in words:
            if len(w) != target:
                continue
            ws.append(w)
            self.search(root, level + 1, target, ws, ans)
            ws.pop()
        return

    def buildTrie(self, words):
        root = Trie()
        for word in words:
            p = root
            for c in word:
                if c not in p.next.keys():
                    p.next[c] = Trie()
                p = p.next[c]
            p.word = word
        return root

    def findByPrefix(self, root, prefix):
        p = root
        for c in prefix:
            if c in p.next.keys():
                p = p.next[c]
            else:
                return []
        # find all words with the given prefix
        ans = [] if not p.word else [p.word]
        self.dfs(p, ans)
        return ans

    def dfs(self, root, ans):
        if root.word:
            ans.append(root.word)
            return

        for c in root.next.keys():
            self.dfs(root.next[c], ans)
        return

s = TrieSolution()
print(s.wordSquares(["area","lead","wall","lady","ball"]))
print(s.wordSquares(["abat","baba","atan","atal"]))