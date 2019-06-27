class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
        If there isn't one, return 0 instead.

        Note:
        The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

        Example 1:

        Input: nums = [1, -1, 5, -2, 3], k = 3
        Output: 4
        Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
        Example 2:

        Input: nums = [-2, -1, 2, 1], k = 1
        Output: 2
        Explanation: The subarray [-1, 2] sums to 1 and is the longest.
        Follow Up:
        Can you do it in O(n) time?


        :type nums: List[int]
        :type k: int
        :rtype: int

        Since the elements in array can be negative;

        "The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range" hints presum

        """
        # not 0 return True -> k is None
        if not nums or k is None:
            return 0
        n = len(nums)

        # key presum and value is index.
        # base case: empty string sum == 0; -1 is convenient for length
        psums = {0: -1}
        psum = 0
        ans = float("-inf")
        for i in range(n):
            psum += nums[i]
            target = psum - k
            if target in psums.keys():
                ans = max(ans, i - psums[target])

            # record the first index of prefix_sum
            if psum not in psums.keys():
                psums[psum] = i

        return 0 if ans == float("-inf") else ans

s = Solution()
print(s.maxSubArrayLen([1, -1, 5, -2, 3], 3))
print(s.maxSubArrayLen([-2, -1, 2, 1], 1))