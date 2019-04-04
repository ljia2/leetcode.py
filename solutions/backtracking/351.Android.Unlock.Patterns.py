class Solution:
    def numberOfPatterns(self, m, n):
        """
        Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9,
        count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.



        Rules for a valid pattern:

        Each pattern must connect at least m keys and at most n keys.
        All the keys must be distinct.
        If the line connecting two consecutive keys in the pattern passes through any other keys,
        the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
        The order of keys used matters.



        Explanation:

        | 1 | 2 | 3 |
        | 4 | 5 | 6 |
        | 7 | 8 | 9 |
        Invalid move: 4 - 1 - 3 - 6
        Line 1 - 3 passes through key 2 which had not been selected in the pattern.

        Invalid move: 4 - 1 - 9 - 2
        Line 1 - 9 passes through key 5 which had not been selected in the pattern.

        Valid move: 2 - 4 - 1 - 3 - 6
        Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

        Valid move: 6 - 5 - 4 - 1 - 9 - 2
        Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

        :type m: int
        :type n: int
        :rtype: int

        backtrack by 1) distance-one  dirs of step1 and 2) distance-two dirs of step2 (with conditions).


        """
        ans = [0]
        visited = dict()
        for r in range(0, 3):
            for c in range(0, 3):
                visited[(r, c)] = True
                self.dfs(r, c, visited, m, n, ans)
                del visited[(r, c)]
        return ans[0]

    def dfs(self, r, c, visited, m, n, ans):
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        new_dirs = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

        if m <= len(visited.keys()) <= n:
            ans[0] += 1
            return

        if len(visited.keys()) > n:
            return

        for dir in dirs:
            # try step of 1
            new_r, new_c = r + dir[0], c + dir[1]
            # out of boundary
            if new_r < 0 or new_r > 2 or new_c < 0 or new_c > 2:
                continue

            if (new_r, new_c) in visited.keys():
                # try step of 2
                new_r, new_c = new_r + dir[0], new_c + dir[1]
                # out of boundary
                if new_r < 0 or new_r > 2 or new_c < 0 or new_c > 2:
                    continue
                if (new_r, new_c) in visited.keys():
                    continue

                visited[(new_r, new_c)] = True
                self.dfs(new_r, new_c, visited, m, n, ans)
                del visited[(new_r, new_c)]
            else:
                visited[(new_r, new_c)] = True
                self.dfs(new_r, new_c, visited, m, n, ans)
                del visited[(new_r, new_c)]

        for dir in new_dirs:
            # try a hybrid move of step 1 and step 2 in row and col
            new_r, new_c = r + dir[0], c + dir[1]
            if new_r < 0 or new_r > 2 or new_c < 0 or new_c > 2:
                continue
            if (new_r, new_c) in visited.keys():
                continue

            visited[(new_r, new_c)] = True
            self.dfs(new_r, new_c, visited, m, n, ans)
            del visited[(new_r, new_c)]

        return

s = Solution()
print(s.numberOfPatterns(1, 2))