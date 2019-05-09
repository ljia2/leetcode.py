from heapq import heappop, heappush


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def minMeetingRooms(self, intervals):
        """
        Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
        find the minimum number of conference rooms required.

        Example 1:

        Input: [[0, 30],[5, 10],[15, 20]]
        Output: 2
        Example 2:

        Input: [[7,10],[2,4]]
        Output: 1
        NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals is None or not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        # hint: use list and heappop/heappush from heapq to mimic priorityQueue
        conf_queue = [intervals[0]]
        room_cnt = 1

        for interval in intervals[1:]:
            # keep poping conferences ending already.
            while conf_queue:
                # the room with min ending time i; interval is overlap with i, push i back and break
                # otherwise, keep popping booked room that had ended before interval.start.
                i = heappop(conf_queue)
                if interval.start < i:
                    heappush(conf_queue, i)
                    break
            heappush(conf_queue, interval.end)
            # keep the max_num conference room so far.
            room_cnt = max(room_cnt, len(conf_queue))

        return room_cnt


s = Solution()
print(s.minMeetingRooms([Interval(0, 30), Interval(15, 20), Interval(5, 10)]))