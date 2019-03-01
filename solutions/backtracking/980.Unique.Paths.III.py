class Solution(object):
    def uniquePathsIII(self, grid):
        """
        On a 2-dimensional grid, there are 4 types of squares:

        1 represents the starting square.  There is exactly one starting square.
        2 represents the ending square.  There is exactly one ending square.
        0 represents empty squares we can walk over.
        -1 represents obstacles that we cannot walk over.
        Return the number of 4-directional walks from the starting square to the ending square,
        that walk over every non-obstacle square exactly once.

        Example 1:

        Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
        Output: 2
        Explanation: We have the following two paths:
        1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
        2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
        Example 2:

        Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
        Output: 4
        Explanation: We have the following four paths:
        1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
        2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
        3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
        4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
        Example 3:

        Input: [[0,1],[2,0]]
        Output: 0
        Explanation:
        There is no path that walks over every empty square exactly once.
        Note that the starting and ending square can be anywhere in the grid.

        Note:

        1 <= grid.length * grid[0].length <= 20

        :type grid: List[List[int]]
        :rtype: int

        return all pathes hints backtracking

        speciality: walking over non-obstacle exact once -> the path length is fixed.
        use this condition for early pruning.
        """

        if not grid or not grid[0]:
            return 0

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        target_length = 0
        start = end = None

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > -1:
                    target_length += 1

                if grid[r][c] == 1:
                    start = [r, c]
                elif grid[r][c] == 2:
                    end = [r, c]
        ans = [0]
        self.dfs(grid, start, end, visited, 0, target_length, ans)
        return ans[0]


    def dfs(self, grid, start, end, visited, path_length, target_length, ans):
        r, c = start
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] < 0:
            return

        if visited[r][c]:
            return

        if start == end:
            if path_length == target_length - 1:
                ans[0] += 1
            return

        visited[r][c] = True
        for nr, nc in [(r, c-1), (r, c+1), (r-1,c), (r+1,c)]:
            self.dfs(grid, [nr, nc], end, visited, path_length + 1, target_length, ans)
        visited[r][c] = False

        return

s = Solution()
print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
print(s.uniquePathsIII([[0,1],[2,0]]))