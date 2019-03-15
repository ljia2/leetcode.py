class Solution(object):
    def regionsBySlashes(self, grid):
        """
        In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

        (Note that backslash characters are escaped, so a \ is represented as "\\".)

        Return the number of regions.



        Example 1:

        Input:
        [
          " /",
          "/ "
        ]
        Output: 2
        Explanation: The 2x2 grid is as follows:

        Example 2:

        Input:
        [
          " /",
          "  "
        ]
        Output: 1
        Explanation: The 2x2 grid is as follows:

        Example 3:

        Input:
        [
          "\\/",
          "/\\"
        ]
        Output: 4
        Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
        The 2x2 grid is as follows:

        Example 4:

        Input:
        [
          "/\\",
          "\\/"
        ]
        Output: 5
        Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
        The 2x2 grid is as follows:

        Example 5:

        Input:
        [
          "//",
          "/ "
        ]
        Output: 3
        Explanation: The 2x2 grid is as follows:

        Note:

        1 <= grid.length == grid[0].length <= 30
        grid[i][j] is either '/', '\', or ' '.
        :type grid: List[str]
        :rtype: int

        each cell is assumed split into 0, 1, 2, 3 triangle regions.
        their index is r * cols + c + 0/1/2/3 according.



        if cell is ' ': merge all regions.
        if cell is '/' merge 0, 3 and 1, 2 into two regions.
        if cell is '\\' merge 0, 1 and 2, 3 into two regions

        iterate for each region, union with its possible neighbor.
        we only consider the following four conditions:
                         (r, c, 0) with (r-1, c-1, 2).
                         (r, c, 1) with (r, c+1, 3)
                         (r, c, 2) with (r+1, c, 0)
                         (r, c, 3) with (r, c-1, 1).

        Then find the connected components by union find.

        """

        if not grid or not grid[0]:
            return 0

        n = len(grid)
        grid = [list(r) for r in grid]

        parents = [i for i in range(4*n*n)]
        sizes = [1]*4*n*n

        for r in range(n):
            for c in range(n):
                if grid[r][c] == " ":
                    self.union(parents, sizes, 4*(r*n + c), 4*(r*n + c) + 1)
                    self.union(parents, sizes, 4*(r*n + c), 4*(r*n + c) + 2)
                    self.union(parents, sizes, 4*(r*n + c), 4*(r*n + c) + 3)
                elif grid[r][c] == "\\":
                    self.union(parents, sizes, 4*(r*n + c), 4*(r*n + c) + 1)
                    self.union(parents, sizes, 4*(r*n + c) + 2, 4*(r*n + c) + 3)
                elif grid[r][c] == "/":
                    self.union(parents, sizes, 4*(r*n + c), 4*(r*n + c) + 3)
                    self.union(parents, sizes, 4*(r*n + c) + 1, 4*(r*n + c) + 2)

                if r > 0:
                    self.union(parents, sizes, 4*(r*n + c), 4*((r-1)*n + c) + 2)
                if r < n - 1:
                    self.union(parents, sizes, 4*(r*n + c) + 2, 4*((r+1)*n + c))
                if c > 0:
                    self.union(parents, sizes, 4*(r*n + c) + 3, 4*(r*n + c - 1) + 1)
                if c < n - 1:
                    self.union(parents, sizes, 4*(r*n + c) + 1, 4*(r*n + c + 1) + 3)

        components = set()
        for i in range(4*n*n):
            pi = self.find(parents, i)
            if pi not in components:
                components.add(pi)
        return len(components)

    def union(self, parents, sizes, i, j):
        pi = self.find(parents, i)
        pj = self.find(parents, j)
        if pi == pj:
            return
        if sizes[pi] > sizes[pj]:
            pi, pj = pj, pi
        parents[pi] = pj
        sizes[pj] += sizes[pi]
        return

    def find(self, parents, i):
        while i != parents[i]:
            parents[i] = parents[parents[i]]
            i = parents[i]
        return i


s = Solution()
print(s.regionsBySlashes([" /", "/ "]))


