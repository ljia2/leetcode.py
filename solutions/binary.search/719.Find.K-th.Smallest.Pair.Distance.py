import bisect
class Solution:
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

        2 <= len(nums) <= 10000 hints at most O(nlogn) algorithm
        0 <= nums[i] < 1000000 hints binary search over value space

        let count(nums, d) denote the number of pair distances among nums that are no greater than d, then the K-th smallest pair distance will be the smallest integer such that count(d) >= K. Similar to lower_bound (bisect_left).

        1) binary search over (0, m) where m = max(nums) - min(nums)
           1.1) for a candidate distance d.
                1.1.1) le = count(nums, d).
                1.1.2) if le == k:
                          return d
                        if le > k
                         r = d
                        else:
                         l = d
           return l
        """

        nums.sort()
        l = 0
        r = max(nums)
        # again l and r are searching integer space.
        # find the least distance that have k distances less than or equal to it.
        while l < r :
            m = (l + r) // 2
            le = self.count(nums, m)
            if le >= k:
                r = m
            else:
                l = m + 1
        return l

    def count(self, nums, m):
        ans = 0
        for i in range(len(nums)):
            j = bisect.bisect_right(nums, nums[i] + m)
            # j is first index nums[j] > nums[i] + m
            if j > 1:
                ans += j - 1 - i
        return ans

s = Solution()
print(s.smallestDistancePair([1, 3, 1], 2))