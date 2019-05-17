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


# Note that, binary search can only find local minima.
class Solution(object):
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


s = Solution()
print(s.localMin([]))
print(s.localMin([1]))
print(s.localMin([1, 2]))
print(s.localMin([2, 2]))
print(s.localMin([1, 2, 1]))
print(s.localMin([1, 1, 1, 1]))
print(s.localMin([2, 1, 3, 2, 4]))
print(s.localMin([5, 4, 3, 2, 1]))
print(s.localMin([1, 2, 3, 4, 5]))
print(s.localMin([2, 1, 5, 4, 3, 2, 4]))