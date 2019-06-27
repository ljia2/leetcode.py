class Solution(object):
    def wallsAndGates(self, rooms):
        """
        You are given a m x n 2D grid initialized with these three possible values.

        -1 - A wall or an obstacle.
        0 - A gate.
        INF - Infinity means an empty room.
        We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
        Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

        Example:

        Given the 2D grid:

        INF  -1  0  INF
        INF INF INF  -1
        INF  -1 INF  -1
          0  -1 INF INF
        After running your function, the 2D grid should be:

          3  -1   0   1
          2   2   1  -1
          1  -1   2  -1
          0  -1   3   4
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.

        nearest gate -> bfs from gates.
        """
        if not rooms or not rooms[0]:
            return

        row, col = len(rooms), len(rooms[0])

        # initialize with all the gates
        queue = []
        visited = set()
        for r in range(row):
            for c in range(col):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        # bfs from all rooms.
        step = 0
        while queue:
            size = len(queue)
            while size > 0:
                r, c = queue.pop(0)
                size -= 1

                rooms[r][c] = step

                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if nr < 0 or nc < 0 or nr >= row or nc >= col or rooms[nr][nc] < 0 or (nr, nc) in visited:
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            step += 1
        return


s = Solution()
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
s.wallsAndGates(rooms)
print(rooms)