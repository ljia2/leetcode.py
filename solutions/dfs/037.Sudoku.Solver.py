import collections

class Solution(object):
    def solveSudoku(self, board):
        """
        Write a program to solve a Sudoku puzzle by filling the empty cells.

        A sudoku solution must satisfy all of the following rules:

        Each of the digits 1-9 must occur exactly once in each row.
        Each of the digits 1-9 must occur exactly once in each column.
        Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
        Empty cells are indicated by the character '.'.


        A sudoku puzzle...

        ...and its solution numbers marked in red.

        Note:

        The given board contain only digits 1-9 and the character '.'.
        You may assume that the given Sudoku puzzle will have a single unique solution.
        The given board size is always 9x9.

        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.

        typical dfs over board.

        """
        found = [False]
        unassigned_cells = self.unassigned(board)
        self.solve(board, unassigned_cells, found)

    def solve(self, board, unassigned_cells, found):
        if not unassigned_cells:
            found[0] = True
            return
        l = len(unassigned_cells)
        for i in range(l):
            # try to fill in (r, c)
            r, c = unassigned_cells[i]
            for num in range(1, 10):
                if self.is_safe(board, r, c, str(num)):
                    board[r][c] = str(num)
                    unassigned_cells.popleft()
                    self.solve(board, unassigned_cells, found)
                    if found[0]:
                        return
                    board[r][c] = "."
                    unassigned_cells.appendleft((r,c))
            return
        return

    def unassigned(self, board):
        ans = collections.deque()
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    ans.append((r, c))
        return ans

    def is_safe(self, board, r, c, num):
        return self.is_row_safe(board, r, num) and self.is_col_safe(board, c, num) and self.is_square_safe(board, r, c, num)

    def is_row_safe(self, board, r, num):
        for c in range(9):
            if board[r][c] == num:
                return False
        return True

    def is_col_safe(self, board, c, num):
        for r in range(9):
            if board[r][c] == num:
                return False
        return True

    def is_square_safe(self, board, r, c, num):
        box_r = r - r % 3
        box_c = c - c % 3
        for i in range(box_r, box_r + 3):
            for j in range(box_c, box_c + 3):
                if board[i][j] == num:
                    return False
        return True



s = Solution()
board=[["5","3",".",".","7",".",".",".","."],
       ["6",".",".","1","9","5",".",".","."],
       [".","9","8",".",".",".",".","6","."],
       ["8",".",".",".","6",".",".",".","3"],
       ["4",".",".","8",".","3",".",".","1"],
       ["7",".",".",".","2",".",".",".","6"],
       [".","6",".",".",".",".","2","8","."],
       [".",".",".","4","1","9",".",".","5"],
       [".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
print(board)
