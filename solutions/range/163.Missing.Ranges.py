class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper],
        return its missing ranges.

        Example:

        Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
        Output: ["2", "4->49", "51->74", "76->99"]
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        results = []
        if not nums:
            results.append((lower, upper))
        else:
            if nums[0] > lower:
                results.append((lower, nums[0]-1))
            start = 0
            while start < len(nums):
                end = start
                # note that we use <=, because [1, 1, 1] is a number of 1. 
                while end < len(nums)-1 and nums[end+1] <= nums[end] + 1:
                    end += 1
                # (start, end) is a continuous interval
                if end < len(nums) - 1:
                    start = end + 1
                    results.append((nums[end]+1, nums[start]-1))

                else:
                    if nums[end] < upper:
                        results.append((nums[end]+1, upper))
                    break
        return list(map(lambda x: str(x[0]) + "->" + str(x[1]) if x[0] < x[1] else str(x[0]), results))
