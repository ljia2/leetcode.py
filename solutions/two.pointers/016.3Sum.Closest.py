class Solution:
    def threeSumClosest(self, nums, target):
        """
        Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
        Return the sum of the three integers. You may assume that each input would have exactly one solution.

        Example:

        Given array nums = [-1, 2, 1, -4], and target = 1.

        The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_diff = -1
        for left in range(len(nums)-2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid, right = left + 1, len(nums)-1
            while mid < right:
                sum = nums[left] + nums[mid] + nums[right]

                diff = nums[left] + nums[mid] + nums[right] - target
                if min_diff < 0 or abs(diff) < min_diff:
                    min_diff = abs(diff)
                    result = sum

                if diff == 0:
                    mid += 1
                    while mid < right and nums[mid] == nums[mid-1]:
                        mid += 1
                    right -= 1
                    while right > mid and nums[right] == nums[right+1]:
                        right -= 1

                elif diff < 0:
                    mid += 1
                    while mid < right and nums[mid] == nums[mid-1]:
                        mid += 1

                elif diff > 0:
                    right -= 1
                    while right > mid and nums[right] == nums[right+1]:
                        right -= 1
        return result


s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1))