import bisect

class Solution:
    def searchMatrix(self, matrix, target):
        """
        Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
        Integers in each row are sorted from left to right.
        The first integer of each row is greater than the last integer of the previous row.

        Example 1:

        Input:
        matrix = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 3
        Output: true
        Example 2:

        Input:
        matrix = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 13
        Output: false

        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        max_row = len(matrix)
        max_col = len(matrix[0])

        rownums = [matrix[i][0] for i in range(max_row)]
        colnums = [matrix[i][max_col-1] for i in range(max_row)]

        low_row_index = bisect.bisect_left(colnums, target)
        upper_row_index = bisect.bisect_right(rownums, target)

        for r in range(low_row_index, upper_row_index):
            row = matrix[r]
            index = bisect.bisect_right(row, target)
            if index > 0 and row[index-1] == target:
                return True
        return False

s = Solution()
print(s.searchMatrix([[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]], 3))
print(s.searchMatrix([[1], [3]], 3))