class Solution:
    def shortestPathAllKeys(self, grid):
        """
        We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point,
        ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

        We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.
        We cannot walk outside the grid, or walk into a wall.
        If we walk over a key, we pick it up.
        We can't walk over a lock unless we have the corresponding key.

        For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.
        This means that there is exactly one key for each lock, and one lock for each key;
        and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

        Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.

        Example 1:

        Input: ["@.a.#","###.#","b.A.B"]
        Output: 8
        Example 2:

        Input: ["@..aA","..B#.","....b"]
        Output: 6


        Note:

        1 <= grid.length <= 30
        1 <= grid[0].length <= 30
        grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
        The number of keys is in [1, 6].
        Each key has a different letter and opens exactly one lock.
        
        :type grid: List[str]
        :rtype: int

        shortest path variation, we can revisit nodes after the keys state if different

        state: (r, c, keysets)

        T: O(m * n * 2^keys)
        S: O(m * n * 2^keys)
        """
        # binary representation of how many keys
        key_count = 0
        row_num = len(grid)
        col_num = len(grid[0])
        sr, sc = (None, None)
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '@':
                    sr, sc = r, c
                elif 'a' <= grid[r][c] <= 'z':
                    key_count |= 1 << (ord(grid[r][c]) - ord('a'))
        # auxiliary array for directional search
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # initialize queue of state of bfs for shortest path
        qe = [(sr, sc, 0)]
        # initialize visited with start position and what keys collected.
        visited = set()
        visited.add((sr, sc, 0))

        moves = 0
        while qe:
            size = len(qe)
            while size > 0:
                # use binary bits to denote which keys is collected. 'a' is 000001, 'b' is 000010, c = '000100'
                r, c, collected_keys = qe.pop(0)
                size -= 1

                if collected_keys == key_count:
                    return moves

                # delta row and delta col
                for (dr, dc) in dirs:
                    nr, nc = r + dr, c + dc
                    # early pruning for out of boundary and wall
                    if nr < 0 or nr >= row_num or nc < 0 or nc >= col_num or grid[nr][nc] == '#':
                        continue

                    # early pruning for blocked by lock
                    if 'A' <= grid[nr][nc] <= 'Z':
                        key = grid[nr][nc].lower()

                        # bitwise & operation to determine whether key is picked already or not.
                        # if the key is not collected.
                        if collected_keys & (1 << (ord(key) - ord('a'))) == 0:
                            continue

                    # early pruning for visited cell
                    if (nr, nc, collected_keys) in visited:
                        continue

                    if 'a' <= grid[nr][nc] <= 'z':
                        qe.append((nr, nc, collected_keys | (1 << (ord(grid[nr][nc]) - ord('a')))))
                        visited.add((nr, nc, collected_keys | (1 << (ord(grid[nr][nc]) - ord('a')))))
                    else:
                        qe.append((nr, nc, collected_keys))
                        visited.add((nr, nc, collected_keys))
            moves += 1

        return -1

s = Solution()
print(s.shortestPathAllKeys(["@.a.#","###.#","b.A.B"]))
print(s.shortestPathAllKeys(["@..aA","..B#.","....b"]))
print(s.shortestPathAllKeys(["@...a",".###A","b.BCc"]))