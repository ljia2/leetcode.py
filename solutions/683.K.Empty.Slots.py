class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        fb_day = [0] * len(flowers)

        for i in range(len(flowers)):
            fb_day[flowers[i]-1] = i + 1

        earliest_results = -1
        start = 0
        while start < len(fb_day)-k-1:
            max_day = max(fb_day[start], fb_day[start+k+1])
            l_start = start + 1
            while l_start < start + k + 1:
                if fb_day[l_start] > max_day:
                    l_start += 1
                else:
                    break
            if l_start == start + k + 1:
                if earliest_results < 0 or earliest_results > max_day:
                    earliest_results = max_day
                start = start + k + 1
            else:
                start = l_start
        return earliest_results


def main():
    s = Solution()
    # day 6 and day 8 all are qualified results. we need to return the earliest qualified day.
    print(s.kEmptySlots([3,9,2,8,1,6,10,5,4,7], 1))


if __name__ == "__main__":
    main()

