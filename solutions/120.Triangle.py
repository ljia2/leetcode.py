class Solution:
    def minimumTotal(self, triangle):
        """

        Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

        For example, given the following triangle

        [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]
        The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

        Note:

        Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

        :type triangle: List[List[int]]
        :rtype: int


        iterate i from row 1 to row n:
            dp [len(traiangle[i-1]) + 2] stores the min path sum to the left/right shoulder
        """

        last_min_sum = [0]
        for i in range(len(triangle)):
            min_sum = [0] * len(triangle[i])
            for j in range(len(triangle[i])):
                if j == 0:
                    min_sum[j] = last_min_sum[j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    min_sum[j] = last_min_sum[j-1] + triangle[i][j]
                else:
                    min_sum[j] = min(last_min_sum[j-1], last_min_sum[j]) + triangle[i][j]
            last_min_sum = min_sum
        return min(last_min_sum)