class Solution(object):
    def combinationSum4(self, nums, target):
        """
        Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

        Example:

        nums = [1, 2, 3]
        target = 4

        The possible combination ways are:
        (1, 1, 1, 1)
        (1, 1, 2)
        (1, 2, 1)
        (1, 3)
        (2, 1, 1)
        (2, 2)
        (3, 1)

        Note that different sequences are counted as different combinations.

        Therefore the output is 7.


        Follow up:
        What if negative numbers are allowed in the given array?
        How does it change the problem?
        What limitation we need to add to the question to allow negative numbers?


        :type nums: List[int]
        :type target: int
        :rtype: int

        Based on the example, it is not combination, it is permutation!!!!
        allow duplication and dfs is not feasible.

        
        """

        if not nums or target <= 0:
            return 0

        ans = [0]
        self.dfs(nums, target, set(), ans)
        return ans[0]

    def dfs(self, nums, target, used, ans):
        if target == 0:
            ans[0] += 1
            return
        if target < 0:
            return

        for i in range(len(nums)):
            if nums[i] in used:
                continue
            used.add(nums[i])
            for j in range(1, target//nums[i] + 1):
                self.dfs(nums, target - nums[i]*j, used, ans)
            used.remove(nums[i])
        return
s = Solution()
print(s.combinationSum4([1, 2, 3], 4))