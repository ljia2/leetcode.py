class Solution:
    def findLengthOfLCIS(self, nums):
        """
        Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

        Example 1:
        Input: [1,3,5,4,7]
        Output: 3
        Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
        Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.

        Example 2:
        Input: [2,2,2,2,2]
        Output: 1
        Explanation: The longest continuous increasing subsequence is [2], its length is 1.
        Note: Length of the array will not exceed 10,000 => O(n)
        :type nums: List[int]
        :rtype: int

        similar to LC128.
        """

        if not nums:
            return 0

        start = 0
        max_length = 0
        while start < len(nums):
            length = 1
            while start + 1 < len(nums) and nums[start+1] > nums[start]:
                start += 1
                length += 1
            if max_length < length:
                max_length = length
            start += 1
        return max_length

#### Follow up: what if the first and the last number is different at most one
class VarationSolution:
    def findLengthOfLCIS(self, nums):
        """

        :type nums: List[int]
        :rtype: int

        find the longest increasing subsequence where the adjaencet num indexes are apart at most one gap.
        not necessary continous

        DP

        """

        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return 1

        # the longest increasing subsequence with at most one gap ending at previous previous index
        pprev = 1
        # the longest increasing subsequence with at most one gap ending at previous index
        prev = 2 if nums[0] < nums[1] else 1
        ans = prev

        for i in range(2, n):
            tmp = 1
            if nums[i-2] < nums[i] and pprev + 1 > tmp:
                tmp = pprev + 1

            if nums[i-1] < nums[i] and prev + 1 > tmp:
                tmp = prev + 1

            ans = max(ans, tmp)
            pprev = prev
            prev = tmp

        return ans


class VarationSolutionII:
    def findLengthOfLCIS(self, nums, k):
        """

        :type nums: List[int]
        :rtype: int

        find the longest increasing subsequence where the adjaencet num indexes are apart at most K gap.
        not necessary continous

        dp[i] stores the longes increasing qualified subsequence ending at i.

        """

        if not nums:
            return 0

        n = len(nums)


        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i-k-1, i-1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
