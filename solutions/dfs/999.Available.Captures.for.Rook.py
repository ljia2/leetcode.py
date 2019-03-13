class Solution(object):
    def numRookCaptures(self, board):
        """
        On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops,
        and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively.
        Uppercase characters represent white pieces, and lowercase characters represent black pieces.

        The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south),
        then moves in that direction until it chooses to stop, reaches the edge of the board,
        or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

        Return the number of pawns the rook can capture in one move.



        Example 1:



        Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
        Output: 3
        Explanation:
        In this example the rook is able to capture all the pawns.
        Example 2:



        Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
        Output: 0
        Explanation:
        Bishops are blocking the rook to capture any pawn.
        Example 3:



        Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
        Output: 3
        Explanation:
        The rook can capture the pawns at positions b5, d6 and f5.


        Note:

        board.length == board[i].length == 8
        board[i][j] is either 'R', '.', 'B', or 'p'
        There is exactly one cell with board[i][j] == 'R'

        :type board: List[List[str]]
        :rtype: int


        search one direction over the board, stop when encounter a bishop, out of box or capture a pawn.


        """
        if not board or not board[0]:
            return 0

        start = None
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    start = (r, c)
                    break
        if not start:
            return 0

        r, c = start
        ans = [0]
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for step in range(1, 8):
                nr, nc = r + dr*step, c + dc*step
                if self.stop(board, nr, nc, ans):
                    break
        return ans[0]

    def stop(self, board, r, c, ans):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return True

        if board[r][c] == 'B':
            return True

        if board[r][c] == 'p':
            ans[0] += 1
            return True
        return False

s = Solution()
print(s.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))