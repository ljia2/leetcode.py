class Solution(object):
    def minFallingPathSum(self, A):
        """
        Given a square array of integers A, we want the minimum sum of a falling path through A.

        A falling path starts at any element in the first row, and chooses one element from each row.
        The next row's choice must be in a column that is different from the previous row's column by at most one.

        Example 1:

        Input: [[1,2,3],[4,5,6],[7,8,9]]
        Output: 12
        Explanation:
        The possible falling paths are:
        [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
        [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
        [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
        The falling path with the smallest sum is [1,4,7], so the answer is 12.


        Note:

        1 <= A.length == A[0].length <= 100
        -100 <= A[i][j] <= 100

        :type A: List[List[int]]
        :rtype: int


        minPath[i][j] is the minimum sum of falling path ending at A[i][j]

        mp[i][j] = min(mp[i-1][j-1], mp[i-1][i], mp[i-1][j+1]) + A[i][j]

        ans = min(mp[-1])
        """
        m, n = len(A), len(A[0])

        mp = [[100*100*100] * n for _ in range(m)]

        for j in range(n):
            mp[0][j] = A[0][j]

        for i in range(1, m):
            for j in range(n):
                for nj in [j-1, j, j+1]:
                    if nj < 0 or nj >= n:
                        continue
                    mp[i][j] = min(mp[i][j], mp[i-1][nj] + A[i][j])
        return min(mp[m-1])


s = Solution()
print(s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))