class Solution:
    def shortestBridge(self, A):
        """
        In a given 2D binary array A, there are two islands.
        (An island is a 4-directionally connected group of 1s not connected to any other 1s.)
        Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
        Return the smallest number of 0s that must be flipped.
        (It is guaranteed that the answer is at least 1.)



        Example 1:
        Input: [[0,1],[1,0]]
        Output: 1

        Example 2:
        Input: [[0,1,0],[0,0,0],[0,0,1]]
        Output: 2

        Example 3:
        Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
        Output: 1

        Note:

        1 <= A.length = A[0].length <= 100
        A[i][j] == 0 or A[i][j] == 1

        :type A: List[List[int]]
        :rtype: int

        first use DFS to mark islands

        then use BFS to find the shortest path to connect two islands

        """
        rcount = len(A)
        ccount = len(A[0])

        island = 0
        for r in range(rcount):
            for c in range(ccount):
                if A[r][c] <= 0:
                    continue
                island += 1
                self.dfs(A, r, c, island)

        # A is marked island1 and island2 are marked with -1 and -2 respectively
        qe = []
        visited = set()
        for r in range(rcount):
            for c in range(ccount):
                if A[r][c] == -1:
                    qe.append((r, c))
                    visited.add((r, c))

        moves = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while qe:
            size = len(qe)
            while size > 0:
                r, c = qe.pop(0)
                size -= 1
                if A[r][c] == -2:
                    # use moves - 1 to denote how many 0 is flipped.
                    return moves - 1
                for dir in dirs:
                    nr, nc = r + dir[0], c + dir[1]
                    if nr < 0 or nc < 0 or nr >= rcount or nc >= ccount or A[nr][nc] == -1:
                        continue
                    if (nr, nc) in visited:
                        continue
                    qe.append((nr, nc))
                    visited.add((nr, nc))
            moves += 1
        return -1


    def dfs(self, A, r, c, island):
        if r < 0 or c < 0 or r >= len(A) or c >= len(A[0]) or A[r][c] <= 0:
            return
        # flip to negative island to mark island index and visited
        A[r][c] = -island
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dir in dirs:
            nr, nc = r + dir[0], c + dir[1]
            self.dfs(A, nr, nc, island)
        return

s = Solution()
print(s.shortestBridge([[0,0,0,0,0,0],[0,1,0,0,0,0],[1,1,0,0,0,0],[1,1,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,0,0]]))