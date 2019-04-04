class Solution:
    def summaryRanges(self, nums):
        """
        Given a sorted integer array without duplicates, return the summary of its ranges.

        Example 1:

        Input:  [0,1,2,4,5,7]
        Output: ["0->2","4->5","7"]
        Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
        Example 2:

        Input:  [0,2,3,4,6,8,9]
        Output: ["0","2->4","6","8->9"]
        Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        results = []
        start = 0
        while start < len(nums):
            # finding a range starting from start
            end = start
            while end < len(nums)-1 and nums[end + 1] == nums[end] + 1:
                end += 1

            if end < len(nums) - 1:
                # a new range is found
                results.append((nums[start], nums[end]))
                # reset the start
                start = end + 1
            else:
                results.append((nums[start], nums[end]))
                break
        return list(map(lambda x: str(x[0]) + "->" + str(x[1]) if x[0] < x[1] else str(x[0]), results))
