class Solution(object):
    def shortestDistance(self, grid):
        """
        You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
        You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

        Each 0 marks an empty land which you can pass by freely.
        Each 1 marks a building which you cannot pass through.
        Each 2 marks an obstacle which you cannot pass through.
        Example:

        Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

        1 - 0 - 2 - 0 - 1
        |   |   |   |   |
        0 - 0 - 0 - 0 - 0
        |   |   |   |   |
        0 - 0 - 1 - 0 - 0

        Output: 7

        Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
                     the point (1,2) is an ideal empty land to build a house, as the total
                     travel distance of 3+3+1=7 is minimal. So return 7.
        Note:
        There will be at least one building.
        If it is not possible to build such house according to the above rules, return -1.

        :type grid: List[List[int]]
        :rtype: int


        How about BFS from buildings iteratively, use dist[i][j] accumatively records the distance to each build
        Then search the min distance from dist.

        """
        if not grid or not grid[0]:
            raise Exception("Invalid Input")

        rnum, cnum = len(grid), len(grid[0])
        visitedtimes = [[0] * cnum for _ in range(rnum)]
        dist = [[0] * cnum for _ in range(rnum)]
        buildnum = 0
        for r in range(rnum):
            for c in range(cnum):
                if grid[r][c] == 1:
                    buildnum += 1
                    # use negative buildnum to tag the grid visited by this building already
                    self.bfs(grid, r, c, visitedtimes, dist, -buildnum)


        ans = -1
        for r in range(rnum):
            for c in range(cnum):
                if visitedtimes[r][c] == buildnum:
                    if ans > 0:
                        ans = min(ans, dist[r][c])
                    else:
                        ans = dist[r][c]
        return ans

    ### Follow up: can you speed up a little bid,
    ### Only search the grid accessable by previous build.
    def bfs(self, grid, r, c, visittimes, dist, target):
        q = [(r, c)]
        visited = set()
        visited.add((r, c))
        step = 1
        while q:
            size = len(q)
            while size > 0:
                r, c = q.pop(0)
                size -= 1

                for nr, nc in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] != target or (nr, nc) in visited:
                        continue

                    # trick!!!! use target mark the cells accessible by abs(target-1) building already.
                    grid[nr][nc] = target

                    visited.add((nr, nc))
                    q.append((nr, nc))
                    dist[nr][nc] += step
                    visittimes[nr][nc] += 1

            step += 1
        return


s = Solution()
print(s.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))
print(s.shortestDistance([[1, 1]]))


