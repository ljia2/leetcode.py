class Solution:
    def maxProduct(self, nums):
        """
        Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
        which has the largest product.

        Example 1:

        Input: [2,3,-2,4]
        Output: 6
        Explanation: [2,3] has the largest product 6.
        Example 2:

        Input: [-2,0,-1]
        Output: 0
        Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

        :type nums: List[int]
        :rtype: int
        """
        # dp[i] stores the max/min product of any subarray of nums[:i+1] using nums[i]
        dp = [(0, 0)] * len(nums)
        dp[0] = (nums[0], nums[0])
        for i in range(1, len(nums), 1):
            pre_max, pre_min = dp[i-1]
            cmax = max(max(pre_max * nums[i], nums[i]), pre_min * nums[i])
            cmin = min(min(pre_min * nums[i], nums[i]), pre_max * nums[i])
            dp[i] = (cmax, cmin)
        return max(map(lambda x: x[0], dp))


s = Solution()
print(s.maxProduct([-2,-1,0]))
