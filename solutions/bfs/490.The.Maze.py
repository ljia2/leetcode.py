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
        r, c = len(maze), len(maze[0])

        sr, sc = start
        queue = [(sr, sc)]
        visited = set()
        visited.add((sr, sc))
        while queue:
            size = len(queue)
            while size > 0:
                cr, cc = queue.pop(0)
                size -= 1

                if destination[0] == cr and destination[1] == cc:
                    return True

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = cr + dr, cc + dc
                    while 0 <= nr < r and 0 <= nc < c and maze[nr][nc] == 0:
                        nr, nc = nr + dr, nc + dc

                    # (nr, nc) hits a wall and stop at (nr-dr, nc-dc).
                    if (nr-dr, nc-dc) not in visited:
                        visited.add((nr-dr, nc-dc))
                        queue.append((nr-dr, nc-dc))
        return False

s = Solution()
print(s.hasPath([ [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4]))
print(s.hasPath([ [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [3, 2]))
