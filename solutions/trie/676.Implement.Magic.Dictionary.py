"""
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""


class Trie(object):
    def __init__(self):
        self.cdict = dict()
        self.word = None


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for word in dict:
            p = self.root
            for c in word:
                if c not in p.cdict.keys():
                    p.cdict[c] = Trie()
                p = p.cdict[c]
            p.word = word
        return

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.root, word, False, 0)

    def dfs(self, node, word, isChanged, level):
        if level == len(word):
            return node.word and isChanged

        c = word[level]
        if isChanged:
            if c not in node.cdict.keys():
                return False
            return self.dfs(node.cdict[c], word, isChanged, level + 1)
        else:
            for d in node.cdict.keys():
                if self.dfs(node.cdict[d], word, c != d, level + 1):
                    return True
        return False


obj = MagicDictionary()
obj.buildDict(["hello", "hallo", "leetcode"])
print(obj.search("hello"))
print(obj.search("hhllo"))
print(obj.search("hell"))
print(obj.search("leetcoded"))