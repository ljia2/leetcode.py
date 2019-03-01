class Solution:
    def slidingPuzzle(self, board):
        """
        On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

        A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

        The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

        Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

        Examples:

        Input: board = [[1,2,3],[4,0,5]]
        Output: 1
        Explanation: Swap the 0 and the 5 in one move.
        Input: board = [[1,2,3],[5,4,0]]
        Output: -1
        Explanation: No number of moves will make the board solved.

        Input: board = [[4,1,2],[5,0,3]]
        Output: 5
        Explanation: 5 is the smallest number of moves that solves the board.

        An example path:
        After move 0: [[4,1,2],[5,0,3]]
        After move 1: [[4,1,2],[0,5,3]]
        After move 2: [[0,1,2],[4,5,3]]
        After move 3: [[1,0,2],[4,5,3]]
        After move 4: [[1,2,0],[4,5,3]]
        After move 5: [[1,2,3],[4,5,0]]

        Input: board = [[3,2,4],[1,5,0]]
        Output: 14

        Note:
        board will be a 2 x 3 array as described above.
        board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].


        :type board: List[List[int]]
        :rtype: int

        given the board and ask for shortest moves, bfs is the solution.
        The state is the board state. How to represent the state?
        we can use an string to represent the state, b[0:3] + b[1:3]
        """
        rows = len(board) # 2
        cols = len(board[0]) # 3

        start = ""
        goal = ""
        for r in range(rows):
            for c in range(cols):
                start += str(board[r][c])
                goal += str((r * cols + c + 1) % (rows * cols))

        if start == goal:
            return 0

        qe = [start]
        visited = set()
        visited.add(start)
        steps = 0
        while qe:
            size = len(qe)
            while size > 0:
                state = qe.pop(0)
                size -= 1

                if state == goal:
                    return steps

                zindex = state.index("0")
                r = zindex // cols
                c = zindex % cols

                for nr, nc in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    # generate the new state.
                    nindex = nr * cols + nc
                    nstate = list(state)
                    nstate[nindex], nstate[zindex] = nstate[zindex], nstate[nindex]
                    nstate = "".join(nstate)

                    if nstate in visited:
                        continue

                    qe.append(nstate)
                    visited.add(nstate)
            steps += 1
        return -1

s = Solution()
print(s.slidingPuzzle([[1,2,3],[4,0,5]]))