import collections
import math
class Solution(object):
    def countCornerRectangles(self, grid):
        """
        Given a grid where each entry is only 0 or 1, find the number of corner rectangles.

        A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.



        Example 1:

        Input: grid =
        [[1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1],
         [0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1]]
        Output: 1
        Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].


        Example 2:

        Input: grid =
        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]
        Output: 9
        Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.


        Example 3:

        Input: grid =
        [[1, 1, 1, 1]]
        Output: 0
        Explanation: Rectangles must have four distinct corners.


        Note:

        The number of rows and columns of grid will each be in the range [1, 200].
        Each grid[i][j] will be either 0 or 1.
        The number of 1s in the grid will be at most 6000.


        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not len(grid[0]):
            return 0

        if len(grid) == 1 or len(grid[0]) == 1:
            return 0

        r, c = len(grid), len(grid[0])

        col_dict = collections.defaultdict(set)
        for j in range(c):
            for i in range(r):
                if grid[i][j] == 1:
                    col_dict[j].add(i)
        ans = 0
        cols = list(col_dict.keys())
        for c1 in range(len(cols)):
            for c2 in range(0, c1):
                s1, s2 = col_dict[cols[c1]], col_dict[cols[c2]]
                ans += self.combination(len(s1.intersection(s2)), 2)

        return ans

    def combination(self, n, m):
        if n < m:
            return 0
        if n == m:
            return 1

        return math.factorial(n) / (math.factorial(n-m) * math.factorial(m))

s = Solution()
print(s.countCornerRectangles([[0,0,1,1],
                               [1,0,0,0],
                               [0,0,1,0],
                               [1,0,1,1]]))