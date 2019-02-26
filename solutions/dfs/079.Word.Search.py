class DFSSolution:
    def exist(self, board, word):
        """
        Given a 2D board and a word, find if the word exists in the grid.

        The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

        Example:

        board =
        [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]

        Given word = "ABCCED", return true.
        Given word = "SEE", return true.
        Given word = "ABCB", return false.

        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        typical dfs search problem.

        iterate over each cell and dfs over K steps where k is the length of given word.

        T: O(m*n*4^len(word))
        S: O(m*n)

        """
        if not board or not board[0] or not word:
            return False

        visited = [[False] * len(board[0]) for _ in range(len(board))]
        ans = [False]
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.dfs(board, word, 0, r, c, visited, ans)
                if ans[0]:
                    return ans[0]
        return False

    def dfs(self, board, word, level, r, c, visited, ans):
        # out of bound
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return

        # avoid visited cell
        if visited[r][c]:
            return

        # exceed word length
        if level >= len(word):
            return

        # do not match
        if board[r][c] != word[level]:
            return

        # find the last index
        if level == len(word) - 1:
            ans[0] = True
            return

        # start the standard dfs search.
        visited[r][c] = True
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self.dfs(board, word, level + 1, r + dr, c + dc, visited, ans)
            if ans[0]:
                return
        visited[r][c] = False
        return

