import operator
from heapq import heappop, heappush

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals is None or not intervals:
            return 0
        room_cnt = 0
        intervals.sort(key=operator.attrgetter("start"))
        # hint: use list and heappop/heappush from heapq to mimic piroityQueue
        conf_queue = []
        for interval in intervals:
            if not conf_queue:
                room_cnt = 1
                heappush(conf_queue, interval.end)
            else:
                while conf_queue:
                    i = heappop(conf_queue)
                    if interval.start < i: # interval is inclsive on end
                        heappush(conf_queue, i)
                        break
                heappush(conf_queue, interval.end)
                if len(conf_queue) > room_cnt:
                    room_cnt = len(conf_queue)
        return room_cnt


s = Solution()
input = [Interval(0, 30), Interval(15, 20), Interval(5, 10)]
print(s.minMeetingRooms(input))