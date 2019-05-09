class Solution:
    def threeSum(self, nums):
        """
        Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
        Find all unique triplets in the array which gives the sum of zero.

        Note:
        The solution set must not contain duplicate triplets.

        Example:
        Given array nums = [-1, 0, 1, 2, -1, -4],
        A solution set is:
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]

        :type nums: List[int]
        :rtype: List[List[int]]


        1) for each number c, find it complement target (0 - c).
        2) sort the numbers and use start (a) and end (b) (two pointers) to find the three numbers, s.t. a + b + c = 0

        """
        if not nums or len(nums) < 3:
            return []

        # in-place sorting by ascending order
        nums.sort()

        # output all 3-item tuples (a, b, c) summed to 0; the left as a and mid as b and right as c where a<=b<=c
        ans = set()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # two pointers of left + 1 and the last one.
            l, r = i+1, len(nums)-1
            while l < r:
                ssum = nums[i] + nums[l] + nums[r]
                if ssum == 0:
                    ans.add((nums[i], nums[l], nums[r]))
                    # after a qualified tuple, need to change b and c at the same time
                    l += 1
                    r -= 1
                elif ssum > 0:
                    # need to move right to left to shrink sum.
                    r -= 1
                elif ssum < 0:
                    # need to move mid to right to increase sum.
                    l += 1

        return list(map(list, ans))


s = Solution()
print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
print(s.threeSum([-1,0,1,2,-1,-4]))