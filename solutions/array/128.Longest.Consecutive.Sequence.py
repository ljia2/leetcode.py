class Solution:
    def longestConsecutive(self, nums):
        """
        Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

        Your algorithm should run in O(n) complexity.

        Example:

        Input: [100, 4, 200, 1, 3, 2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

        :type nums: List[int]
        :rtype: int

        convert nums to set.

        iterate over each number n that n - 1 not in set.
        Then expansion from n + 1 until n + k not in set, update length k with max_length.

        """
        if nums is None or len(nums) == 0:
            return 0
        ans = 0
        num_set = set(nums)
        for num in nums:
            # always find the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                length = 1
                # check whether there is a sequence in nums
                while current_num + 1 in num_set:
                    length += 1
                    current_num += 1
                # update the answer
                ans = max(ans, length)
        return ans
