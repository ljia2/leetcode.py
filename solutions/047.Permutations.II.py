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
        self.dfs(nums, 0, len(nums), used, permutation, ans)
        return ans

    def dfs(self, nums, level, target_level, used, permutation, ans):
        if level == target_level:
            ans.append(permutation.copy())
            return
        else:
            # there are duplicated numbers, if a number has already handled on level, we do not need handle the same number at the same level.
            handled = set()
            for i in range(len(nums)):
                if used[i]:
                    continue
                if nums[i] in handled:
                    continue
                used[i] = True
                permutation.append(nums[i])
                handled.add(nums[i])
                self.dfs(nums, level+1, target_level, used, permutation, ans)
                used[i] = False
                permutation.pop()
            return