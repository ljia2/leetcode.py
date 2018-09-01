class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        else:
            results = []
            start = 0
            while start < len(nums):
                end = start
                while end < len(nums)-1 and nums[end + 1] == nums[end] + 1:
                    end += 1
                if end < len(nums) - 1:
                    results.append((nums[start], nums[end]))
                    start = end + 1
                else:
                    results.append((nums[start], nums[end]))
                    break
            return list(map(lambda x: str(x[0]) + "->" + str(x[1]) if x[0] < x[1] else str(x[0]), results))