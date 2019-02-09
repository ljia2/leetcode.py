class Solution:
    def findLengthOfLCIS(self, nums):
        """
        Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

        Example 1:
        Input: [1,3,5,4,7]
        Output: 3
        Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
        Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
        Example 2:
        Input: [2,2,2,2,2]
        Output: 1
        Explanation: The longest continuous increasing subsequence is [2], its length is 1.
        Note: Length of the array will not exceed 10,000 => O(n)
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        start = 0
        max_length = 0
        while start < len(nums):
            length = 1
            while start + 1 < len(nums) and nums[start+1] > nums[start]:
                start += 1
                length += 1
            if max_length < length:
                max_length = length
            start += 1
        return max_length

