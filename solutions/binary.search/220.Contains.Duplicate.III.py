import bisect

class Solution: # TLE
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        Given an array of integers, find out whether there are two distinct indices i and j in the array
        such that the absolute difference between nums[i] and nums[j] is at most t
        and the absolute difference between i and j is at most k.

        Example 1:

        Input: nums = [1,2,3,1], k = 3, t = 0
        Output: true
        Example 2:

        Input: nums = [1,0,1,1], k = 1, t = 2
        Output: true
        Example 3:

        Input: nums = [1,5,9,1,5,9], k = 2, t = 3
        Output: false

        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool

        using a sorted sliding window sized of k + 1 to scan array
        """
        if len(nums) < 2 or k == 0:
            return False

        sw = []
        for i in range(len(nums)):
            # remove the earliest element from sliding window
            if i > k:
                index = bisect.bisect_left(sw, nums[i-k-1])
                sw.pop(index)

            index = bisect.bisect_left(sw, nums[i])
            if index > 0:
                prev = sw[index-1]
            else:
                prev = -float("inf")
            if index < len(sw):
                succ = sw[index]
            else:
                succ = float("inf")

            if abs(nums[i] - succ) <= t or abs(nums[i] - prev) <= t:
                return True
            else:
                bisect.insort_left(sw, nums[i])

        return False
s = Solution()
#print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
#print(s.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))
print(s.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))