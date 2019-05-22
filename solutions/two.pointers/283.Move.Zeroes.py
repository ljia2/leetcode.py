class OptimalSolution(object):
    def moveZeroes(self, nums):
        """
        Given an array nums, write a function to move all 0's to the end of it
        while maintaining the relative order of the non-zero elements.

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
        # from 0 to j - 1 are non-zero while j is the next position for non-zero
        # for j to i-1 are all zeros
        # for i to end are mixed.
        # always swap i if nums[1] != j with j.
        i = j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i == j:
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
        return


s = OptimalSolution()
nums = [0,1,0,3,12]
s.moveZeroes(nums)
print(nums)

