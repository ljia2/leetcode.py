import queue as q


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
                lnum = q.heappop()
                if lnum < num:
                    q.heappush(hp, num)
                else:
                    q.heappush(hp, lnum)
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
