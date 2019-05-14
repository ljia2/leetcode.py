class Solution(object):
    def moveZeroes(self, nums):
        """
        Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Example:

        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]
        Note:

        You must do this in-place without making a copy of the array.
        Minimize the total number of operations.

        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.



        """
        if not nums or len(nums) == 1:
            return
        n = len(nums)
        i = 0
        while i < n:
            # find the first index of zero
            while i < n and nums[i] != 0:
                i += 1
            # find the first index of non-zero after i.
            j = i + 1
            while j < n and nums[j] == 0:
                j += 1

            if i < j < n:
                # if there is a non-zero after i, swap numbers at i and j
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break

        return


s = Solution()
nums = [0,1,0,3,12]
s.moveZeroes(nums)
print(nums)
