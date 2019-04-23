class TrieNode:
    def __init__(self):
        self.dic = dict()
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        """
        Given a 2D board and a list of words from the dictionary, find all words in the board.

        Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
        The same letter cell may not be used more than once in a word.

        Example:

        Input:
        words = ["oath","pea","eat","rain"] and board =
        [
          ['o','a','a','n'],
          ['e','t','a','e'],
          ['i','h','k','r'],
          ['i','f','l','v']
        ]

        Output: ["eat","oath"]
        Note:
        You may assume that all inputs are consist of lowercase letters a-z.

        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]

        Tire tree use index words

        for each word,
            dfs on board with early pruning.


        """
        if not board or not board[0] or not words:
            return []
        root = self.buildTireTree(words)
        ans = []
        used = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.dfs(board, r, c, root, used, ans)
        return ans

    # Imfortant! How to Build TireTree!!!
    def buildTireTree(self, words):
        root = TrieNode()
        for word in words:
            p = root
            for c in word:
                if c not in p.dic.keys():
                    p.dic[c] = TrieNode()
                p = p.dic[c]
            p.word = word
        return root

    def dfs(self, board, r, c, node, used, ans):
        # out of bound
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return

        # (r,c) location has been visited.
        if used[r][c]:
            return

        chr = board[r][c]
        if chr not in node.dic.keys():
            return

        node = node.dic[chr]

        # find a word matching.
        if node.word:
            ans.append(node.word)
            # avoid duplication
            node.word = None

        # keep search guided by Trie
        # (r,c) at level
        used[r][c] = True
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            self.dfs(board, nr, nc, node, used, ans)
        used[r][c] = False
        return

s = Solution()
print(s.findWords([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], ["oath","pea","eat","rain"]))
print(s.findWords([['a','a','n']], ["a", "a"]))
print(s.findWords([['a','a']], ["aaa"]))
print(s.findWords([['a']], ["a"]))
print(s.findWords([["a","b"],["a","a"]], ["bab"]))
print(s.findWords([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], ["aaaaaaaaaaaa","aaaaaaaaaaaaa","aaaaaaaaaaab"]))

