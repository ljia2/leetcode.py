import bisect
class Solution:
    def countRangeSum(self, nums, lower, upper):
        """
        Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
        Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

        Note:
        A naive algorithm of O(n2) is trivial. You MUST do better than that.

        Example:

        Input: nums = [-2,5,-1], lower = -2, upper = 2,
        Output: 3
        Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.

        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        presums = []
        presum = 0
        ans = 0
        for i in range(len(nums)):
            presum += nums[i]
            # a presum starting with 0
            if lower <= presum <= upper:
                ans += 1

            if not presums:
                bisect.insort_left(presums, presum)
            else:
                # looking for presums <= lt
                lt = presum - lower
                # looking for presums >= ut
                ut = presum - upper

                # lt >= presum >= ut

                # presums[:lindex] >= lt
                lindex = bisect.bisect_right(presums, lt)
                # presums[uindex:] >= ut
                uindex = bisect.bisect_left(presums, ut)

                if uindex >= 0 and lindex - 1 < len(presums):
                    ans += lindex - uindex # lindex - 1 - uindex + 1
                bisect.insort_left(presums, presum)
        return ans

s = Solution()
#print(s.countRangeSum([-2, 5, -1], -2, 2))
print(s.countRangeSum([0, 0], 0, 0))