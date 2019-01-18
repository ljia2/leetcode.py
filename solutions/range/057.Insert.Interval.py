# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """

        Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

        You may assume that the intervals were initially sorted according to their start times.

        Example 1:

        Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        Output: [[1,5],[6,9]]
        Example 2:

        Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        Output: [[1,2],[3,10],[12,16]]
        Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]


        """
        ans = []
        insert = False
        s, e = newInterval.start, newInterval.end
        for interval in intervals:
            if interval.start > e and not insert:
                ans.append(Interval(s, e))
                insert = True
            if interval.end < s or interval.start > e:
                ans.append(interval)
            else:
                s = min(s, interval.start)
                e = max(e, interval.end)
        if not insert:
            ans.append(Interval(s, e))
        return ans