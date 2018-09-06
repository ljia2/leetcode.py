class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        else:
            row_num = len(matrix)
            col_num = len(matrix[0])
            for r in range(row_num):
                for c in range(col_num):
                    if matrix[r][c] == 0:
                        for i in range(row_num):
                            if i != r and matrix[i][c] != 0:
                                matrix[i][c] = None
                        for i in range(col_num):
                            if i != c and matrix[r][i] != 0:
                                matrix[r][i] = None

            for r in range(row_num):
                for c in range(col_num):
                    if not matrix[r][c]:
                        matrix[r][c] = 0
            return
