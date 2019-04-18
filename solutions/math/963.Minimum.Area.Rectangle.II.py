from collections import defaultdict
import math

class Solution(object):
    def minAreaFreeRect(self, points):
        """
        Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points,
        with sides not necessarily parallel to the x and y axes.

        If there isn't any rectangle, return 0.

        Example 1:

        Input: [[1,2],[2,1],[1,0],[0,1]]
        Output: 2.00000
        Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
        Example 2:



        Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
        Output: 1.00000
        Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
        Example 3:



        Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
        Output: 0
        Explanation: There is no possible rectangle to form from these points.
        Example 4:



        Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
        Output: 2.00000
        Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.


        Note:

        1 <= points.length <= 50
        0 <= points[i][0] <= 40000
        0 <= points[i][1] <= 40000
        All points are distinct.
        Answers within 10^-5 of the actual value will be accepted as correct.

        :type points: List[List[int]]
        :rtype: float


        Dot product of two sides in a rectangle should be zero because a . b = |a| |b| cos(90)
        If we can extend p3 by the same margin delta(p2 - p1), we can have the fourth point p4.
        x4 = x3 + (x2 - x1)
        y4 = y3 + (y2 - y1)
        If p4 in points, calculate area.
        """
        if not points or len(points) < 4:
            return 0

        points = list(map(lambda x: (x[0], x[1]), points))
        n = len(points)

        rectangles = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                # if we use point i and j use the diagnoal.
                xi, yi = points[i]
                xj, yj = points[j]
                dist = (xi-xj)**2 + (yi-yj)**2
                center = (xi+xj)/2, (yi+yj)/2
                rectangles[(dist, center)].append((points[i], points[j]))

        min_area = 10**9
        for k, v in rectangles.items():
            if len(v) < 2:
                continue
            for i in range(len(v)):
                for j in range(i+1, len(v)):
                    # when two pairs of points sharing the same center and having the same length,
                    # a rectangle is formed; take three points to compute area
                    xi, yi = v[i][0]
                    xj, yj = v[i][1]
                    xk, yk = v[j][0]
                    area = math.sqrt((xk-xj) ** 2 + (yk-yj) ** 2) * math.sqrt((xi-xk)**2 + (yi-yk)**2)
                    min_area = min(min_area, area)
        return min_area if min_area < 10**9 else 0

s = Solution()
print(s.minAreaFreeRect([[0,1],[2,1],[1,1],[1,0],[2,0]]))

