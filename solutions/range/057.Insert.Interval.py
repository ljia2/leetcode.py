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
        if not newInterval:
            return intervals

        ans = []
        for interval in intervals:
            # if 1) newInterval has been merged; or 2) interval is not overlapping with newInterval, add it into answer.
            if not newInterval or interval.end < newInterval.start or interval.start > newInterval.end:
                ans.append(interval)
            # if interval is after newInterval, insert newInterval first and then interval into answer
            elif interval.start > newInterval.end:
                ans.append(newInterval)
                ans.append(interval)
                newInterval = None
            else:
                # interval overlap with newInterval, merge interval with newInterval
                newInterval = Interval(min(s, interval.start), max(e, interval.end))

        # if newInterval is not inserted yet.
        if newInterval:
            ans.append(newInterval)
        return ans

#### Follow up: given a list of intervals and a target interval,
# return the mininum number of intervals from the list to merge to cover the target interver
# For example, [[-1, 9], [1, 10], [0, 3], [9, 10], [3, 14], [2, 9], [10, 16]] and [2, 15]
# there are several ways to conver [2, 15]
# 1: [-1, 9], [9, 10], [10, 16]
# 2: [1, 10], [10, 16]
# return 2.

class GreedySolution(object):
    def minimumIntervals(self, intervals, target):
        if not intervals or not target:
            return -1

        intervals.sort()
        n = len(intervals)
        start = target[0]
        ans = 0
        for i in range(n):
            cur = self.greedyHelper(intervals, i, start)
            ans += 1
            if intervals[cur][1] >= target[1]:
                return ans

            # the target has been partially covered until intervals[cur][1], update start to denote the remaining interval.
            start = intervals[cur][1]

        return ans

    # find the interval
    def greedyHelper(self, intervals, start, target):
        ans = None
        for i in range(start, len(intervals))

