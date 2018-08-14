class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return

        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.liveCell(board, r, c):
                    if board[r][c] == 0:
                        board[r][c] = -2
                else:
                    if board[r][c] == 1:
                        board[r][c] = 2
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
        for i in range(max(r-1, 0), min(r+2, len(board))):
            for j in range(max(c-1, 0), min(c+2, len(board[0]))):
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

def main():
    s = Solution()
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    s.gameOfLife(board)
    print(board)

if __name__ == "__main__":
    main()