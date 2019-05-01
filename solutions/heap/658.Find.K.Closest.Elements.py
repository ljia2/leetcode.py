import heapq as hq
import bisect

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        Given a sorted array, two integers k and x, find the k closest elements to x in the array.
        The result should also be sorted in ascending order.
        If there is a tie, the smaller elements are always preferred.

        Example 1:
        Input: [1,2,3,4,5], k=4, x=3
        Output: [1,2,3,4]
        Example 2:
        Input: [1,2,3,4,5], k=4, x=-1
        Output: [1,2,3,4]


        Note:
        The value k is positive and will always be smaller than the length of the sorted array.
        Length of the given array is positive and will not exceed 104
        Absolute value of elements in the array and x will not exceed 104


        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        pq = []
        for i, a in enumerate(arr):
            if len(pq) < k:
                hq.heappush(pq, (-abs(a-x), -i, a))
            else:
                hq.heappushpop(pq, (-abs(a-x), -i, a))
        ans = []
        while pq:
            _, _, v = hq.heappop(pq)
            bisect.insort_left(ans, v)
        return ans

s = Solution()
print(s.findClosestElements([1,2,3,4,5], 4, 3))
