"""
Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix).
It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:

Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1


Note:

words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.
"""

class TrieNode:
    def __init__(self):
        self.next = dict()
        self.windex = None

class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.pre_root = TrieNode()
        self.suf_root = TrieNode()
        self.size = len(words)
        # building prefix suffix Trie trees.
        for windex, word in enumerate(words):
            p = self.pre_root
            for c in word:
                if c not in p.next.keys():
                    p.next[c] = TrieNode()
                p = p.next[c]
            p.windex = windex

            p = self.suf_root
            for c in word[::-1]:
                if c not in p.next.keys():
                    p.next[c] = TrieNode()
                p = p.next[c]
            p.windex = windex

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        if not prefix and not suffix:
            return self.size - 1
        else:
            pans = set()
            sans = set()

            self.dfs(self.pre_root, prefix, 0, pans)
            self.dfs(self.suf_root, suffix[::-1], 0, sans)

            if not suffix:
                if not pans:
                    return -1
                else:
                    rs = list(pans)
                    rs.sort()
                    return rs[-1]
            elif not prefix:
                if not sans:
                    return -1
                else:
                    rs = list(sans)
                    rs.sort()
                    return rs[-1]
            else:
                candidates = pans.intersection(sans)
                if not candidates:
                    return -1
                else:
                    rs = list(candidates)
                    rs.sort()
                    return rs[-1]

    def dfs(self, node, prefix, level, ans):
        # find the node satisfying prefix(suffix)
        if level < len(prefix):
            c = prefix[level]
            if prefix[level] not in node.next.keys():
                return
            else:
                # only search the subtree here.
                self.dfs(node.next[c], prefix, level+1, ans)
                return

        # node is prefix/suffix with prefix
        # when index is 0, by nature it is false.
        if node.windex is not None:
            ans.add(node.windex)

        for c in node.next.keys():
            self.dfs(node.next[c], prefix, level+1, ans)
        return


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(["apple"])
# print(obj.f("a","e"))


#tests = [["","abaa"],["babbab",""],["ab","baaa"],["baaabba","b"],["abab","abbaabaa"],["","aa"],["","bba"],["","baaaaabbbb"],["ba","aabbbb"],["baaa","aabbabbb"]]
tests = [["ab","baaa"]]
obj = WordFilter(["abbbababbb","baaabbabbb","abababbaaa","abbbbbbbba","bbbaabbbaa","ababbaabaa","baaaaabbbb","babbabbabb","ababaababb","bbabbababa"])
for prefix, suffix in tests:
    print(obj.f(prefix, suffix))