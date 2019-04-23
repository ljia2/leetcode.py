class Trie:
    def __init__(self):
        self.next = dict()
        self.word = None


class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
        A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

        Example:

        Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

        Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

        Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
         "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
        "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
        Note:

        The number of elements of the given array will not exceed 10,000
        The length sum of elements in the given array will not exceed 600,000.
        All the input string will only include lower case letters.
        The returned elements order does not matter.


        :type words: List[str]
        :rtype: List[str]
        """

        if not words:
            return []

        root = self.buildTrieTree(words)

        ans = []
        for word in words:
            if self.dfs(root, word, root, 0):
                ans.append(word)
        return ans

    def buildTrieTree(self, words):
        root = Trie()
        for w in words:
            p = root
            for c in w:
                if c not in p.next.keys():
                    p.next[c] = Trie()
                p = p.next[c]
            p.word = w
        return root

    def dfs(self, root, word, node, l):
        # must reach a word node but != give word
        if l == len(word):
            if node.word:
                # make sure do not return True on the given word. 
                return node.word != word
            else:
                return False

        if word[l] not in node.next.keys():
            # if the character on level l is not found in the node.next
            # but if node is word node, restart dfs from root and l
            if node.word:
                return self.dfs(root, word, root, l)
            else:
                return False

        if not node.word:
            return self.dfs(root, word, node.next[word[l]], l + 1)
        else:
            # keep search among the node.next or
            # if a prefix is found, restart dfs from root (when restart search from root, level l does not change).
            return self.dfs(root, word, node.next[word[l]], l + 1) or self.dfs(root, word, root, l)


s = Solution()
print(s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))