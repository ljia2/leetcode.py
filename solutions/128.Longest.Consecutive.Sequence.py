class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        max_len = 0
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

                if length > max_len:
                    max_len = length
        return max_len
