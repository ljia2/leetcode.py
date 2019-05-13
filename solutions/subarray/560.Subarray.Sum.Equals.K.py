# class Solution: # Brute Force
#     def subarraySum(self, nums, k):
#         """
#
#         Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
#         Example 1:
#         Input:nums = [1,1,1], k = 2
#         Output: 2
#         Note:
#         The length of the array is in range [1, 20,000].
#         The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
#
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 sum = 0
#                 for k in range(i, j+1):
#                     sum += nums[k]
#                 if sum == k:
#                     count += 1
#         return count
#
# class SolutionII: # Brute Force without repeated computation
#     def subarraySum(self, nums, k):
#         """
#
#         Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
#         Example 1:
#         Input:nums = [1,1,1], k = 2
#         Output: 2
#         Note:
#         The length of the array is in range [1, 20,000].
#         The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
#
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         count = 0
#         for i in range(len(nums)):
#             presum = 0
#             for j in range(i, len(nums)):
#                 presum += nums[j]
#                 if presum == k:
#                     count += 1
#         return count

from collections import defaultdict


# class SolutionIII:
#     def subarraySum(self, nums, k):
#         """
#
#         Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
#         Example 1:
#         Input:nums = [1,1,1], k = 2
#         Output: 2
#         Note:
#         The length of the array is in range [1, 20,000].
#         The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
#
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#
#         Hint: 20000 indicate optimal linear solution
#
#         when calculate the subarray sum, we need to the prefixsum trick:
#
#         to find the subarray summing to k, i.e. prefix_sum[j] - prefix_sum[i] == k where j > i
#
#         1. use hashtable to store the prefix sum of nums[:i] as key and indices list as value
#         2. scan the array by calculating prefix_sum of nums[:i], s and use k+s as key to query hashtable to ensure there exits j > i with the key
#         moreover, we need to check whether s == k or not.
#         """
#
#         prefix_sum = defaultdict(list)
#         psum = 0
#         for i in range(len(nums)):
#             psum += nums[i]
#             prefix_sum[psum].append(i)
#
#         count = 0
#         psum = 0
#         for i in range(len(nums)):
#             psum += nums[i]
#
#             if psum == k:
#                 count += 1
#
#             if k + psum in prefix_sum.keys():
#                 for j in prefix_sum[k-psum]:
#                     if j > i:
#                         count += 1
#         return count


class Solution:
    def subarraySum(self, nums, k):
        """

        Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

        Example 1:
        Input:nums = [1,1,1], k = 2
        Output: 2
        Note:
        The length of the array is in range [1, 20,000].
        The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

        :type nums: List[int]
        :type k: int
        :rtype: int

        Hint: 20000 indicate optimal linear solution

        when calculate the subarray sum, we need to the prefixsum trick:


        to find the subarray summing to k, i.e. prefix_sum[j] - prefix_sum[i] == k where j > i


        for each j of prefix_sum:
            <i, j> where prefix_sum[i] + k = prefix_sum[j] where i < j

        """
        prefix_sum = [0]
        psum = 0
        for i in range(len(nums)):
            psum += nums[i]
            prefix_sum.append(psum)

        count = 0
        # key: prefix_sum; value: the frequency of key before j (i.e. # of subarraies summing to key before j)
        prefix_dict = dict()
        # Note: there is one empty subarray whose sum is zero.
        prefix_dict[0] = 1
        for j in range(1, len(prefix_sum)):
            target = prefix_sum[j] - k
            if target in prefix_dict.keys():
                count += prefix_dict[target]
            # update the frequency by 1
            prefix_dict[prefix_sum[j]] = prefix_dict.get(prefix_sum[j], 0) + 1
        return count

###  What if all numbers are positive, we can use two pointer!!!
class VarationSolution:
    def subarraySum(self, nums, k):
        if k < 0:
            return 0
        if not nums:
            return 0

        numsum = 0
        i = 0
        ans = 0
        for num in nums:
            numsum += num

            while numsum > k:
                numsum -= nums[i]
                i += 1

            if numsum == k:
                ans += 1
        return ans

