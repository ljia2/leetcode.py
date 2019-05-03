class Solution(object):
    def search(self, nums, target):
        """
        Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

        (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

        You are given a target value to search. If found in the array return true, otherwise return false.

        Example 1:

        Input: nums = [2,5,6,0,0,1,2], target = 0
        Output: true
        Example 2:

        Input: nums = [2,5,6,0,0,1,2], target = 3
        Output: false
        Follow up:

        This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
        Would this affect the run-time complexity? How and why?

        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        if not nums:
            return False
        l = 0
        r = len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return True

            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m + 1
            elif nums[m] < nums[r-1]:
                if nums[m] < target <= nums[r-1]:
                    l = m + 1
                else:
                    r = m
            else:
                l += 1

        if l >= len(nums) or nums[l] != target:
            return False

        return True

s = Solution()
print(s.search([2,5,6,0,0,1,2], 3))
print(s.search([1,3,1,1], 3))