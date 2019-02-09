2class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result_cnt = 0
        for left in range(len(nums)-2):
            mid, right = left + 1, len(nums)-1
            while mid < right:
                sum = nums[left] + nums[mid] + nums[right]
                if sum < target:
                    result_cnt += right - mid
                    mid += 1
                    right = len(nums)-1
                elif sum > target:
                    right -= 1
                elif sum == target:
                    right -= 1
                    # moving right from high to low to find the first num smaller than nums[right]
                    while mid < right and nums[right] == nums[right+1]:
                        right -= 1
                    result_cnt += right-mid
                    # when move mid to right, must need a num smaller than the original nums[right]; do not reset right.
                    mid += 1
        return result_cnt




