class Solution(object):
    def updateMatrix(self, matrix):
        """
        Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

        The distance between two adjacent cells is 1.
        Example 1:
        Input:

        0 0 0
        0 1 0
        0 0 0
        Output:
        0 0 0
        0 1 0
        0 0 0


        Example 2:
        Input:

        0 0 0
        0 1 0
        1 1 1
        Output:
        0 0 0
        0 1 0
        1 2 1
        Note:

        The number of elements of the given matrix will not exceed 10,000.
        There are at least one 0 in the given matrix.
        The cells are adjacent in only four directions: up, down, left and right.
        
        :type matrix: List[List[int]]
        :rtype: List[List[int]]

        # find the shortest path hints the bfs; 10000 hints a linear algorithm.
        basically initialize the queue with all 0s. and expanding from these 0s to calculate 1s distance to any 0.
        T O(n)
        S O(n)
        """

        if not matrix or not matrix[0]:
            return matrix

        m, n = len(matrix), len(matrix[0])
        ans = [[float("inf")] * n for _ in range(m)]
        # initialize queue with all 0s.
        q = []
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    ans[r][c] = 0
                    q.append((r, c))
        # bfs over the matrix
        while q:
            size = len(q)
            while size > 0:
                (r, c) = q.pop(0)
                size -= 1

                for nr, nc in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
                    if nr < 0 or nc < 0 or nr >= m or nc >= n:
                        continue
                    # (nr, nc) has been visited.
                    if ans[nr][nc] <= ans[r][c] + 1:
                        continue

                    ans[nr][nc] = ans[r][c] + 1
                    q.append((nr, nc))
        return ans

s = Solution()
print(s.updateMatrix([[0, 0, 0 ],[0, 1, 0], [1, 1, 1]]))