"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or ..
A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.


How about use Trie Tree.

"""

class TrieNode:
    def __init__(self):
        self.next = dict()
        self.word = None


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        p = self.root
        for c in word:
            if c not in p.next.keys():
                p.next[c] = TrieNode()
            p = p.next[c]
        p.word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.root, 0, word)

    def dfs(self, root, level, word):
        if level == len(word):
            return root.word

        c = word[level]
        if c != ".":
            if c not in root.next.keys():
                return False
            return self.dfs(root.next[c], level + 1, word)
        else:
            for d in root.next.keys():
                if self.dfs(root.next[d], level + 1, word):
                    return True
            return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)