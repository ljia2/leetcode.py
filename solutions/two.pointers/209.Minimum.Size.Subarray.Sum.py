class SolutionI: # Two Pointers solution
    def minSubArrayLen(self, s, nums):
        """
        Given an array of n positive integers and a positive integer s,
        find the minimal length of a contiguous subarray of which the sum ≥ s.
        If there isn't one, return 0 instead.

        Example:

        Input: s = 7, nums = [2,3,1,2,4,3]
        Output: 2
        Explanation: the subarray [4,3] has the minimal length under the problem constraint.
        Follow up:
        If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

        :type s: int
        :type nums: List[int]
        :rtype: int

        give an array of positive numbers, we can use two pointers, because presume is strictly increasing.

        """

        if not nums or sum(nums) < s:
            return 0

        i = -1
        j = 0
        psum1 = 0
        psum2 = nums[0]
        min_length = len(nums) + 1
        while i < len(nums) and j < len(nums):
            ssum = psum2 - psum1
            if ssum < s:
                j += 1
                if j < len(nums):
                    psum2 += nums[j]
            else:
                length = j - i
                if min_length > length:
                    min_length = length

                i += 1
                if i < len(nums):
                    psum1 += nums[i]
        return min_length


s = SolutionI()
print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))