class Solution(object):
    def wiggleSort(self, nums):
        """
        Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

        Example:

        Input: nums = [3,5,2,1,6,4]
        Output: One possible answer is [3,5,1,6,2,4]

        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        1) sort array in-place
        2) for i in range(1, n, 2):
            swap nums[i] and nums[i+1]

        T: O(nlogn)
        """
        if not nums:
            return nums

        nums.sort()
        if len(nums) < 3:
            return nums
        for i in range(1, len(nums), 2):
            if i+1 < len(nums):
                nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums

class BestSolution(object):
    def wiggleSort(self, nums):
        """
        Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

        Example:

        Input: nums = [3,5,2,1,6,4]
        Output: One possible answer is [3,5,1,6,2,4]

        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        T: O(n)

        """
        if not nums:
            return nums

        n = len(nums)
        for i in range(n-1):
            if i % 2 == 1 and nums[i] < nums[i+1]:
                # hint: nums[i-1] <= nums[i] < nums[i+1], swap nums[i] and nums[i+1] make nums[:i+2] still wiggle sorted.
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif i % 2 == 0 and nums[i] > nums[i+1]:
                # hint: nums[i-1] >= nums[i] > nums[i+1], swap nums[i] and nums[i+1] make nums[:i+2] still wiggle sorted.
                nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums