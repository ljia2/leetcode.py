class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

        Example 1:

        Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
        Output: True
        Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

        Note:

        1 <= k <= len(nums) <= 16.
        0 < nums[i] < 10000.

        :type nums: List[int]
        :type k: int
        :rtype: bool

        given the nums size is just 16, hints for backtracking search via dfs.
        """

        if not nums or k <= 0:
            return False
        # quick case 1: k == 1
        if k == 1:
            return True

        # quick case 2: sum is not divible by k.
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k
        nums.sort()
        # quick case 3, a number bigger than target
        if nums[-1] > target:
            return False

        # if nums have a single num == target, itself is a partition
        index = len(nums)-1
        while index > -1 and nums[index] == target:
            index -= 1
            k -= 1

        # then partition nums[0:index+1] into k partitions
        subsets = [0] * k
        # dfs/backtracking for each number starting 0 to index
        return self.partition(subsets, nums, index, target)

    def partition(self, subsets, nums, end, target):
        if end < 0:
            return True

        for i in range(len(subsets)):
            if subsets[i] + nums[end] > target:
                continue

            # typical backtracking
            subsets[i] += nums[end]
            if self.partition(subsets, nums, end-1, target):
                return True
            subsets[i] -= nums[end]

        return False


s = Solution()
print(s.canPartitionKSubsets([4,3,2,3,5,2,1], 4))