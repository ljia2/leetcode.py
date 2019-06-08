class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

        Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

        The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.



        Example 1:

        Input 1: a maze represented by a 2D array

        0 0 1 0 0
        0 0 0 0 0
        0 0 0 1 0
        1 1 0 1 1
        0 0 0 0 0

        Input 2: start coordinate (rowStart, colStart) = (0, 4)
        Input 3: destination coordinate (rowDest, colDest) = (4, 4)

        Output: true

        Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

        Example 2:

        Input 1: a maze represented by a 2D array

        0 0 1 0 0
        0 0 0 0 0
        0 0 0 1 0
        1 1 0 1 1
        0 0 0 0 0

        Input 2: start coordinate (rowStart, colStart) = (0, 4)
        Input 3: destination coordinate (rowDest, colDest) = (3, 2)

        Output: false

        Explanation: There is no way for the ball to stop at the destination.



        Note:

        There is only one ball and one destination in the maze.
        Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
        The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
        The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool

        1) dfs from start to end. use (r, c, dir) to mark visited.
        2) special rule: if nr, nc is not wal, keep the direction otherwise expand one of four directions

        """
        if maze[destination[0]][destination[1]] == 1:
            return False
        # mark the location of ball stops before
        visited = set()
        sr, sc = start
        visited.add((sr, sc))

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = self.stop(maze, sr, sc, dr, dc)
            if self.dfs(maze, destination, nr, nc, visited):
                return True
        return False

    def dfs(self, maze, des, r, c, visited):
        if (r, c) in visited:
            return False

        # record the cell and its direction
        visited.add((r, c))

        # stops the destination.
        if des[0] == r and des[1] == c:
            return True

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = self.stop(maze, r, c, dr, dc)
            if self.dfs(maze, des, nr, nc, visited):
                return True
        return False

    def stop(self, maze, cr, cc, dr, dc):
        nr, nc = cr + dr, cc + dc
        while 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] == 0:
            nr, nc = nr + dr, nc + dc
        # ball hitting wall at nr, nc and  thus stop at (nr - dr, nc - dc).
        return nr - dr, nc - dc


s = Solution()
print(s.hasPath([ [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4]))
print(s.hasPath([ [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [3, 2]))
