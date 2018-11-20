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
            self.dfs(board, r, 0, 'F')
            self.dfs(board, r, col-1, 'F')

        for c in range(col):
            self.dfs(board, 0, c, 'F')
            self.dfs(board, row-1, c, 'F')

        for r in range(1, row-1):
            for c in range(1, col-1):
                if board[r][c] == 'O':
                    self.dfs(board, r, c, 'X')

        for r in range(0, row):
            for c in range(0, col):
                if board[r][c] == 'F':
                    board[r][c] = 'O'
        return

    def dfs(self, board, r, c, target):
        if not self.inbound(board, r, c):
            return
        elif board[r][c] == 'X' or board[r][c] == 'F':
            return
        else:
            board[r][c] = target
            self.dfs(board, r+1, c, target)
            self.dfs(board, r-1, c, target)
            self.dfs(board, r, c+1, target)
            self.dfs(board, r, c-1, target)
            return

    # check whether (r, c) within the bound.
    def inbound(self, board, r, c):
        return -1 < r < len(board) and -1 < c < len(board[0])

s = DFSSolution()
#board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
board = [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
s.solve(board)
print(board)