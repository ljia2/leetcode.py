class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or len(matrix[0]) == 0:
            self.sum = [[]]

        row = len(matrix)
        column = len(matrix[0])

        # trick: use row + 1 and column + 1 to initialize sum matrix.
        # sum[i][j] records the sum of rectangle from (0, 0) to (i-1, j-1)
        self.sumMatrix = [[0] * (column + 1) for _ in range(row + 1)]

        for r in range(row):
            for c in range(column):
                self.sumMatrix[r+1][c+1] = self.sumMatrix[r][c+1] + self.sumMatrix[r+1][c] + matrix[r+1][c+1] - self.sumMatrix[r][c]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sumMatrix[row2+1][col2+1] - self.sumMatrix[row2+1][col1] - self.sumMatrix[row1][col2+1] + self.sumMatrix[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(obj.sumRegion(2,1,4,3))
print(obj.sumRegion(1,1,2,2))
print(obj.sumRegion(1,2,2,4))