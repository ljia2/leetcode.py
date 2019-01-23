from heapq import heappop, heappush
import bisect

class Solution:
    def smallestDistancePair(self, nums, k):
        """
        Given an integer array, return the k-th smallest distance among all the pairs.
        The distance of a pair (A, B) is defined as the absolute difference between A and B.

        Example 1:

        Input:
        nums = [1,3,1]
        k = 1
        Output: 0
        Explanation:
        Here are all the pairs:
        (1,3) -> 2
        (1,1) -> 0
        (3,1) -> 2
        Then the 1st smallest distance pair is (1,1), and its distance is 0.
        Note:

        2 <= len(nums) <= 10000.
        0 <= nums[i] < 1000000.
        1 <= k <= len(nums) * (len(nums) - 1) / 2.

        :type nums: List[int]
        :type k: int
        :rtype: int

        1) sort nums
        2) image a matrix[i][j] = abs(nums[i] - nums[j])
        3) initialize the heap by matrix[i][i+1] for i in [0, len(nums)-2]
        4) keep pop heap (i, j) and bisect_right nj nums[j] and extend the heap by (i, j+1) if j < len(nums) - 1.
        5) stop at the kth pop
        """
        nums.sort()

        # store the adjacent diff (guarantee the minimum exists in hp.
        hp = []
        for i in range(0, len(nums)-1):
            heappush(hp, (abs(nums[i] - nums[i+1]), i, i+1))

        ans = None
        while hp and k > 0:
            d, i, j = heappop(hp)

            # find the first number > nums[j]
            nj = bisect.bisect_right(nums, nums[j])
            # there are nj - 1 - j duplications of nums[j]
            # there are totally nj - 1 - j + 1 distance same as d.
            k -= nj - j
            if k <= 0:
                ans = d
                break

            if nj < len(nums):
                heappush(hp, (abs(nums[i] - nums[nj]), i, nj))

        return ans

s = Solution()
print(s.smallestDistancePair([38,33,57,65,13,2,86,75,4,56], 26))

