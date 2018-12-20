from math import ceil
class Solution:
    def snakesAndLadders(self, board):
        """
        On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board, and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:


        You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square x, consists of the following:

        You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
        (This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations.)
        If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
        A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or ladder is board[r][c].

        Note that you only take a snake or ladder at most once per move:
        if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving.
        (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`,
        then you finish your first move at `3`, because you do not continue moving to `4`.)

        Return the least number of moves required to reach square N*N.  If it is not possible, return -1.

        Example 1:

        Input: [
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,35,-1,-1,13,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1]]
        Output: 4
        Explanation:
        At the beginning, you start at square 1 [at row 5, column 0].
        You decide to move to square 2, and must take the ladder to square 15.
        You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
        You then decide to move to square 14, and must take the ladder to square 35.
        You then decide to move to square 36, ending the game.
        It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
        Note:

        2 <= board.length = board[0].length <= 20
        board[i][j] is between 1 and N*N or is equal to -1.
        The board square with number 1 has no snake or ladder.
        The board square with number N*N has no snake or ladder.

        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)
        qe = [1]

        visited = set()
        visited.add(1)

        moves = 0
        while qe:
            size = len(qe)
            while size > 0:
                snum = qe.pop(0)
                size -= 1

                if snum == N*N:
                    return moves

                # expand by snake
                for delta in range(1, 7):
                    newsnum = snum + delta
                    if newsnum > N * N:
                        continue
                    # if there is a ladder, then use it.
                    r, c = self.square2rowcol(N, newsnum)
                    if board[r][c] != -1:
                        newsnum = board[r][c]

                    if newsnum in visited:
                        continue
                    qe.append(newsnum)
                    visited.add(newsnum)

            moves += 1
        return -1

    def square2rowcol(self, N, squarenum):
        # # roundup
        # row = N - ceil(squarenum / N)
        # mod = squarenum % N
        # if ceil(squarenum / N) % 2 == 1:
        #     col = mod - 1 if mod > 0 else N - 1
        # else:
        #     col = N - mod if mod > 0 else 0
        #
        # return row, col

        # 求商：quot = a // b, 求余数： rem = a % b
        quot, rem = divmod(squarenum-1, N)
        # 因为是左下角开始，所以是减去
        row = N - 1 - quot
        # 确定列
        col = rem if row%2 != N%2 else N - 1 - rem
        return row, col

s = Solution()
#print(s.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
#print(s.snakesAndLadders([[-1,-1],[-1,3]]))
print(s.snakesAndLadders([[-1,-1,-1,46,47,-1,-1,-1],[51,-1,-1,63,-1,31,21,-1],[-1,-1,26,-1,-1,38,-1,-1],[-1,-1,11,-1,14,23,56,57],[11,-1,-1,-1,49,36,-1,48],[-1,-1,-1,33,56,-1,57,21],[-1,-1,-1,-1,-1,-1,2,-1],[-1,-1,-1,8,3,-1,6,56]]))