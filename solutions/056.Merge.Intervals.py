import operator


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __lt__(self, other):
        self.start < other.start


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        results = []
        # If intervals is empty directly return empty list
        if intervals:
            # use operator and sorted to sort class instances
            s_intervals = sorted(intervals, key=operator.attrgetter("start"))
            for i in s_intervals:
                if s_intervals.index(i) == 0:
                    left = i.start
                    right = i.end
                elif right >= i.start:
                    left = min(i.start, left)
                    right = max(i.end, right)
                else:
                   results.append(Interval(left, right))
                   left = i.start
                   right = i.end
            # Do not forget the last interval if it does not overlap with previous ones.
            results.append(Interval(left, right))

        return results


def main():
    s = Solution()
    results = s.merge([ Interval(2,6), Interval(8,10), Interval(1,3), Interval(15,18)])
    print(results)


if __name__ == "__main__":
    main()


