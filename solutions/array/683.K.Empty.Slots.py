class Solution:
    def kEmptySlots(self, flowers, k):
        """
        There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days.
        In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

        Given an array flowers consists of number from 1 to N.
        Each number in the array represents the place where the flower will open in that day.

        For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i
        and x will be in the range from 1 to N.

        Also given an integer k, you need to output in which day there exists two flowers in the status of blooming,
        and also the number of flowers between them is k and these flowers are not blooming.

        If there isn't such day, output -1.

        :type flowers: List[int]
        :type k: int
        :rtype: int

        Note:
        1) create fb_day[x] = i: represent flower x blooming at day i
        2) scan fb_day with a sliding window of k to ensure the first and the last in the window their fb_day differs at least k
          a) use max_day to track the latest day (max_day) of fb_day[start] and fb_start[start + k - 1]
             (a valid window the flowers in between start and start + k - 1 should all blooming after that latest day!!!)
          b) if there is a flower in the middle l_start if earlier than max_day, then the flowers in the window do not satisfy the condition.
             i) restart the next window at position l_start.
          c) otherwise we have a window satisfy the condition; return earliest_results.

        """
        # mapping from day i to flower fb_day[i]
        fb_day = [0] * len(flowers)
        for i in range(len(flowers)):
            fb_day[flowers[i]-1] = i + 1

        earliest_results = -1
        start = 0
        while start < len(fb_day)-k-1:
            max_day = max(fb_day[start], fb_day[start+k+1])
            # check the blooming day between flower start and flower start+k+1
            l_start = start + 1
            while l_start < start + k + 1:
                if fb_day[l_start] > max_day:
                    l_start += 1
                else:
                    break

            # check whether find a valid window of k
            if l_start == start + k + 1:
                if earliest_results < 0 or earliest_results > max_day:
                    earliest_results = max_day
                # reset the start.
                start = start + k + 1
            else:
                # restart the sliding window at the position l_start
                start = l_start
        return earliest_results


def main():
    s = Solution()
    # day 6 and day 8 all are qualified results. we need to return the earliest qualified day.
    print(s.kEmptySlots([3,9,2,8,1,6,10,5,4,7], 1))


if __name__ == "__main__":
    main()

