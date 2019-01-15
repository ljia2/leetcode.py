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
        """
        if nums is None or not nums or len(nums) < 3:
            return []

        # in-place sorting by ascending order
        nums.sort()
        # output all 3-item tuples (a, b, c) summed to 0; the left as a and mid as b and right as c where a<=b<=c
        ans = []
        for left in range(len(nums)-2):
            # skip the duplicated entries and start the last of the duplications.
            if left > 0 and nums[left] == nums[left-1]:
                continue

            # two pointers of left + 1 and the last one.
            mid, right = left+1, len(nums)-1
            while mid < right:
                sum = nums[left] + nums[mid] + nums[right]
                if sum == 0:
                    ans.append([nums[left], nums[mid], nums[right]])

                    # after a qualified tuple, need to change b and c at the same time
                    mid += 1
                    while mid < right and nums[mid] == nums[mid-1]:
                        mid += 1
                    right -= 1
                    while right > mid and nums[right] == nums[right+1]:
                        right -= 1

                elif sum > 0:
                    right -= 1
                    while right > mid and nums[right] == nums[right+1]:
                        right -= 1

                elif sum < 0:
                    mid += 1
                    while mid < right and nums[mid] == nums[mid-1]:
                        mid += 1
        return ans


s = Solution()
print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
print(s.threeSum([-1,0,1,2,-1,-4]))