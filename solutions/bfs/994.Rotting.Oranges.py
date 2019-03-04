class Solution(object):
    def orangesRotting(self, grid):
        """
        In a given grid, each cell can have one of three values:

        the value 0 representing an empty cell;
        the value 1 representing a fresh orange;
        the value 2 representing a rotten orange.
        Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

        Return the minimum number of minutes that must elapse until no cell has a fresh orange.
        If this is impossible, return -1 instead.

        Example 1:
        Input: [[2,1,1],[1,1,0],[0,1,1]]
        Output: 4

        Example 2:
        Input: [[2,1,1],[0,1,1],[1,0,1]]
        Output: -1
        Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten,
        because rotting only happens 4-directionally.

        Example 3:
        Input: [[0,2]]
        Output: 0
        Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

        Note:
        1 <= grid.length <= 10
        1 <= grid[0].length <= 10
        grid[i][j] is only 0, 1, or 2.

        :type grid: List[List[int]]
        :rtype: int

        typical bfs over the grid.


        """
        if not grid or not grid[0]:
            return 0

        q = []
        visited = set()
        fresh_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        if not q:
            return 0 if fresh_count == 0 else -1

        if fresh_count == 0:
            return 0

        minutes = 0
        while q:
            size = len(q)
            while size > 0:
                r, c = q.pop(0)
                size -= 1

                # when visiting them, they got rotten.
                if grid[r][c] == 1:
                    fresh_count -= 1
                if fresh_count == 0:
                    return minutes

                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] == 0:
                        continue
                    if (nr, nc) in visited:
                        continue

                    visited.add((nr, nc))
                    q.append((nr, nc))
            minutes += 1

        return -1

s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(s.orangesRotting([[1],[2],[2]]))

