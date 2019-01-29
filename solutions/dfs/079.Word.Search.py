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
        rnum = len(board)
        cnum = len(board[0])

        visited = [[False] * cnum for i in range(rnum)]

        for r in range(rnum):
            for c in range(cnum):
                if self.dfs(board, r, c, visited, 0, word):
                    return True
        return False

    def dfs(self, board, row, col, visited, windex, word):
        # out of bound
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]):
            return False
        # avoid visited cell
        if visited[row][col]:
            return False
        # do not match
        if board[row][col] != word[windex]:
            return False
        # find the last index
        if windex == len(word) - 1:
            return True

        visited[row][col] = True
        res = self.dfs(board, row-1, col, visited, windex+1, word) \
              or self.dfs(board, row+1, col, visited, windex+1, word) \
              or self.dfs(board, row, col-1, visited, windex+1, word) \
              or self.dfs(board, row, col+1, visited, windex+1, word)
        visited[row][col] = False
        return res

