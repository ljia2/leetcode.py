# Implement a MyCalendarTwo class to store your events.
# A new event can be added if adding the event will not cause a triple booking.
#
# Your class will have one method, book(int start, int end).
# Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
#
# A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)
#
# For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking.
# Otherwise, return false and do not add the event to the calendar.
#
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
#
# Example 1:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true
# MyCalendar.book(5, 15); // returns false
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true
#
# Explanation:
# The first two events can be booked.  The third event can be double booked.
# The fourth event (5, 15) can't be booked, because it would result in a triple booking.
# The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
# The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
# the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
# Note:
#
# The number of calls to MyCalendar.book per test case will be at most 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

import bisect

class MyCalendarTwo:

    def __init__(self):
        self.bookings = [(0, 0), (float("inf"), float("inf"))]
        # use a list of overlaps to identify double booking; triple booking overlaps with overlap
        self.dbookings = [(0, 0), (float("inf"), float("inf"))]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # return the index of insert (start, end)
        dblot = bisect.bisect_left(self.dbookings, (start, end))
        s1, e1 = self.dbookings[dblot-1]
        s2, e2 = self.dbookings[dblot]
        if self._is_overlap(s1, e1, start, end) or self._is_overlap(s2, e2, start, end):
            return False
        else:
            # iterate all bookings to update overlaps.
            for booking in self.bookings:
                s, e = booking
                if self._is_overlap(s, e, start, end):
                    bisect.insort_left(self.dbookings, (max(s, start), min(e, end)))
            self.bookings.append((start, end))
            return True

    def _is_overlap(self, s1, e1, s2, e2):
        return max(s1, s2) < min(e1, e2)


# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo()
print(obj.book(33,44));
print(obj.book(85,95));
print(obj.book(20,37));
print(obj.book(91,100));
print(obj.book(89,100));
print(obj.book(77,87));
print(obj.book(80,95));
print(obj.book(42,61));
print(obj.book(40,50));
print(obj.book(85,99));
print(obj.book(74,91));
print(obj.book(70,82));
print(obj.book(5,17));
print(obj.book(77,89));
print(obj.book(16,26));
print(obj.book(21,31));
print(obj.book(30,43));
print(obj.book(96,100));
print(obj.book(27,39));
print(obj.book(44,55));
print(obj.book(15,34));
print(obj.book(85,99));
print(obj.book(74,93));
print(obj.book(84,94));
print(obj.book(82,94));
print(obj.book(46,65));
print(obj.book(31,49));
print(obj.book(58,73));
print(obj.book(86,99));
print(obj.book(73,84));
print(obj.book(68,80));
print(obj.book(5,18));
print(obj.book(75,87));
print(obj.book(88,100));
print(obj.book(25,41));
print(obj.book(66,79));
print(obj.book(28,41));
print(obj.book(60,70));
print(obj.book(62,73));
print(obj.book(16,33));