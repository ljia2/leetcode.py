class Solution:
    def gameOfLife(self, board):
        """
        According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

        Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
        Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules
        (taken from the above Wikipedia article):

        Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population..
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        Write a function to compute the next state (after one update) of the board given its current state.
        The next state is created by applying the above rules simultaneously to every cell in the current state,
        where births and deaths occur simultaneously.

        Example:

        Input:
        [
          [0,1,0],
          [0,0,1],
          [1,1,1],
          [0,0,0]
        ]
        Output:
        [
          [0,0,0],
          [1,0,1],
          [0,1,1],
          [0,1,0]
        ]
        Follow up:

        Could you solve it in-place?

        Remember that the board needs to be updated at the same time:
        You cannot update some cells first and then use their updated values to update other cells.
        In this question, we represent the board using a 2D array.
        In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array.
        How would you address these problems?

        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.

        if a live cell to dead, mark it with 2 in place; do not mess up the future calculation.
        if a dead cell to live, mark it with -2 in place; do not mess up the future calculation.
        """
        if not board or not board[0]:
            return

        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.liveCell(board, r, c):
                    if board[r][c] == 0:
                        board[r][c] = -2
                else:
                    if board[r][c] == 1:
                        board[r][c] = 2
        # flip back 2 or -2 to 0 or 1
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == -2:
                    board[r][c] = 1
                elif board[r][c] == 2:
                    board[r][c] = 0

    def liveCell(self, board, r, c):
        dead_cnt = 0
        live_cnt = 0
        # test neighbors by range. note the inclusive of range.
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                    continue
                if i == r and j == c:
                    continue

                if board[i][j] <= 0:
                    dead_cnt += 1
                elif board[i][j] >= 0:
                    live_cnt += 1

        print(f"""given ${r}, ${c}, checking ${live_cnt}, ${dead_cnt}""")
        if board[r][c] == 1 and live_cnt < 2:
            return False
        elif board[r][c] == 1 and (live_cnt == 2 or live_cnt == 3):
            return True
        elif board[r][c] == 1 and live_cnt > 3:
            return False
        elif board[r][c] == 0 and live_cnt == 3:
            return True
        return board[r][c] == 1


s = Solution()
board = [[0,1,0],
         [0,0,1],
         [1,1,1],
         [0,0,0]]
s.gameOfLife(board)
print(board)