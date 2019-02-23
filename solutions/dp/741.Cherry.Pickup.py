class Solution(object):
    def cherryPickup(self, grid):
        """
        In a N x N grid representing a field of cherries, each cell is one of three possible integers.

        0 means the cell is empty, so you can pass through;
        1 means the cell contains a cherry, that you can pick up and pass through;
        -1 means the cell contains a thorn that blocks your way.

        Your task is to collect maximum number of cherries possible by following the rules below:

        Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
        After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
        When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
        If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.

        Example 1:

        Input: grid =
        [[0, 1, -1],
         [1, 0, -1],
         [1, 1,  1]]
        Output: 5
        Explanation:
        The player started at (0, 0) and went down, down, right right to reach (2, 2).
        4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
        Then, the player went left, up, up, left to return home, picking up one more cherry.
        The total number of cherries picked up is 5, and this is the maximum possible.

        Note:

        grid is an N by N 2D array, with 1 <= N <= 50.
        Each grid[i][j] is an integer in the set {-1, 0, 1}.
        It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.

        :type grid: List[List[int]]
        :rtype: int

        a round-trip dynamtic programming

        1) a top bottom tb_dp
        2) udpate grid by tb_dp
        3) bottom up bu_dp
        4) return td_dp[n][n] + bu_dp[0][0]

        """
        if not grid:
            return 0
        n = len(grid)

        td_dp = [[0 for _ in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if grid[r][c] == -1:
                    td_dp[r][c] = -1
                else:
                    if r == c == 0:
                        td_dp[r][c] = grid[r][c]
                    elif r == 0:
                        if grid[r][c-1] == -1:
                            td_dp[r][c] = -1
                        else:
                            td_dp[r][c] = td_dp[r][c-1] + grid[r][c]
                    elif c == 0:
                        if grid[r-1][c] == -1:
                            td_dp[r][c] = -1
                        else:
                            td_dp[r][c] = td_dp[r-1][c] + grid[r][c]
                    else:
                        if td_dp[r-1][c] == td_dp[r][c-1] == -1:
                            td_dp[r][c] = -1
                        else:
                            td_dp[r][c] = max(td_dp[r-1][c], td_dp[r][c-1]) + grid[r][c]

        # there is no path from (0, 0) to (n, n)
        if td_dp[n-1][n-1] == -1:
            return 0

        r = c = n - 1
        while r >= 0 or c >= 0:
            # pick a cherry if exists
            grid[r][c] = 0
            if r > 0 and c > 0:
                if td_dp[r-1][c] > td_dp[r][c-1]:
                    r -= 1
                else:
                    c -= 1
            elif c > 0:
                c -= 1
            elif r > 0:
                r -= 1
            else:
                break

        bu_dp = [[0 for _ in range(n)] for _ in range(n)]

        for r in range(n-1, -1, -1):
            for c in range(n-1, -1, -1):
                if grid[r][c] == -1:
                    bu_dp[r][c] = -1

                if r == c == n-1:
                    bu_dp[r][c] = 0
                elif r == n - 1:
                    if bu_dp[r][c+1] == -1:
                        bu_dp[r][c] = -1
                    else:
                        bu_dp[r][c] = bu_dp[r][c+1] + grid[r][c]
                elif c == n - 1:
                    if bu_dp[r+1][c] == -1:
                        bu_dp[r][c] = -1
                    else:
                        bu_dp[r][c] = bu_dp[r+1][c] + grid[r][c]
                else:
                    if bu_dp[r+1][c] == bu_dp[r][c+1] == -1:
                        bu_dp[r][c] = -1
                    else:
                        bu_dp[r][c] = max(bu_dp[r+1][c], bu_dp[r][c+1]) + grid[r][c]

        return td_dp[n-1][n-1] + bu_dp[0][0]

s = Solution()
#print(s.cherryPickup([[0, 1, -1],[1, 0, -1],[1, 1,  1]]))
#print(s.cherryPickup([[1,1,-1],[1,-1,1],[-1,1,1]]))
print(s.cherryPickup([[1,1,1,1,1],[1,1,1,1,1],[1,1,-1,1,1],[0,-1,-1,1,1],[1,1,1,1,1]]))

"""
[[1,1,1,1,1]
,[1,1,1,1,1]
,[1,1,-1,1,1]
,[0,-1,-1,1,1]
,[1,1,1,1,1]]
"""