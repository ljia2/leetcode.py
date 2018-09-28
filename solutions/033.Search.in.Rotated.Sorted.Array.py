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

        T: O(logn): Recursive
        """

        if not nums:
            return -1
        else:
            return self.binarySearch(nums, target, 0, len(nums))

    def RecursiveBinarySearch(self, nums, target, start, end): # start: inclusive index and end: exclusive index
        if start == end - 1:
            if target == nums[start]:
                return start
            else:
                return -1
        else:
            mid = (start + end) // 2 # Note the mid index for binary search
            if nums[start] <= nums[mid-1]:
                if nums[start] <= target <= nums[mid-1]:
                    return self.binarySearch(nums, target, start, mid)
                else:
                    return self.binarySearch(nums, target, mid, end)
            else:
                if nums[mid] <= target <= nums[end-1]:
                    return self.binarySearch(nums, target, mid, end)
                else:
                    return self.binarySearch(nums, target, start, mid)
    # binarySearch where T = O(logn) and S = O(1)
    def binarySearch(self, nums, target, start, end): # start: inclusive index and end: exclusive index
        while start < end:
            mid = (end + start) // 2
            if target == nums[mid]:
                return mid
            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end-1]:
                    start = mid + 1
                else:
                    end = mid
        return -1

s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))
print(s.search([4,5,6,7,0,1,2], 3))
