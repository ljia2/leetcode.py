class DPSolution(object):
    def combinationSum4(self, nums, target):
        """
        Given an integer array with all positive numbers and no duplicates,
        find the number of possible combinations that add up to a positive integer target.

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

        Based on the example, it is not combination, it is permutation!!!! Allowing duplication, pure dfs is not feasible.

        Moreover, the count problem can be used by dynamtic programming.

        dp[k] stores the # of possible combinations summing up to k.

        So we know that target is the sum of numbers in the array.
        Imagine we only need one more number to reach target, this number can be any one in the array, right?


        So the # of combinations of target, comb[target] = sum(comb[target - nums[i]]), where 0 <= i < nums.length, and target >= nums[i].

        In the example given, we can actually find the # of combinations of 4 with the # of combinations of 3(4 - 1), 2(4- 2) and 1(4 - 3).
        As a result, comb[4] = comb[4-1] + comb[4-2] + comb[4-3] = comb[3] + comb[2] + comb[1].

        Then think about the base case. Since if the target is 0, there is only one way to get zero, which is using 0, we can set comb[0] = 1.

        very similar to coin change problem? LC322

        """
        if not nums or target <= 0:
            return 0

        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if num > i:
                    continue
                dp[i] += dp[i - num]
        return dp[target]

s = DPSolution()
print(s.combinationSum4([1, 2, 3], 4))

# class DFSSolution(object): # TLE
#     def combinationSum4(self, nums, target):
#         """
#         Given an integer array with all positive numbers and no duplicates,
#         find the number of possible combinations that add up to a positive integer target.
#
#         Example:
#
#         nums = [1, 2, 3]
#         target = 4
#
#         The possible combination ways are:
#         (1, 1, 1, 1)
#         (1, 1, 2)
#         (1, 2, 1)
#         (1, 3)
#         (2, 1, 1)
#         (2, 2)
#         (3, 1)
#
#         Note that different sequences are counted as different combinations.
#
#         Therefore the output is 7.
#
#         Follow up:
#         What if negative numbers are allowed in the given array?
#         How does it change the problem?
#         What limitation we need to add to the question to allow negative numbers?
#
#
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#
#         Based on the example, it is not combination, it is permutation!!!! Allowing duplication, pure dfs is not feasible.
#
#         We need leverage DFS + memory
#
#         """
#         if not nums or target <= 0:
#             return 0
#
#         dp = [0] * (target + 1)
#         dp[0] = 1
#         nums.sort()
#         self.dfs(nums, target, dp)
#         return dp[target]
#
#     def dfs(self, nums, target, dp):
#         if dp[target] != 0:
#             return dp[target]
#         ans = 0
#         for i in range(len(nums)):
#             if nums[i] > target:
#                 break
#             ans += self.dfs(nums, target - nums[i], dp)
#         dp[target] = ans
#         return ans
#
# s = DFSSolution()
# print(s.combinationSum4([3, 33, 333], 10000))
