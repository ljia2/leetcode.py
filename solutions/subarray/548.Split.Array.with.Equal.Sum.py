from collections import defaultdict

class Solution(object):
    def splitArray(self, nums):
        """
        Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

        0 < i, i + 1 < j, j + 1 < k < n - 1
        Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
        where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.

        Example:
        Input: [1,2,1,2,1,2,1]
        Output: True

        Explanation:
        i = 1, j = 3, k = 5.
        sum(0, i - 1) = sum(0, 0) = 1
        sum(i + 1, j - 1) = sum(2, 2) = 1
        sum(j + 1, k - 1) = sum(4, 4) = 1
        sum(k + 1, n - 1) = sum(6, 6) = 1

        :type nums: List[int]
        :rtype: bool

        1) convert to prefix_sum
        2) similar to 4Sum problem with sepicial conditions

        """

        if not nums or len(nums) < 7:
            return False

        prefix_sum = 0
        prefix_sums = []
        for num in nums:
            prefix_sum += num
            prefix_sums.append(prefix_sum)

        n = len(nums)
        for j in range(3, n - 3):
            sum_candidate = set()
            for i in range(1, j-1):
                # (0, i-1) sum == (i+1, j) sum
                if prefix_sums[i-1] == prefix_sums[j-1] - prefix_sums[i]:
                    sum_candidate.add(prefix_sums[i-1])
                for k in (j + 2, n - 1):
                    # sum (n-1, k+1) == sum (k-1, j+1)
                    # sum (k-1, j+1) exists in the set.
                    if prefix_sums[n - 1] - prefix_sums[k] == prefix_sums[k - 1] - prefix_sums[j] and prefix_sums[k - 1] - prefix_sums[j] in sum_candidate:
                        return True
        return False


s = Solution()
#print(s.splitArray([1,2,1,2,1,2,1]))
print(s.splitArray([-1,0,-1,0,-1,0,-1]))