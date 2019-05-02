import bisect


class Solution(object):
    def searchRange(self, nums, target):
        """
        Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

        Your algorithm's runtime complexity must be in the order of O(log n).

        If the target is not found in the array, return [-1, -1].

        Example 1:

        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]
        Example 2:

        Input: nums = [5,7,7,8,8,10], target = 6
        Output: [-1,-1]

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        # lower bound
        lindex = bisect.bisect_left(nums, target)
        if lindex < len(nums) and nums[lindex] == target:
            # target is found, then find upper bound
            rindex = bisect.bisect_right(nums, target)
            return [lindex, rindex-1]
        else:
            # target is not found.
            return [-1, -1]
