class Solution: # Two Pointers solution
    def minSubArrayLen(self, s, nums):
        """
        Given an array of n positive integers and a positive integer s,
        find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

        Example:

        Input: s = 7, nums = [2,3,1,2,4,3]
        Output: 2
        Explanation: the subarray [4,3] has the minimal length under the problem constraint.
        Follow up:
        If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if not nums or sum(nums) < s:
            return 0

        i = j = 0
        j = 0
        psum1 = 0
        psum2 = nums[0]
        min_length = len(nums) + 1
        while i < len(nums) and j < len(nums):
            ssum = psum2 - psum1
            if ssum < s:
                psum2 += nums[j]
                j += 1
            else:
                length = j - i
                if min_length < length:
                    min_length = length
                psum1 += nums[i]
                i += 1





######################################

import bisect
from collections import OrderedDict

class SolutionII:
    def minSubArrayLen(self, s, nums):
        """
        Given an array of n positive integers and a positive integer s,
        find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

        Example:

        Input: s = 7, nums = [2,3,1,2,4,3]
        Output: 2
        Explanation: the subarray [4,3] has the minimal length under the problem constraint.
        Follow up:
        If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if not nums or sum(nums) < s:
            return 0

        psum = 0
        psum2index = OrderedDict()
        for i in range(len(nums)):
            psum += nums[i]
            psum2index[psum] = i

        sorted_psums = list(psum2index.keys())
        min_length = len(nums)
        for psum in sorted_psums:
            if psum < s:
                continue
            target = psum - s
            # find the psum <= 5 but with the largest index
            index = bisect.bisect_right(sorted_psums, target)
            if index > 0:
                length = psum2index[psum] - psum2index[sorted_psums[index-1]]
            else:
                length = psum2index[psum] + 1
            if min_length > length:
                min_length = length
        return min_length

s = SolutionII()
#print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))