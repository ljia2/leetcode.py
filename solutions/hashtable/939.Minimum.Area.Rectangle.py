import collections


class Solution(object):
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

        vlines = collections.defaultdict(list)
        hlines = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x, y = points[i]
                xx, yy = points[j]
                if xx == x:
                    vlines[(xx, yy)].append(y-yy) if y > yy else vlines[(x, y)].append(yy-y)
                elif yy == y:
                    hlines[(xx, yy)].append(x-xx) if x > xx else hlines[(x, y)].append(xx - x)

        minArea = 10**32

        spoints = set(map(lambda x: (x[0], x[1]), points))
        ps = set(vlines.keys()).intersection(set(hlines.keys()))
        for p in ps:
            for vh in vlines[p]:
                for hh in hlines[p]:
                    x, y = p
                    if (x+hh, y+vh) in spoints:
                        minArea = min(vh*hh, minArea)
        return minArea if minArea < 10**32 else 0

s = Solution()
print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))