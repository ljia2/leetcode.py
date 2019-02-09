class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix and matrix[0]:
            self.size = len(matrix[0])
            self.forest = [[0] * len(matrix[0]) + row for row in matrix]
            self.buildForest(self.forest)

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.forest[row][col + self.size] = val
        ti = col + self.size
        while ti > 0:
            pti = ti // 2
            self.forest[row][pti] = self.forest[row][2*pti] + self.forest[row][2*pti+1]
            ti //= 2

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        sum = 0
        for r in range(row1, row2+1, 1):
            ti = col1 + self.size
            tj = col2 + self.size
            while ti <= tj:
                if ti % 2 != 0:
                    sum += self.forest[r][ti]
                    ti += 1

                if tj % 2 != 1:
                    sum += self.forest[r][tj]
                    tj -= 1
                ti //= 2
                tj //= 2
        return sum

    def buildForest(self, forest):
        for t in forest:
            ti = self.size - 1
            while ti > 0:
                t[ti] = t[2*ti] + t[2*ti + 1]
                ti -= 1
