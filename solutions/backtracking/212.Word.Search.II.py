class Solution(object): # TLE
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

        for each word,
            dfs on board with early pruning.

        """
        if not board or not board[0] or not words:
            return []

        ans = []
        wdict = set(words)
        for word in wdict:
            for r in range(len(board)):
                for c in range(len(board[0])):
                    self.dfs(board, word, 0, r, c, set(), ans)
                    if ans and ans[-1] == word:
                        break
                if ans and ans[-1] == word:
                    break
        return ans

    def dfs(self, board, word, level, r, c, used, ans):
        if level >= len(word) or board[r][c] != word[level]:
            return
        # use (r,c) at level
        used.add((r,c))

        if level + 1 == len(word):
            ans.append(word)
            return

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]):
                continue
            if (nr, nc) in used:
                continue

            self.dfs(board, word, level+1, nr, nc, used, ans)

            if ans and ans[-1] == word:
                break
        used.remove((r,c))

        return

s = Solution()
print(s.findWords([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], ["oath","pea","eat","rain"]))
print(s.findWords([['a','a','n']], ["a", "a"]))
print(s.findWords([['a','a']], ["aaa"]))
print(s.findWords([['a']], ["a"]))
print(s.findWords([["a","b"],["a","a"]], ["bab"]))
print(s.findWords([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], ["aaaaaaaaaaaa","aaaaaaaaaaaaa","aaaaaaaaaaab"]))

