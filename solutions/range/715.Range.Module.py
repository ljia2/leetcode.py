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

import bisect

class RangeModule:
    def __init__(self):
        # interval must be ordered and adjacent intervals.
        self.intervals = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void

        # add range might merge interval

        """
        new_intervals = []
        inserted = False
        for interval in self.intervals:
            if interval[0] > right and not inserted:
                bisect.insort_left(new_intervals, (left, right))
                inserted = True

            if interval[1] < left or interval[0] > right:
                bisect.insort_left(new_intervals, interval)
            else:
                # interval overlaps (left, right), update left and right
                left = min(left, interval[0])
                right = max(right, interval[1])

        if not inserted:
            bisect.insort_left(new_intervals, (left, right))
        self.intervals = new_intervals
        return

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        index = bisect.bisect_left(self.intervals, (left, right))
        if index > 0:
            interval = self.intervals[index-1]
            if interval[0]<= left and right <= interval[1]:
                return True
        if index < len(self.intervals):
            interval = self.intervals[index]
            if interval[0]<= left and right <= interval[1]:
                return True
        return False


    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void

        # remove range does not cause merging of interval, but might generates two disjoint intervals when overlapping.

        """
        new_intervals = []
        for interval in self.intervals:
            if interval[0] >= right or interval[1] <= left:
                bisect.insort_left(new_intervals, interval)
                continue
            if interval[0] < left:
                bisect.insort_left(new_intervals, (interval[0], left))
            if interval[1] > right:
                bisect.insort_left(new_intervals, (right, interval[1]))
        self.intervals = new_intervals
        return


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

obj.addRange(10, 20)
obj.removeRange(14, 16)
print(obj.queryRange(10, 14))
print(obj.queryRange(13, 15))
print(obj.queryRange(16, 17))