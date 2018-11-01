from heapq import heappush, heappushpop, heappop


class Solution: # Brute Force + Bucket Sorting of abs diff but TLE
    def smallestDistancePair(self, nums, k):
        """
        Given an integer array, return the k-th smallest distance among all the pairs.
        The distance of a pair (A, B) is defined as the absolute difference between A and B.

        Example 1:
        Input:
        nums = [1,3,1]
        k = 1
        Output: 0

        Explanation:
        Here are all the pairs:
        (1,3) -> 2
        (1,1) -> 0
        (3,1) -> 2
        Then the 1st smallest distance pair is (1,1), and its distance is 0.

        Note:
        2 <= len(nums) <= 10000.
        0 <= nums[i] < 1000000.
        1 <= k <= len(nums) * (len(nums) - 1) / 2.

        :type nums: List[int]
        :type k: int
        :rtype: int

        T: O(n^2)
        S: O(max(nums))
        """

        snums = sorted(nums)
        buckets = [0] * (max(snums) + 1)

        for i in range(len(snums)):
            for j in range(i+1, len(snums)):
                buckets[snums[j] - snums[i]] += 1
        freqsum = 0
        for i in range(len(buckets)):
            freqsum += buckets[i]
            if freqsum >= k:
                return i
        return 0

class BSDPSolution:
    def smallestDistancePair(self, nums, k):
        """
        Given an integer array, return the k-th smallest distance among all the pairs.
        The distance of a pair (A, B) is defined as the absolute difference between A and B.

        Example 1:
        Input:
        nums = [1,3,1]
        k = 1
        Output: 0

        Explanation:
        Here are all the pairs:
        (1,3) -> 2
        (1,1) -> 0
        (3,1) -> 2
        Then the 1st smallest distance pair is (1,1), and its distance is 0.

        Note:
        2 <= len(nums) <= 10000.
        0 <= nums[i] < 1000000.
        1 <= k <= len(nums) * (len(nums) - 1) / 2.

        :type nums: List[int]
        :type k: int
        :rtype: int

        binary search + DP

        sort the numbers and find the minimum distance m with k pairs whose distance <= m

        binary search over distance space,
            compute # of pairs whose distance <= m in O(n) (dynamtic programming)


            dp[i]: # pairs whose distance are <= m' using nums[j] - nums[0:i] where j > i.
            dp[i] = dp[i-1] + (j - i - 1) where j is the smallest index where nums[j] - nums[i] > m' (stop)
            dp[n-2] is the ans (because num[n-1] is the maximum number can not be substracted).


        """

        snums = sorted(nums)
        l = 0
        # the largest possible distance
        r = max(snums) - min(snums)
        while l <= r:
            dp = [0] * (len(snums) - 1)
            j = 0
            m = (l + r) // 2
            # i and j are two pointer and thus T: O(n) !!!!
            for i in range(len(snums)-1):
                while j < len(snums) and snums[j] - snums[i] <= m:
                    j += 1
                # Transition
                # only find out how many pair of snums[j] - snums[i] <= m (which is j - i - 1)
                dp[i] = dp[i-1] + (j - i - 1)
            # if there are more than k pairs whose distance <= m.
            # binary search snums[l: m] to find out the smallest space with k pairs
            if dp[len(snums)-2] >= k:
                r = m - 1
            else:
                l = m + 1

        return l

s = BSDPSolution()
print(s.smallestDistancePair([1, 3, 1], 1))


