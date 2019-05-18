from heapq import heappop, heappush

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

        :type intervals: List[List[Int]]
        :rtype: int
        """
        if not intervals:
            return 0

        # sorting meetings by their start
        intervals.sort()

        # hint: use list and heappop/heappush from heapq to mimic priorityQueue
        hp = [intervals[0][1]]
        for start, end in intervals[1:]:
            # peek the meeing with the earliest end time, if it ends before start, assign its room to new meeting
            if hp and hp[0] <= start:
                # the room with min ending time i; interval is overlap with i, push i back and break
                # otherwise, keep popping booked room that had ended before interval.start.
                heappop(hp)
            heappush(hp, end)
        return len(hp)


s = Solution()
print(s.minMeetingRooms([[0, 30], [15, 20], [5, 10]]))

# Scan the line
# class SolutionII(object):
#     def minMeetingRooms(self, intervals):
#         """
#         :type intervals: List[List[Int]
#         :rtype: int
#         """
#
#         # If there are no meetings, we don't need any rooms.
#         if not intervals:
#             return 0
#
#         used_rooms = 0
#
#         # Separate out the start and the end timings and sort them individually.
#         start_timings = sorted([s for s, _ in intervals])
#         end_timings = sorted(e for _, e in intervals)
#         L = len(intervals)
#
#         # The two pointers in the algorithm: e_ptr and s_ptr.
#         end_pointer = 0
#         start_pointer = 0
#
#         # Until all the meetings have been processed
#         while start_pointer < L:
#
#             # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
#             if start_timings[start_pointer] >= end_timings[end_pointer]:
#                 # Free up a room and increment the end_pointer.
#                 used_rooms -= 1
#                 end_pointer += 1
#
#             # We do this irrespective of whether a room frees up or not.
#             # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
#             # remain the same in that case. If no room was free, then this would increase used_rooms
#             used_rooms += 1
#             start_pointer += 1
#
#         return used_rooms


# Follow up: What if the times are given as 10AM - 11:30AM or 11:00AM to 1PM
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Soltion(object):
    def translate(self, times):
        ans = []
        for time in times:
            ts = time.lower().trim().split("-")
            start = self.convert(ts[0])
            end = self.convert(ts[1])
            ans.append(Interval(start, end))
        return ans

    def convert(self, ts):
        i = ts.find("am")
        base = 0 if i > 0 else 12

        ts = ts[:i]
        hm = ts.split(":")
        h = int(hm[0]) + base
        m = int(hm[1])
        return h * 60 + m



