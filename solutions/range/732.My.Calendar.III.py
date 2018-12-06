# Implement a MyCalendarThree class to store your events. A new event can always be added.
#
# Your class will have one method, book(int start, int end).
# Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
#
# A K-booking happens when K events have some non-empty intersection (ie., there is 41 time that is common to all K events.)
#
# For each call to the method MyCalendar.book,
# return an integer K representing the largest integer such that there exists a K-booking in the calendar.
#
# Your class will be called like this: MyCalendarThree cal = new MyCalendarThree(); MyCalendarThree.book(start, end)
# Example 1:
#
# MyCalendarThree();
# MyCalendarThree.book(10, 20); // returns 1
# MyCalendarThree.book(50, 60); // returns 1
# MyCalendarThree.book(10, 40); // returns 2
# MyCalendarThree.book(5, 15); // returns 3
# MyCalendarThree.book(5, 10); // returns 3
# MyCalendarThree.book(25, 55); // returns 3
# Explanation:
# The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
# The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
# The remaining events cause the maximum K-booking to be only a 3-booking.
# Note that the last event locally causes a 2-booking, but the answer is still 3 because
# eg. [10, 20), [10, 40), and [5, 15) are still triple booked.
#
#
# Note:
#
# The number of calls to MyCalendarThree.book per test case will be at most 400.
# In calls to MyCalendarThree.book(start, end), start and end are integers in the range [0, 10^9].
import bisect

class MyCalendarThree:

    def __init__(self):
        # a sorted starting positions of segments.
        self.starts = []
        # given (a, b), self.point2count indicates how many segments covering point a.
        self.point2count = dict()
        self.bookings = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        cnt = 0
        for booking in self.bookings:
            s, e = booking
            if s <= start < e:
                cnt += 1

        # update all points starting start covering by (start, end)
        low_bound_index = bisect.bisect_left(self.starts, start)
        while low_bound_index < len(self.starts) and self.starts[low_bound_index] < end:
            self.point2count[self.starts[low_bound_index]] += 1
            low_bound_index += 1

        # there are cnt + 1 segments covering the point of start, if start not in the starts list already
        if start not in self.point2count.keys():
            bisect.insort_left(self.starts, start)

        self.point2count[start] = cnt + 1
        self.bookings.append((start, end))

        max_count = -1
        for (_, c) in self.point2count.items():
            max_count = max(max_count, c)
        return max_count

cal = MyCalendarThree()
print(cal.book(26, 32))
print(cal.book(26, 35))
print(cal.book(25, 32))
print(cal.book(18, 26))




