class Solution:
    def permuteUnique(self, nums):
        """

        Given a collection of numbers that might contain duplicates, return all possible unique permutations.

        Example:

        Input: [1,1,2]
        Output:
        [
          [1,1,2],
          [1,2,1],
          [2,1,1]
        ]

        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        ans = []
        used = [False] * len(nums)
        permutation = []
        nums.sort()
        self.dfs(nums, 0, len(nums), used, permutation, ans)
        return ans

    def dfs(self, nums, level, target_level, used, permutation, ans):
        if level == target_level:
            ans.append(permutation.copy())
            return
        else:
            for i in range(len(nums)):
                if used[i]:
                    continue
                # there are duplicated numbers, if a number has already handled on level,
                # we do not need handle the same number at the same level.
                if i + 1 < len(nums) and nums[i] == nums[i+1]:
                    continue

                used[i] = True
                permutation.append(nums[i])
                self.dfs(nums, level+1, target_level, used, permutation, ans)
                used[i] = False
                permutation.pop()
            return
