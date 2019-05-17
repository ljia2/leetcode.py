
# class Solution(object):
#     def minAreaRect(self, points):
#         """
#         Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points,
#         with sides parallel to the x and y axes.
#
#         If there isn't any rectangle, return 0.
#
#         Example 1:
#
#         Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
#         Output: 4
#
#         Example 2:
#         Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
#         Output: 2
#
#
#         Note:
#
#         1 <= points.length <= 500
#         0 <= points[i][0] <= 40000
#         0 <= points[i][1] <= 40000
#         All points are distinct.
#
#         :type points: List[List[int]]
#         :rtype: int
#         """
#
#         if len(points) < 4:
#             return 0
#
#         vlines = collections.defaultdict(list)
#         hlines = collections.defaultdict(list)
#         for i in range(len(points)):
#             for j in range(i+1, len(points)):
#                 x, y = points[i]
#                 xx, yy = points[j]
#                 if xx == x:
#                     vlines[(xx, yy)].append(y-yy) if y > yy else vlines[(x, y)].append(yy-y)
#                 elif yy == y:
#                     hlines[(xx, yy)].append(x-xx) if x > xx else hlines[(x, y)].append(xx - x)
#
#         minArea = float("inf")
#         spoints = set(map(lambda x: (x[0], x[1]), points))
#         ps = set(vlines.keys()).intersection(set(hlines.keys()))
#         for p in ps:
#             for vh in vlines[p]:
#                 for hh in hlines[p]:
#                     x, y = p
#                     if (x+hh, y+vh) in spoints:
#                         minArea = min(vh*hh, minArea)
#         return minArea if minArea < float("inf") else 0

# s = Solution()
# print(s.minAreaRect([[1,2],[1,3],[3,3],[4,4],[2,1],[1,4],[2,2],[1,0],[0,2]]))

class SolutionII(object):
    """
    Intuition

    Count each rectangle by right-most edge.

    Algorithm

    Group the points by x coordinates, so that we have columns of points.
    Then, for every pair of points in a column (with coordinates (x,y1) and (x,y2)),
    check for the smallest rectangle with this pair of points as the rightmost edge.
    We can do this by keeping memory of what pairs of points we've seen before.
    """

    def minAreaRect(self, points):
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)

        lastx = dict()
        ans = float('inf')

        # iterate from left to right:
        for x in sorted(columns):
            column = columns[x]
            column.sort()
            # for any pair of y1 and y2
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    # if (y1, y2) are seen before in lastx
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    # record (y1, y2) to latest x ordinate.
                    lastx[(y1, y2)] = x
        return ans if ans < float('inf') else 0


### Follow up  toe see all rectangles with minimum areas.
import collections
class VartionSolution(object):
    def minAreaRect(self, points):
        """
        Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points,
        with sides parallel to the x and y axes.

        If there isn't any rectangle, return 0.

        Example 1:

        Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
        Output: 4

        Example 2:
        Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
        Output: 2


        Note:

        1 <= points.length <= 500
        0 <= points[i][0] <= 40000
        0 <= points[i][1] <= 40000
        All points are distinct.

        :type points: List[List[int]]
        :rtype: int
        """

        if len(points) < 4:
            return 0

        n = len(points)
        centers = collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                ix, iy = points[i]
                jx, jy = points[j]

                cx, cy = (ix + jx) * 0.5, (iy + jy) * 0.5
                dist = (ix-jx) ** 2 + (iy-jy) ** 2

                centers[(cx, cy, dist)].append((i, j))

        ans = float("inf")
        for key in centers.keys():
            pairs = centers[key]
            if len(pairs) < 2:
                continue
            n = len(pairs)
            for i in range(n):
                for j in range(i+1, n):
                    a, b = pairs[i]
                    c, d = pairs[j]
                    l1 = ((points[a][0] - points[c][0]) ** 2 + (points[a][1] - points[c][1]) ** 2) ** 0.5
                    l2 = ((points[a][0] - points[d][0]) ** 2 + (points[a][1] - points[d][1]) ** 2) ** 0.5
                    ans = min(ans, l1*l2)
        return int(ans) if ans < float("inf") else 0

s = SolutionII()
print(s.minAreaRect([[1,2],[1,3],[3,3],[4,4],[2,1],[1,4],[2,2],[1,0],[0,2]]))