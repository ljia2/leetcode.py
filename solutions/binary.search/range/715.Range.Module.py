# A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.
#
# addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval.
# Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
# queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.
# removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).

# Example 1:
#
# addRange(10, 20): null
# removeRange(14, 16): null
# queryRange(10, 14): true (Every number in [10, 14) is being tracked)
# queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
# queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
# Note:
#
# A half open interval [left, right) denotes all real numbers left <= x < right.
# 0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
# The total number of calls to addRange in a single test case is at most 1000.
# The total number of calls to queryRange in a single test case is at most 5000.
# The total number of calls to removeRange in a single test case is at most 1000.


# Typical use tree of segment

import bisect

class RangeModule:

    def __init__(self):
        self.intervals = [(-float("inf"), -float("inf")), (float("inf"), float("inf"))]

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        newIntervals = set()
        removedIntervals = []
        for interval in self.intervals:
            if interval[1] < left:
                continue
            if interval[0] > right:
                break
            if max(interval[0], left) >= min(interval[1], right):
                newIntervals.add((left, right))
            else:
                newIntervals.add((min(left, interval[0]), max(right, interval[1])))
                removedIntervals.append(interval)

        if not newIntervals:
            bisect.insort_left(self.intervals, (left, right))
        else:
            for interval in removedIntervals:
                self.intervals.pop(bisect.bisect_left(self.intervals, interval))
            for interval in newIntervals:
                bisect.insort_left(self.intervals, interval)
        return

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        for interval in self.intervals:
            if interval[0] >= right:
                break
            if interval[0] <= left and right <= interval[1]:
                return True
        return False

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        newIntervals = []
        removedIntervals = []
        for interval in self.intervals:
            if interval[0] >= right:
                break
            # if not overlap
            if max(interval[0], left) >= min(interval[1], right):
                continue
            if interval[0] <= left and right <= interval[1]:
                newIntervals.append((interval[0], left))
                newIntervals.append((right, interval[1]))
                removedIntervals.append(interval)
            elif interval[0] <= left and interval[1] < right:
                newIntervals.append((interval[0], left))
                removedIntervals.append(interval)
            elif interval[0] >= left and interval[1] <= right:
                removedIntervals.append(interval)
            elif interval[0] >= left and interval[1] > right:
                newIntervals.append((right, interval[1]))
                removedIntervals.append(interval)

        for interval in removedIntervals:
            self.intervals.pop(bisect.bisect_left(self.intervals, interval))
        for interval in newIntervals:
            bisect.insort_left(self.intervals, interval)
        return



# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.addRange(6, 8)
obj.removeRange(7, 8)
obj.removeRange(8, 9)
obj.addRange(8, 9)
obj.removeRange(1, 3)
obj.addRange(1, 8)
print(obj.queryRange(2, 4))
print(obj.queryRange(2, 9))
print(obj.queryRange(4, 6))