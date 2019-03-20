class TwoPointerSolution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        Your are given an array of positive integers nums.

        Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

        Example 1:

        Input: nums = [10, 5, 2, 6], k = 100
        Output: 8
        Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
        Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
        Note:

        0 < nums.length <= 50000.
        0 < nums[i] < 1000.
        0 <= k < 10^6.

        :type nums: List[int]
        :type k: int
        :rtype: int

        how about two pointers, start and end.
        since all elements are positive and production is non-decreasing.

        /**
         * The idea is always keep an max-product-window less than K;
         * Every time add a new number on the right(j), reduce numbers on the left(i), until the subarray product fit less than k again, (subarray could be empty);
         * Each step introduces x new subarrays, where x is the size of the current window (j + 1 - i);
         * example:
         * for window (5, 2, 6), when 6 is introduced, it add 3 new subarray:
         *       (6)
         *    (2, 6)
         * (5, 2, 6)
         */

         LC159
        """
        if k == 0 or not nums:
            return 0

        start = 0
        prod = 1
        ans = 0
        for end in range(len(nums)):
            # prod is the prod of subarray from start to (new) end
            prod *= nums[end]
            # keep retracting start until prod < k
            while start <= end and prod >= k:
                prod /= nums[start]
                start += 1
            # subarray from start to end whose prod < k
            # it generates end - start + 1 qualified subarries.
            ans += end - start + 1
        return ans