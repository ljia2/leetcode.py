class UnionFindSolution: # TLE
    def hitBricks(self, grid, hits):
        """
        We have a grid of 1s and 0s; the 1s in a cell represent bricks.
        A brick will not drop if and only if it is directly connected to the top of the grid,
        or at least one of its (4-way) adjacent bricks will not drop.

        We will do some erasures sequentially. Each time we want to do the erasure at the location (i, j),
        the brick (if it exists) on that location will disappear, and then some other bricks may drop because of that erasure.

        Return an array representing the number of bricks that will drop after each erasure in sequence.

        Example 1:
        Input:
        grid = [[1,0,0,0],[1,1,1,0]]
        hits = [[1,0]]
        Output: [2]
        Explanation:
        If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.

        Example 2:
        Input:
        grid = [[1,0,0,0],[1,1,0,0]]
        hits = [[1,1],[1,0]]
        Output: [0,0]
        Explanation:
        When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move.
        So each erasure will cause no bricks dropping.  Note that the erased brick (1, 0) will not be counted as a dropped brick.

        Note:
        The number of rows and columns in the grid will be in the range [1, 200].
        The number of erasures will not exceed the area of the grid.
        It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.
        An erasure may refer to a location with no brick - if it does, no bricks drop.

        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]


        reverse the order of falling and start from the ultimate graph and keep adding edges

        keep track of the number components containing the bricks connecting to the roof

        """
        ans = []
        rownum = len(grid)
        colnum = len(grid[0])

        # calculate the ultimate grid without removed bricks if exists.
        final_grid = [row.copy() for row in grid]
        for hit in hits:
            r, c = hit
            final_grid[r][c] = 0

        parents = [i for i in range(rownum * colnum)]
        sizes = [1] * rownum * colnum
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(rownum):
            for c in range(colnum):
                if final_grid[r][c] == 0:
                    continue
                for (r_delta, c_delta) in dirs:
                    newr = r + r_delta
                    newc = c + c_delta
                    if newr < 0 or newr >= rownum or newc < 0 or newc >= colnum or final_grid[newr][newc] == 0:
                        continue
                    self.union(parents, sizes, r*colnum + c, newr * colnum + newc)
        # all connected bricks must in the same components as those bricks connecting roof.
        bricks = 0
        components = set()
        for c in range(colnum):
            if final_grid[0][c] == 1:
                pc = self.find(parents, c)
                if pc not in components:
                    components.add(pc)
                    bricks += sizes[pc]

        for hindex in range(len(hits)-1, -1, -1):
            # update the grid
            r, c = hits[hindex]
            if grid[r][c] == 0:
                ans.append(0)
                continue
            # adding an edge to final_grid
            final_grid[r][c] = 1
            for (r_delta, c_delta) in dirs:
                newr = r + r_delta
                newc = c + c_delta
                if newr < 0 or newr >= rownum or newc < 0 or newc >= colnum or final_grid[newr][newc] == 0:
                    continue
                self.union(parents, sizes, r*colnum + c, newr * colnum + newc)

            # all connected bricks must in the same components as those bricks connecting roof.
            new_bricks = 0
            components = set()
            for c in range(colnum):
                if final_grid[0][c] == 1:
                    pc = self.find(parents, c)
                    if pc not in components:
                        components.add(pc)
                        new_bricks += sizes[pc]

            # excluding the removed brick
            falling_bricks = new_bricks - bricks - 1
            ans.append(falling_bricks if falling_bricks > 0 else 0)
            bricks = new_bricks
        ans.reverse()
        return ans

    def find(self, parents, s):
        while s != parents[s]:
            parents[s] = parents[parents[s]]
            s = parents[s]
        return s

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

s = UnionFindSolution()
print(s.hitBricks([[1,0,0,0],[1,1,1,0]], [[1, 0]]))