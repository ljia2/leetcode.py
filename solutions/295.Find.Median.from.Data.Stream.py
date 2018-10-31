"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Both operations should be O(logN)

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

"""
from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.big = []
        self.median = None

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # use negative number to mimic the max heap of original numbers
        if not self.median:
            heappush(self.small, -float(num))
        elif num <= self.median:
            heappush(self.small, -float(num))
        else:
            heappush(self.big, float(num))

        # small at most one element more than big
        while len(self.small) > len(self.big) + 1:
            heappush(self.big, -heappop(self.small))
        # big must at most the same number of elements as small
        while len(self.big) > len(self.small):
            heappush(self.small, -heappop(self.big))

        num1 = -heappop(self.small)
        heappush(self.small, -num1)
        if len(self.small) == len(self.big):
            num2 = heappop(self.big)
            heappush(self.big, num2)
            self.median = (num1 + num2) * 0.5
        else:
            self.median = num1

    def findMedian(self):
        """
        :rtype: float
        """
        return self.median








# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())

