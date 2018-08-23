class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = set()
        for d in time:
            if d == ':':
                continue
            digits.add(d)
        hour = int(time[:time.index(":")])
        min = int(time[time.index(":")+1:])
        while True:
            min = (min + 1) % 60
            if min == 0:
                hour = (hour + 1) % 24
            h_str = "0" + str(hour) if hour < 10 else str(hour)
            m_str = "0" + str(min) if min < 10 else str(min)
            if self.digitCheck(digits, h_str, m_str):
                next_time = h_str + ":" + m_str
                break
        return next_time

    def digitCheck(self, digits, h_str, m_str):
        for d in h_str:
            if d not in digits:
                return False
        for d in m_str:
            if d not in digits:
                return False
        return True


def main():
    s = Solution()
    print(s.nextClosestTime("01:30"))
    print(s.nextClosestTime("23:59"))

if __name__ == "__main__":
    main()