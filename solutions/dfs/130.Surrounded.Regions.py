class DFSSolution:
    def solve(self, board):
        """
        Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

        A region is captured by flipping all 'O's into 'X's in that surrounded region.

        Example:

        X X X X
        X O O X
        X X O X
        X O X X
        After running your function, the board should be:

        X X X X
        X X X X
        X X X X
        X O X X
        Explanation:

        Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
        Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
        Two cells are connected if they are adjacent cells connected horizontally or vertically.

        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        if row <= 2 or col <= 2:
            return

        for r in range(row):
            if board[r][0] == 'O':
                self.dfs(board, r, 0, 'F')
            if board[r][col-1] == 'O':
                self.dfs(board, r, col-1, 'F')

        for c in range(col):
            if board[0][c] == 'O':
                self.dfs(board, 0, c, 'F')
            if board[row-1][c] == 'O':
                self.dfs(board, row-1, c, 'F')

        for r in range(0, row):
            for c in range(0, col):
                if board[r][c] == 'F':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    self.dfs(board, r, c, 'X')
        return

    def dfs(self, board, r, c, target):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return
        if board[r][c] == 'X' or board[r][c] == 'F':
            return
        # mark with visited by setting to target
        board[r][c] = target
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            self.dfs(board, nr, nc, target)
        return

s = DFSSolution()
board = [["O","X","X","O","X"],
         ["X","O","O","X","O"],
         ["X","O","X","O","X"],
         ["O","X","O","O","O"],
         ["X","X","O","X","O"]]
s.solve(board)
print(board)

board = [["X","O","X","X"],
         ["O","X","O","X"],
         ["X","O","X","O"],
         ["O","X","O","X"],
         ["X","O","X","O"],
         ["O","X","O","X"]]
s.solve(board)
print(board)
