class Solution(object):
    def findPeakElement(self, nums):
        """
        A peak element is an element that is greater than its neighbors.

        Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

        The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

        You may imagine that nums[-1] = nums[n] = -∞.

        Example 1:

        Input: nums = [1,2,3,1]
        Output: 2
        Explanation: 3 is a peak element and your function should return the index number 2.
        Example 2:

        Input: nums = [1,2,1,3,5,6,4]
        Output: 1 or 5
        Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
        Note:

        Your solution should be in logarithmic complexity.

        :type nums: List[int]
        :rtype: int

        binary search for local max/mins

        at least we need to determine whether it is an array of all the same elements.

        """

        if not nums:
            raise Exception("Invalid Input")

        if len(nums) == 1:
            return 1

        n = len(nums)
        l, r = 0, n-1
        while l < r:
            m = (l + r) // 2
            if (m == 0 or nums[m-1] < nums[m]) and (m == n-1 or nums[m] > nums[m+1]):
                return m
            elif m > 0 and nums[m-1] > nums[m]:
                r = m
            else:
                l = m + 1

        # what if there are not peak, i.e. all numbers are the same.
        if (l == 0 or nums[l-1] < nums[l]) and (l == n - 1 or nums[l] < nums[l+1]):
            return l
        else:
            return None


### Local Minimum:
# def localMinUtil(arr, low, high, n):
#
#     # Find index of middle element
#     mid = low + (high - low) // 2
#
#     # Compare middle element with its
#     # neighbours (if neighbours exist)
#     if(mid == 0 or arr[mid - 1] > arr[mid]) and (mid == n - 1 or arr[mid] < arr[mid + 1]):
#         return mid
#
#     # If middle element is not minima and its left
#     # neighbour is smaller than it, then left half
#     # must have a local minima.
#     elif mid > 0 and arr[mid - 1] < arr[mid] :
#         return localMinUtil(arr, low, mid - 1, n)
#
#     # If middle element is not minima and its right
#     # neighbour is smaller than it, then right half
#     # must have a local minima.
#     return localMinUtil(arr, mid + 1, high, n)

# Note that, binary search can only find local minimum.
class VariationSolution(object):
    def localMin(self, nums):
        if not nums:
            return None
        elif len(nums) == 1:
            return nums[0]

        n = len(nums)
        l = 0
        r = n-1
        while l < r:
            # important !!!
            # int division floor -> m >=l, we need always l = m + 1
            m = (l + r) // 2

            # condition for local minimum
            if (m == 0 or nums[m-1] > nums[m]) and (m == n-1 or nums[m] < nums[m+1]):
                return nums[m]

            if m > 0 and nums[m-1] < nums[m]:
                r = m
            else:
                l = m + 1

        # existing while by l = r, we need to further verify whether nums[l] satisfying condition or not.
        if (l == 0 or nums[l-1] > nums[l]) and (l == n-1 or nums[l] < nums[l+1]):
            return nums[l]
        else:
            return None
