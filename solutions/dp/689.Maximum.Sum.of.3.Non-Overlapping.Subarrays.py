import copy
# class DPSolution(object): # TLE
#     def maxSumOfThreeSubarrays(self, nums, k):
#         """
#         In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
#
#         Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
#
#         Return the result as a list of indices representing the starting position of each interval (0-indexed).
#         If there are multiple answers, return the lexicographically smallest one.
#
#         Example:
#         Input: [1,2,1,2,6,7,5,1], 2
#         Output: [0, 3, 5]
#         Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
#         We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
#
#         Note:
#         nums.length will be between 1 and 20000.
#         nums[i] will be between 1 and 65535.
#         k will be between 1 and floor(nums.length / 3).
#
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#
#         the start of 1/2/3 subsarry must start from 0, k, 2*k.
#
#         use dp[i][0] store the biggest subarray of size k up to i.
#         use dp[i][1] store the biggest sum of two k-sized subarrays up to i.
#         use dp[i][2] store the biggest sum of three k-sized subarrays up to i.
#
#         """
#
#         if not nums or k <= 0:
#             raise Exception("Invalid Exception!")
#
#         n = len(nums)
#         if k*3 > n:
#             return []
#
#         dp = [[(0, [])] * 4 for _ in range(n)]
#         # transition
#         for j in range(1, 4):
#             for i in range(j*k-1, n):
#                 if dp[i-k][j-1][0] + sum(nums[i-k+1:i+1]) > dp[i-1][j][0]:
#                     lans = copy.copy(dp[i-k][j-1][1])
#                     lans.append(i-k+1)
#                     dp[i][j] = (dp[i-k][j-1][0] + sum(nums[i-k+1:i+1]), lans)
#                 else:
#                     dp[i][j] = (dp[i-1][j][0], copy.copy(dp[i-1][j][1]))
#
#         return dp[n-1][3][1]
#
# s = DPSolution()
# print(s.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))
# print(s.maxSumOfThreeSubarrays([7,13,20,19,19,2,10,1,1,19], 3))


class DPSolutionII(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

        Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

        Return the result as a list of indices representing the starting position of each interval (0-indexed).
        If there are multiple answers, return the lexicographically smallest one.

        Example:
        Input: [1,2,1,2,6,7,5,1], 2
        Output: [0, 3, 5]
        Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
        We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

        Note:
        nums.length will be between 1 and 20000.
        nums[i] will be between 1 and 65535.
        k will be between 1 and floor(nums.length / 3).

        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        dp[i][0] stores the biggest subarray up to i.

        dp[i][1] stores the biggest subarray afterward until i.

        then iterate over i find the biggest, dp[i-1][0] + sum(nums[i:i+k]) + dp[i+k][1]

        """

        if not nums or k <= 0:
            raise Exception("Invalid Exception!")

        n = len(nums)
        if k*3 > n:
            return []

        dp1 = [(0, None)] * n
        dp2 = [(0, None)] * n
        # base case
        dp1[k-1] = (sum(nums[:k]), 0)
        dp2[n-k] = (sum(nums[n-k:n]), n-k)
        # transition
        for i in range(k, n):
            pmax_sum, _ = dp1[i-1]
            max_sum = sum(nums[i-k+1:i+1])
            if max_sum > pmax_sum:
                dp1[i] = (max_sum, i-k+1)
            else:
                dp1[i] = dp1[i-1]

        for i in range(n-k-1, -1, -1):
            smax_sum, _ = dp2[i+1]
            max_sum = sum(nums[i:i+k])
            if max_sum >= smax_sum:
                dp2[i] = (max_sum, i)
            else:
                dp2[i] = dp2[i+1]

        max_sum = 0
        for i in range(k, n-k):
            curr_max_sum = dp1[i-1][0] + dp2[i+k][0] + sum(nums[i:i+k])
            if curr_max_sum > max_sum:
                ans = [dp1[i-1][1], i, dp2[i+k][1]]
                max_sum = curr_max_sum
        return ans

s = DPSolutionII()
print(s.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))
print(s.maxSumOfThreeSubarrays([7,13,20,19,19,2,10,1,1,19], 3))
print(s.maxSumOfThreeSubarrays([4,5,10,6,11,17,4,11,1,3], 1))