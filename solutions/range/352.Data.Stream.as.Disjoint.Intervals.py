# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
# Given a data stream input of non-negative integers a1, a2, ..., an, ...,
# summarize the numbers seen so far as a list of disjoint intervals.
#
# For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:
#
# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]

# Follow up:
# What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?

import bisect

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        # maintain a sorted list of non-overlapping tuples (intervals)
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void

        """
        if not self.intervals:
            self.intervals.append((val, val+1))
        else:
            # the first interval adjacent or overlapping with (val, val + 1)
            index = bisect.bisect_left(self.intervals, (val, val+1))
            if index > 0:
                if self.intervals[index-1][1] >= val:
                    index -= 1
            start = val
            end = val + 1

            # merge intervals overlapping or adjacent to (val, val + 1)
            if index < len(self.intervals):
                start = min(self.intervals[index][0], val)
                while index < len(self.intervals) and self.intervals[index][0] <= val + 1:
                    end = max(self.intervals[index][1], val + 1)
                    # pop tuple at index and following tuples automatically move forward.
                    self.intervals.pop(index)

            bisect.insort_left(self.intervals, (start, end))
        return

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        ans = []
        for s, e in self.intervals:
            # convert back to close interval
            ans.append(Interval(s, e-1))
        return ans


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(1)
obj.addNum(3)
obj.addNum(7)
obj.addNum(2)
obj.addNum(6)
print(obj.getIntervals())