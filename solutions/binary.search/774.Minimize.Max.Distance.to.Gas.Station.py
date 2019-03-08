import math

class Solution:
    def minmaxGasDist(self, stations, K):
        """
        On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1],
        where N = stations.length.

        Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

        Return the smallest possible value of D.

        Example:

        Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
        Output: 0.500000
        Note:

        stations.length will be an integer in range [10, 2000].
        stations[i] will be an integer in range [0, 10^8].
        K will be an integer in range [1, 10^6].
        Answers within 10^-6 of the true value will be accepted as correct.

        :type stations: List[int]
        :type K: int
        :rtype: float

        Answers within 10^-6 of the true value will be accepted as correct.

        it is a hint of binary search over float space.

        Why did I use s binary search?
        In fact there are some similar problems on Leetcode so that is part of experience.
        Secondly, I got a hint from "Answers within 10^-6 of the true value will be accepted as correct.". The first solution I tried was binary search.
        Because binary search may not find exact value but it can approach the true answer.

        Explanation of solution
        Now we are using binary search to find the smallest possible value of D.
        I initilze left = 0 and right = the distance between the first and the last station
        count is the number of gas station we need to make it possible.
        if count > K, it means mid is too small to realize using only K more stations.
        if count <= K, it means mid is possible and we can continue to find a bigger one.
        When left + 1e-6 >= right, it means the answer within 10^-6 of the true value and it will be accepted.

        Time complexity:
        O(NlogM), where N is station length and M is st[N - 1] - st[0]
        """

        # sort the station by their positions, because they may not be sorted in ascending order.
        stations.sort()
        # set the search space over minimum distance
        # find the minimum distance of two adjacent stations with K stations.
        l = 0
        r = stations[-1] - stations[0]
        # when the true value is in the range of 1e-6
        while r - l >= math.pow(10, -6):
            m = (l + r) / 2
            # given the minimum distance m, how many new stations are needed.
            cnt = self.count(stations, m)
            if K >= cnt:
                r = m
            else:
                l = m
        return (l + r) / 2

    # Given minD, find the number of new station.
    def count(self, stations, minD):
        cnt = 0
        for i in range(len(stations)-1):
            d = stations[i+1] - stations[i]
            # only need extra stations if d > minD
            if d > minD:
                # d = 3.2 minD = 1 we need 3
                # d = 3.0 minD = 1 we need 2
                cnt += int(math.ceil(d*1.0/minD)) - 1
        return cnt

s = Solution()
print(s.minmaxGasDist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
