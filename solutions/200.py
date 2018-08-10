class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # edge case: grid is empty
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        num_island = 0
        explored_lands = dict()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) in explored_lands.keys():
                    continue
                if grid[r][c] == '0':
                    continue
                else:
                    # local search needs to be dictionary
                    local_explored_lands = dict()
                    self.explore_island(grid, r, c, local_explored_lands)
                    if self.new_island(explored_lands, local_explored_lands):
                        num_island += 1
                    # need to update explored_lands with local_update_lands
                    explored_lands.update(local_explored_lands)
        return num_island

    def explore_island(self, grid, r, c, local_explored_lands):
        """
        :param grid:
        :param r:
        :param c:
        :param local_explored_lands:
        :return:
        Note: record explored land into local_explored_lands list then search down and right to update local_explored_lands
        """
        if grid[r][c] == '0':
            return
        else:
            local_explored_lands[(r,c)] = 1
            if r < len(grid) - 1 and c < len(grid[0]) - 1:
                self.explore_island(grid, r+1, c, local_explored_lands)
                self.explore_island(grid, r, c+1, local_explored_lands)
            elif r < len(grid) - 1:
                self.explore_island(grid, r+1, c, local_explored_lands)
            elif c < len(grid[0])-1:
                self.explore_island(grid, r, c+1, local_explored_lands)
            return

    def new_island(self, explored_lands, local_explored_lands):
        """
        :param explored_lands:
        :param local_explored_lands:
        :return: whether local_explored_lands overlap with explored_lands; yes -> old island; no -> new_island
        """
        for land in local_explored_lands.keys():
            if land in explored_lands.keys():
                return False
        return True

class Solution2:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        Note:
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        num_island = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    num_island += 1
                    self.dfs(grid, r, c)
        return num_island

    def dfs(self, grid, r, c):
        """
        :param grid:
        :param r:
        :param c:
        :return:

        """
        nr = len(grid)
        nc = len(grid[0])
        # Depth First Search
        # Flip current lands in grid to water to prevent their contributions to future island counting
        # Then DFS Top, Down, L
        grid[r][c] = '0' # flip the land to water
        if r > 0 and grid[r-1][c] == '1':
            self.dfs(grid, r-1, c)
        if r < nr - 1 and grid[r+1][c] == '1':
            self.dfs(grid, r+1, c)
        if c > 0 and grid[r][c-1] == '1':
            self.dfs(grid, r, c-1)
        if c < nc - 1 and grid[r][c+1] == '1':
            self.dfs(grid, r, c+1)

def main():
    s = Solution()
    print(s.numIslands([['0', '1', '1', '0'], ['0', '0', '1', '0'], ['1', '0', '1', '0'], ['0', '1', '1', '0']]))
    print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
    print(s.numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))

    s = Solution2()
    print(s.numIslands([['0', '1', '1', '0'], ['0', '0', '1', '0'], ['1', '0', '1', '0'], ['0', '1', '1', '0']]))
    print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
    print(s.numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))


if __name__ == "__main__":
    main()