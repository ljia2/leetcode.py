class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # sum[i] stores the sum from 0 to i-1
        self.sum = [0] * len(nums)
        for i in range(1, len(nums)+1, 1):
            self.sum[i] = self.sum[i-1] + nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum[j+1] - self.sum[i]
