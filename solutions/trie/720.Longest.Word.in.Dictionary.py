class TrieNode:
    def __init__(self):
        self.next = dict()
        self.word = None

class Solution(object):
    def longestWord(self, words):
        """
        Given a list of strings words representing an English Dictionary,
        find the longest word in words that can be built one character at a time by other words in words.
        If there is more than one possible answer, return the longest word with the smallest lexicographical order.

        If there is no answer, return the empty string.
        Example 1:

        Input:
        words = ["w","wo","wor","worl", "world"]
        Output: "world"
        Explanation:
        The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
        Example 2:

        Input:
        words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        Output: "apple"
        Explanation:
        Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
        Note:

        All the strings in the input will only contain lowercase letters.
        The length of words will be in the range [1, 1000].
        The length of words[i] will be in the range [1, 30].

        :type words: List[str]
        :rtype: str

        1) build TrieTree with words
        2) dfs over tree to find the longest word.

        typical application of dfs based on trie.

        """

        if not words:
            return None

        root = self.buildTrieTree(words)

        # list of tuples, where
        ans = [(None, None)]
        for c in root.next.keys():
            self.dfs(root.next[c], 1, ans)
        maxl, word = ans[0]
        if not maxl:
            return ""
        else:
            return word

    def buildTrieTree(self, words):
        root = TrieNode()
        for word in words:
            p = root
            for c in word:
                if c not in p.next.keys():
                    p.next[c] = TrieNode()
                p = p.next[c]
            p.word = word
        return root

    def dfs(self, node, level, ans):
        if not node.word:
            return

        # update the longest word.
        maxl, word = ans[0]
        if not maxl or maxl < level or (maxl == level and node.word and word > node.word):
            ans[0] = (level, node.word)

        for c in node.next.keys():
            self.dfs(node.next[c], level + 1, ans)
        return
s = Solution()
#print(s.longestWord(["w","wo","wor","worl", "world"]))
print(s.longestWord(["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]))