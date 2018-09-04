class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        house_num = len(nums)
        max_rob = [0] * len(nums)
        for i in range(house_num):
            if i == 0:
                max_rob[i] = nums[i]
            elif i == 1:
                max_rob[i] = max(nums[0], nums[1])
            else:
                max_rob[i] = max(max_rob[i-1], max_rob[i-2] + nums[i])
        return max_rob[house_num-1]


class SolutionII:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        house_num = len(nums)
        include = 0
        exclude = 0
        for i in range(house_num):
            temp_include = include
            include = exclude + nums[i]
            exclude = max(temp_include, exclude)
        return max(include, exclude)