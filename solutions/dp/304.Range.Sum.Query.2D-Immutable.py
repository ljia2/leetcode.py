class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            self.sum = [[]]
        else:
            row = len(matrix)
            column = len(matrix[0])

            # sum[i][j] records the sum of rectangle from (0, 0) to (i, j)

            # can not initilize list of list below, actually all rows are referrence the same columns
            # self.sum = [[0] * column] * row
            self.sum = [[None] * column for r in range(row)]

            for r in range(row):
                for c in range(column):
                    if r == 0 and c == 0:
                        self.sum[r][c] = matrix[r][c]
                    elif r == 0:
                        self.sum[r][c] = self.sum[r][c-1] + matrix[r][c]
                    elif c == 0:
                        self.sum[r][c] = self.sum[r-1][c] + matrix[r][c]
                    else:
                        self.sum[r][c] = self.sum[r-1][c] + self.sum[r][c-1] + matrix[r][c] - self.sum[r-1][c-1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.sum[row2][col2]
        elif row1 == 0:
            return self.sum[row2][col2] - self.sum[row2][col1-1]
        elif col1 == 0:
            return self.sum[row2][col2] - self.sum[row1-1][col2]
        else:
            return self.sum[row2][col2] - self.sum[row2][col1-1] - self.sum[row1-1][col2] + self.sum[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(obj.sumRegion(2,1,4,3))
print(obj.sumRegion(1,1,2,2))
print(obj.sumRegion(1,2,2,4))