class Solution:
    def findNumberOfLIS(self, nums):
        """
        Given an unsorted array of integers, find the number of longest increasing subsequence.

        Example 1:
        Input: [1,3,5,4,7]
        Output: 2
        Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
        Example 2:
        Input: [2,2,2,2,2]
        Output: 5
        Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
        Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

        :type nums: List[int]
        :rtype: int9\
        """
        if not nums:
           return 0

        dp = [(1, 1)] * len(nums)
        global_max = 1
        for i in range(1, len(nums)):
           # initialize the max length of 1, find the longest subsequence ending at i
           maxl = 1
           for j in range(0, i):
               if nums[i] > nums[j]:
                   ll, lc = dp[j]
                   if maxl < ll + 1:
                       maxl = ll + 1

           if maxl > 1: # find a longest subsequence ending with i, exclusing itself.
               maxc = 0
               for j in range(0, i):
                   ll, lc = dp[j]
                   if nums[i] > nums[j] and ll + 1 == maxl:
                       maxc += lc
               dp[i] = (maxl, maxc)

           if global_max < maxl:
               global_max = maxl

        return sum(map(lambda x: x[1], list(filter(lambda x: x[0] == global_max, dp))))

class DPSolution:
   def findNumberOfLIS(self, nums):
        """
        Given an unsorted array of integers, find the number of longest increasing subsequence.

        Example 1:
        Input: [1,3,5,4,7]
        Output: 2
        Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
        Example 2:
        Input: [2,2,2,2,2]
        Output: 5
        Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
        Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

        :type nums: List[int]
        :rtype: int9\
        """
        if not nums:
            return 0

        lis = [1] * len(nums) # length of longest subsequence ending with i, initializing of 1
        nlis = [1] * len(nums) # length of longest subsequence ending with i, initilizing of 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if lis[j] + 1 > lis[i]: # find out a longer subsequence ending at i
                        lis[i] = lis[j] + 1
                        nlis[i] = nlis[j]
                    elif lis[i] == lis[j] + 1: # find out anther set of longest subsequences ending at i
                        nlis[i] += nlis[j]
        max_length = max(lis)
        count = 0
        for i in range(len(lis)):
            if lis[i] == max_length:
                count += nlis[i]
        return count

s = DPSolution()
#print(s.findNumberOfLIS([1, 3, 5, 4, 7]))
print(s.findNumberOfLIS([2, 2, 2, 2, 2]))
#print(s.findNumberOfLIS([1,2,4,3,5,4,7,2]))