import bisect


class Solution:
    def searchMatrix(self, matrix, target):
        """
        Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

        Integers in each row are sorted in ascending from left to right.
        Integers in each column are sorted in ascending from top to bottom.
        Example:

        Consider the following matrix:

        [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
        Given target = 5, return true.

        Given target = 20, return false.

        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        max_row = len(matrix)
        max_col = len(matrix[0])

        rfnums = [matrix[i][0] for i in range(max_row)]
        rlnums = [matrix[i][max_col-1] for i in range(max_row)]
        cfnums = matrix[0]
        clnums = matrix[max_row-1]

        row_lower = bisect.bisect_left(rlnums, target)
        row_upper = bisect.bisect_right(rfnums, target)
        col_lower = bisect.bisect_left(clnums, target)
        col_upper = bisect.bisect_right(cfnums, target)

        for r in range(row_lower, row_upper):
            nums = matrix[r][col_lower:col_upper]
            index = bisect.bisect_right(nums, target)
            if index > 0 and nums[index-1] == target:
                return True
        return False