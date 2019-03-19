class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Given an array of n integers nums and a target, find the number of index triplets i, j, k
        with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

        Example:

        Input: nums = [-2,0,1,3], and target = 2

        Output: 2

        Explanation: Because there are two triplets which sums are less than 2:
                     [-2,0,1]
                     [-2,0,3]


        Follow up: Could you solve it in O(n2) runtime?
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
                    # when move mid to right, must need a num smaller than the original nums[right];
                    # do not reset right.
                    mid += 1
        return result_cnt






