import heapq as q


class Solution:
    def findKthLargest(self, nums, k):
        """
        Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
        not the kth distinct element.

        Example 1:

        Input: [3,2,1,5,6,4] and k = 2
        Output: 5
        Example 2:

        Input: [3,2,3,1,2,4,5,5,6] and k = 4
        Output: 4
        Note:
        You may assume k is always valid, 1 ≤ k ≤ array's length.

        :type nums: List[int]
        :type k: int
        :rtype: int

        T: O(nlogk)
        S: O(k)
        """
        if nums is None or len(nums) == 0:
            return None
        if k < 1:
            return None

        hp = []
        for num in nums:
            # maintain a heap of size k
            if len(hp) < k:
                q.heappush(hp, num)
            else:
                if q[0] < num:
                    q.heappushpop(hp, num)
        return hp.heappop()


##### What if find the 3rd largest without using heap
class Solution:
    def findThirdLargest(self, nums):
        if not nums or len(nums) < 3:
            raise Exception("Invalid Input!")

        fmin = smin = tmin = float("-inf")
        for num in nums:
            if num > fmin:
                tmin = smin
                smin = fmin
                fmin = num
            elif num > smin:
                tmin = smin
                smin = num
            elif num > tmin:
                tmin = num
        return tmin


### Quick Select: O(n) but worse O(n^2)
import random

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index

        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element

            # select a random pivot_index between
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest
        return select(0, len(nums) - 1, len(nums) - k)