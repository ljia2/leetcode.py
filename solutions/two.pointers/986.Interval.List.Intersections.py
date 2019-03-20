# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

        Return the intersection of these two interval lists.

        (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
        The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.
        For example, the intersection of [1, 3] and [2, 4] is [2, 3].)


        Example 1:


        Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
        Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.

        Note:

        0 <= A.length < 1000
        0 <= B.length < 1000
        0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]


        merge two linked list; use a and b to refer the heads of two linked list.
        """

        if not A or not B:
            return []

        A.sort(key=lambda x: x.start)
        B.sort(key=lambda x: x.start)

        ans = []
        a = b = 0
        while a < len(A) and b < len(B):
            if self.overlap(A[a], B[b]):
                ans.append(Interval(max(A[a].start, B[b].start), min(A[a].end, B[b].end)))
                if A[a].end < B[b].end:
                    # replace the first interval of B.
                    B[b] = Interval(A[a].end+1, B[b].end)
                    a += 1
                elif A[a].end > B[b].end:
                    # replace the first interval of B.
                    A[a] = Interval(B[b].end+1, A[a].end)
                    b += 1
                else:
                    a += 1
                    b += 1
            else:
                if A[a].end < B[b].end:
                    a += 1
                else:
                    b += 1
        return ans

    def overlap(self, a, b):
        return max(a.start, b.start) <= min(a.end, b.end)


s = Solution()
A = [Interval(0, 2), Interval(5, 10), Interval(13, 23), Interval(24, 25)]
B = [Interval(1, 5), Interval(8, 12), Interval(15, 24), Interval(25, 26)]
print(s.intervalIntersection(A, B))