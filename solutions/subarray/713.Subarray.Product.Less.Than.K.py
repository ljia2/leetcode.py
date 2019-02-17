from math import log
import bisect

class Solution:
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

        let us take log of nums and convert to sum less than log(K).
        Say we have a subarray [x1,x2,x3] such that its product is less than k.
        x1*x2*x3 < k. Take log of both sides. log(x1) + log(x2) +log(x3) < log(k).
        Lets transform original nums as nums = [log(x) for x in nums]. Next transform it into a cdf array called cums. Also, k = log(k).

        Now if a subarray from index i to index j is a solution, then we can say: cums[j]-cums[i]+nums[i] < k.

        cums[j]-cums[i]+nums[i]-k < 0 or cums[j]-cums[i]+nums[i]-k <= -1e-12. Say target = k+cums[i]-nums[i]-1e-12,
        then we need to find the largest j such that cums[j] <= target.

        We can use bisect_right to find the rightmost index j such that cums[j] <= target.
        There are strong reasons why we use bisect_right and also what happens when target is in cums or not.

        Example: nums=[1,2,2,2,2,3]. If target is 2.5, bisect_right will return j=5. We would need to adjust and make j=5. If target is 2, bisect_right will return 4 and no adjustment is required.

        Time is Nlog(N) and Space is O(N).
        """
        if not nums or k == 0:
            return 0

        k, nums = log(k), [log(x) for x in nums]

        cums = []
        for x in nums:
            if not cums:
                cums.append(x)
            else:
                cums.append(x+cums[-1])

        ans = 0
        for i in range(len(nums)):
            target = k+cums[i]-nums[i]
            j = bisect.bisect_left(cums, target, i)
            # Adjust index j  when cums[j] != target (i.e. larger).
            if j == len(cums) or cums[j] > target:
                j = j-1
            ans += j-i + 1
        return ans


s = Solution()
print(s.numSubarrayProductLessThanK([10, 5, 2, 6], 100))




