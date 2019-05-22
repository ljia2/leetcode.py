class Solution:
    def search(self, nums, target):
        """
        Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

        (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

        You are given a target value to search. If found in the array return its index, otherwise return -1.

        You may assume no duplicate exists in the array.

        Your algorithm's runtime complexity must be in the order of O(log n).

        Example 1:

        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
        Example 2:

        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1
        :type nums: List[int]
        :type target: int
        :rtype: int

        T: O(logn): Typical usage of binary search to find a number.
        """

        if not nums:
            return -1

        return self.binarySearch(nums, target, 0, len(nums)-1)

    # binarySearch where T = O(logn) and S = O(1)
    def binarySearch(self, nums, target, l, r):
        while l < r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif nums[l] < nums[m]:
                if nums[l] < target < nums[m]:
                    r = m
                else:
                    l = m + 1
            else:
                # nums[l] > nums[m], because no duplicates.
                if nums[m] < target < nums[r]:
                    l = m + 1
                else:
                    r = m
        return -1

s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))
print(s.search([4,5,6,7,0,1,2], 3))
