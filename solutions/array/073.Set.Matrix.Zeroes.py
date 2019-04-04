class Solution:
    def setZeroes(self, matrix):
        """
        Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

        Example 1:

        Input:
        [
          [1,1,1],
          [1,0,1],
          [1,1,1]
        ]
        Output:
        [
          [1,0,1],
          [0,0,0],
          [1,0,1]
        ]
        Example 2:

        Input:
        [
          [0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]
        ]
        Output:
        [
          [0,0,0,0],
          [0,4,5,0],
          [0,3,1,0]
        ]

        Follow up:

        A straight forward solution using O(mn) space is probably a bad idea.
        A simple improvement uses O(m + n) space, but still not the best solution.
        Could you devise a constant space solution?


        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        just whenever encourter a zero, mark row and column None. (instead of 0 to aviod looping).
        since each entry only visits once (actually twice).

        reset None to 0 for the second pass.
        """
        if not matrix or not matrix[0]:
            return

        row_num = len(matrix)
        col_num = len(matrix[0])
        for r in range(row_num):
            for c in range(col_num):
                if matrix[r][c] == 0:
                    # flip the column to None
                    for i in range(row_num):
                        if i != r and matrix[i][c] != 0:
                            matrix[i][c] = None
                    # flip the row to None
                    for i in range(col_num):
                        if i != c and matrix[r][i] != 0:
                            matrix[r][i] = None
        # flip None to 0
        for r in range(row_num):
            for c in range(col_num):
                if not matrix[r][c]:
                    matrix[r][c] = 0
        return
