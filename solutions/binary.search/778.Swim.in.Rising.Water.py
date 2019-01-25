class Solution:
    def swimInWater(self, grid):
        """
        On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

        Now rain starts to fall. At time t, the depth of the water everywhere is t.
        You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t.
        You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

        You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

        Example 1:

        Input: [[0,2],[1,3]]
        Output: 3
        Explanation:
        At time 0, you are in grid location (0, 0).
        You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

        You cannot reach point (1, 1) until time 3.
        When the depth of water is 3, we can swim anywhere inside the grid.
        Example 2:

        Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
        Output: 16
        Explanation:
         0  1  2  3  4
        24 23 22 21  5
        12 13 14 15 16
        11 17 18 19 20
        10  9  8  7  6

        The final route is marked in bold.
        We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
        Note:

        2 <= N <= 50.
        grid[i][j] is a permutation of [0, ..., N*N - 1].

        :type grid: List[List[int]]
        :rtype: int

        clearly at time t, the grid is changed where grid[i][j] = max(t, grid[i][j]).
        binary search t over [min(grid), max(grid)]

        find the minimum t when dfs from (0, 0) to (N, N).

        if reachable if dfs from (0, 0) to end,
           r = t
        else:
           l = t + 1

        O(N^2*log(Max(grid))
        """
        l = grid[0][0]
        r = len(grid)**2-1
        while l < r:
            t = (l + r) // 2

            visited = set()
            visited.add((0, 0))
            if self.dfs(grid, t, 0, 0, visited):
                r = t
            else:
                l = t + 1
        return l

    def dfs(self, grid, t, r, c, visited):
        if r == c == len(grid) - 1:
            return True
        visited.add((r, c))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            if (nr, nc) in visited:
                continue
            # from a square to another 4-directionally adjacent square if and only if
            # the elevation of both squares individually are at most t
            # when grid[r][c] <= t and grid[nr][nc] <= t, person can swim pass.
            if grid[r][c] > t or grid[nr][nc] > t:
                continue
            ans = self.dfs(grid, t, nr, nc, visited)
            if ans:
                return True
        return False

s = Solution()
print(s.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))