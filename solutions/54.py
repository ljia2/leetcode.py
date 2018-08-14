import numpy as np

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        max_row = len(matrix)
        max_col = len(matrix[0])

        results = []
        for c in range(0, max_col):
            results.append(matrix[0][c])

        if max_row > 1:
            for r in range(1, max_row):
                results.append(matrix[r][max_col-1])

        if max_row > 1 and max_col > 1:
            for c in range(max_col-2, -1, -1):
                results.append(matrix[max_row-1][c])

        if max_row > 2 and max_col > 1:
            for r in range(max_row-2, 0, -1):
                results.append(matrix[r][0])

        if max_row > 2 and max_col > 2:
            return results + self.spiralOrder(np.array(matrix)[1:max_row-1,1:max_col-1].tolist())
        else:
            return results


def main():
    s = Solution()
    input1 = [[ 1, 2, 3 ],[4, 5, 6 ],[7, 8, 9 ]]
    print(s.spiralOrder(input1))
    input2 = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
    print(s.spiralOrder(input2))
    input3 = [[5, 4, 2, 1]]
    print(s.spiralOrder(input3))
    input4 = [[5], [4], [3], [2]]
    print(s.spiralOrder(input4))
    input5 = [[1, 2, 3, 4],[9,10,11,12]]
    print(s.spiralOrder(input5))

if __name__ == "__main__":
    main()