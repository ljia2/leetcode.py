class Solution:
    def solveNQueens(self, n):
        """
        The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
        Given an integer n, return all distinct solutions to the n-queens puzzle.
        Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

        Example:

        Input: 4
        Output: [
         [".Q..",  // Solution 1
          "...Q",
          "Q...",
          "..Q."],

         ["..Q.",  // Solution 2
          "Q...",
          "...Q",
          ".Q.."]
        ]
        Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
        :type n: int
        :rtype: List[List[str]]

        Since it requires all solutions, clearly backtracking / DFS should be the answer.

        given a board of n * n, there are 2*n - 1 diags from left top to right bottom
        and another 2*n - 1 diags from right top to left bottom.

        use two arraies, diag1 and diag2 to represent these two sets

        given (x, y), it can mapped into the (x - y + n - 1) diag in diag1 and the x + y diag in diag2.

        """
        # store all possible solutions
        ans = []
        # store the availabity of columns
        columns = [True] * n
        # store the availabity of diag1
        diag1 = [True] * (2*n - 1)
        # store the availabity of diag1
        diag2 = [True] * (2*n - 1)
        self.dfs(columns, diag1, diag2, 0, n, [], ans)
        return self.conversion(n, ans)

    def available(self, n, r, c, cols, diag1, diag2):
        return cols[c] and diag1[r + c] and diag2[r - c + n - 1]

    def dfs(self, cols, diag1, diag2, r, n, sol, ans):
        if r == n:
            #### NOTE THAT backtracking must use a copy of solution!!!!!!!
            ans.append(sol.copy())
            return

        for c in range(n):
            if not self.available(n, r, c, cols, diag1, diag2):
                continue
            sol.append(c)
            cols[c] = False
            diag1[r + c] = False
            diag2[r - c + n - 1] = False
            self.dfs(cols, diag1, diag2, r + 1, n, sol, ans)
            sol.remove(c)
            cols[c] = True
            diag1[r + c] = True
            diag2[r - c + n - 1] = True
        return

    def conversion(self, n, sols):
        ans = []
        for sol in sols:
            new_sol = []
            for c in sol:
                s = ["."] * c + ["Q"] + ["."] * (n - c - 1)
                new_sol.append("".join(s))
            ans.append(new_sol)
        return ans

s = Solution()
print(s.solveNQueens(8))