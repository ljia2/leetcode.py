class Solution:
    def fourSum(self, nums, target):
        """
        Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
        such that a + b + c + d = target?

        Find all unique quadruplets in the array which gives the sum of target.

        Note:

        The solution set must not contain duplicate quadruplets.

        Example:

        Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

        A solution set is:
        [
          [-1,  0, 0, 1],
          [-2, -1, 1, 2],
          [-2,  0, 0, 2]
        ]
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []
        for a in range(n-3):
            # skip duplicate
            if a > 0 and nums[a] == nums[a-1]:
                continue

            for b in range(a+1, n-2):
                # skip duplicate
                if b > a+1 and nums[b] == nums[b-1]:
                    continue

                # two pointers starting with b + 1 and last num.
                c = b + 1
                d = n - 1
                while c < d:

                    nsum = nums[a] + nums[b] + nums[c] + nums[d]

                    if nsum == target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])

                        c += 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1

                        d -= 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1

                    elif nsum < target:
                        c += 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                    else:
                        d -= 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
        return ans
