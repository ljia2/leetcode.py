class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves.
        The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

        A chess knight has 8 possible moves it can make, as illustrated below.
        Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


        Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

        The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.


        Example:

        Input: 3, 2, 0, 0
        Output: 0.0625
        Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
        From each of those positions, there are also two moves that will keep the knight on the board.
        The total probability the knight stays on the board is 0.0625.


        Note:

        N will be between 1 and 25.
        K will be between 0 and 100.
        The knight always initially starts on the board.
        
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float

        dp[K][i][j] is probability of a knight moves the (i+1, j+1) in grid after K moves


        """
        # if no move, 100% staying on board.
        if K <= 0:
            return 1.0

        dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(K+1)]
        dp[0][r][c] = 1

        dirs = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
        for k in range(1, K+1):
            for x in range(N):
                for y in range(N):
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx >= N or ny >= N:
                            continue
                        # update the probability from last position (x, y) to (nx, ny)
                        dp[k][nx][ny] += dp[k-1][x][y] * 0.125

        ans = 0
        for x in range(N):
            for y in range(N):
                ans += dp[K][x][y]
        return ans

s = Solution()
print(s.knightProbability(3, 2, 0, 0))