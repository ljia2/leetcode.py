import copy

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

        Note: The solution set must not contain duplicate subsets.

        Example:

        Input: [1,2,2]
        Output:
        [
          [2],
          [1],
          [1,2,2],
          [2,2],
          [1,2],
          []
        ]
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []
        nums.sort()
        ans = [[]]
        for l in range(1, len(nums)+1):
            self.dfs(nums, 0, l, 0, [], ans)
        return ans

    def dfs(self, nums, level, target_level, start, subset, ans):
        if level == target_level:
            ans.append(copy.copy(subset))
            return

        # record whether a number is handled already on this level.
        for i in range(start, len(nums)):
            # if there are duplicates, we only use one at this level.
            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                continue

            subset.append(nums[i])
            self.dfs(nums, level + 1, target_level, i+1, subset, ans)
            subset.pop()
        return

s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
