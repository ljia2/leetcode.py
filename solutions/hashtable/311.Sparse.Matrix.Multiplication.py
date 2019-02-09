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
        C = [[0] * len(B[0]) for i in range(len(A))]

        sparseA = [[] for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    sparseA[i].append((j, A[i][j]))

        for i in range(len(A)):
            sparse_row = sparseA[i]
            for (j, v) in sparse_row:
                for k in range(len(B[j])):
                    C[i][k] += v * B[j][k]
        return C


