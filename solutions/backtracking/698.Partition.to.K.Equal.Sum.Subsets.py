class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        Given an array of integers nums and a positive integer k,

        return a set of k subsets whose sums are all equal. otherwise return []

        Example 1:

        Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
        Output: True
        Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

        Note:

        1 <= k <= len(nums) <= 16.
        0 < nums[i] < 10000.

        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]

        given the nums size is just 16, hints for backtracking search via dfs.
        """

        if not nums or k <= 0:
            return []
        # quick case 1: k == 1
        if k == 1:
            return [nums]

        # quick case 2: sum is not divible by k.
        if sum(nums) % k != 0:
            return []

        target = sum(nums) // k
        nums.sort()

        # quick case 3, a number bigger than target
        if nums[-1] > target:
            return []

        ans = []
        # if nums have a single num == target, itself is a partition
        end = len(nums)-1
        while end > -1 and nums[end] == target:
            ans.append([nums[end]])
            end -= 1
            k -= 1

        # then partition nums[0:end+1] into k partitions
        subsets = [[] for _ in range(k)]
        # dfs/backtracking for each number starting 0 to end
        self.partition(subsets, nums, end, target)
        ans += subsets
        if all(map(lambda x: sum(x) == target, ans)):
            return ans
        else:
            return []

    def partition(self, subsets, nums, end, target):
        if end < 0:
            return
        # iterate over all subsets
        for i in range(len(subsets)):
            # skip all subsets whose sum + nums[end] > target
            if sum(subsets[i]) + nums[end] > target:
                continue
            # find a subset whose sum + nums[end] <= target
            # typical backtracking
            subsets[i].append(nums[end])
            self.partition(subsets, nums, end-1, target)
            if all(map(lambda x: sum(x) == target, subsets)):
                return
            subsets[i].pop()
        return


s = Solution()
print(s.canPartitionKSubsets([4,3,2,3,5,2,1], 4))