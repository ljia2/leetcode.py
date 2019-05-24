# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e


class Solution:
    def merge(self, intervals):
        """
        Given a collection of intervals, merge all overlapping intervals.

        Example 1:

        Input: [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
        Example 2:

        Input: [[1,4],[4,5]]
        Output: [[1,5]]
        Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        # use operator and sorted to sort class instances
        intervals.sort(key=lambda x: x.start)
        s = intervals[0].start
        e = intervals[0].end
        for i in range(1, len(intervals)):
            interval = intervals[i]
            # if it is overlap with the most recent "reference" interval (left, right)
            # that may merge all overlap intervals before.
            if e >= interval.start:
                s = min(interval.start, s)
                e = max(interval.end, e)
            # update results; reset the "reference" interval as current one.
            else:
                ans.append(Interval(s, e))
                s = interval.start
                e = interval.end

        # Note! Do not forget the last interval (left, right) !!!!
        ans.append(Interval(s, e))
        return ans






