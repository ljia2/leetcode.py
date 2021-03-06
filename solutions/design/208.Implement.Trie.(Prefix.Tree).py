"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Directly use 26 children's index to indicate the value.
        # For example, if search children[0], assuming the first char of word is 'a'.
        self.children = [None] * 26
        # indicate whether this node is a finish of an word
        self.finish = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            self.finish = True
            return

        child = self.children[ord(word[0]) - ord('a')]
        if child:
            child.insert(word[1:])
            return
        else:
            child = Trie()
            child.insert(word[1:])
            self.children[ord(word[0]) - ord('a')] = child
            return

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            return True and self.finish
        child = self.children[ord(word[0]) - ord('a')]
        if child:
            return child.search(word[1:])
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix:
            return True
        child = self.children[ord(prefix[0]) - ord('a')]
        if child:
            return child.startsWith(prefix[1:])
        else:
            return False


class Trie2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # use a dictionary to represent children where key the first char and value if another trie node.
        self.children = dict()
        # indicate whether this node is a finish of an word
        self.is_word = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            self.is_word = True
            return

        if word[0] in self.children.keys():
            self.children[word[0]].insert(word[1:])
            return
        else:
            child = Trie()
            child.insert(word[1:])
            self.children[word[0]] = child
            return

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            return True and self.is_word
        if word[0] in self.children.keys():
            return self.children[word[0]].search(word[1:])
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix:
            return True
        if prefix[0] in self.children.keys():
            return self.children[prefix[0]].startsWith(prefix[1:])
        else:
            return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)