class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.rangeMap = dict()
        for i in range(len(nums)):
            for j in range(i, len(nums), 1):
                if i == j:
                    self.rangeMap[(i, j)] = nums[i]
                else:
                    self.rangeMap[(i, j)] = sum(nums[i:j+1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.rangeMap[(i, j)]



class NumArray2:

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