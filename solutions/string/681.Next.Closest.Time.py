class BruteForceSolution:
    def nextClosestTime(self, time):
        """
        Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
        There is no limit on how many times a digit can be reused.

        You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

        Example 1:

        Input: "19:34"
        Output: "19:39"
        Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
        It is not 19:33, because this occurs 23 hours and 59 minutes later.

        Example 2:

        Input: "23:59"
        Output: "22:22"
        Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
        It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
        Seen this question in a real interview before?

        :type time: str
        :rtype: str

        keep adding a minute until encouter a time reusing existing digits.

        T: O(24*60)

        """
        digits = set(time)
        hour = int(time[:time.index(":")])
        min = int(time[time.index(":")+1:])

        while True:
            min = (min + 1) % 60
            if min == 0:
                hour = (hour + 1) % 24
            # convert to valid time format.
            new_time = "%02d:%02d" % (hour, min)
            # python use <= compare whether a set is a subset of another set
            if set(new_time) <= digits:
                break
        return new_time

def main():
    s = BruteForceSolution()
    print(s.nextClosestTime("01:30"))
    print(s.nextClosestTime("23:59"))

if __name__ == "__main__":
    main()