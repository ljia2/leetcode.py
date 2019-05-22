class Solution:
    def multiply(self, A, B):
        """

        Given two sparse matrices A and B, return the result of AB.

        You may assume that A's column number is equal to B's row number.

        Example:

        Input:

        A = [
          [ 1, 0, 0],
          [-1, 0, 3]
        ]

        B = [
          [ 7, 0, 0 ],
          [ 0, 0, 0 ],
          [ 0, 0, 1 ]
        ]

        Output:

             |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
        AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                          | 0 0 1 |

        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]

        """
        # result matrix
        ans = [[0] * len(B[0]) for i in range(len(A))]

        # Note: use a tuple of (row, value) to represent a sparse matrix !!!!
        sparseA = [[] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    sparseA[i].append((j, A[i][j]))

        sparseB = [[]for _ in range(len(B[0]))]
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j] != 0:
                    sparseB[j].append((i, B[i][j]))

        for i in range(len(sparseA)):
            for j in range(len(sparseB)):
                sparse_row = sparseA[i]
                sparse_col = sparseB[j]
                ans[i][j] = self.vectorDot(sparse_row, sparse_col)


        return ans
    # two pointer or event binary search if one long one short.
    # how to determine which is better: len(row) + len(col) < min(len(row)*log(len(col), len(col)*log(len(row))
    def vectorDot(self, row, col):
        i = 0
        j = 0
        ans = 0
        while i < len(row) and j < len(col):
            ci, m = row[i]
            rj, n = col[j]
            if ci == rj:
                ans += m * n
                i += 1
                j += 1
            else:
                if ci < rj:
                    i += 1
                    while i < len(row) and row[i][0] < rj:
                        i += 1
                else:
                    j += 1
                    while j < len(col) and col[j][0] < cj:
                        j += 1
        return ans



s = Solution()
print(s.multiply([[ 1, 0, 0],[-1, 0, 3]], [[ 7, 0, 0 ],[ 0, 0, 0 ],[ 0, 0, 1]]))
