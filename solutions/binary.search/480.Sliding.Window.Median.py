import bisect

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
        So the median is the mean of the two middle value.

        Examples:
        [2,3,4] , the median is 3

        [2,3], the median is (2 + 3) / 2 = 2.5

        Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
        You can only see the k numbers in the window. Each time the sliding window moves right by one position.
        Your job is to output the median array for each window in the original array.

        For example,
        Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

        Window position                Median
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       1
         1 [3  -1  -3] 5  3  6  7       -1
         1  3 [-1  -3  5] 3  6  7       -1
         1  3  -1 [-3  5  3] 6  7       3
         1  3  -1  -3 [5  3  6] 7       5
         1  3  -1  -3  5 [3  6  7]      6
        Therefore, return the median sliding window as [1,-1,-1,3,5,6].

        Note:
        You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.

        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """

        if not nums:
            return nums
        n = len(nums)
        sw = []
        sorted_sw = []
        ans = []
        for i in range(n):
            if len(sw) < k:
                sw.append(i)
                bisect.insort_left(sorted_sw, nums[i])
            else:
                ans.append(self.median(sorted_sw, k))
                self.update(nums, sw, sorted_sw, i)

        # do not forget the median of last sliding window
        ans.append(self.median(sorted_sw, k))
        return ans


    def update(self, nums, sw, sorted_sw, i):
        pi = sw.pop(0)
        di = bisect.bisect_left(sorted_sw, nums[pi])
        sorted_sw.pop(di)
        sw.append(i)
        bisect.insort_right(sorted_sw, nums[i])
        return

    def median(self, sorted_sw, k):
        if k % 2 == 1:
            return sorted_sw[k//2]
        else:
            return (sorted_sw[k//2-1] + sorted_sw[k//2]) / 2.0

s = Solution()
print(s.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
