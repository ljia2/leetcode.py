from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

        Define a pair (u,v) which consists of one element from the first array and one element from the second array.

        Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

        Example 1:

        Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
        Output: [[1,2],[1,4],[1,6]]
        Explanation: The first 3 pairs are returned from the sequence:
                     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
        Example 2:
        Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
        Output: [1,1],[1,1]
        Explanation: The first 2 pairs are returned from the sequence:
                     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
        Example 3:

        Input: nums1 = [1,2], nums2 = [3], k = 3
        Output: [1,3],[2,3]
        Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]

        since both arrays are sorted, we can not use O(n^2).

        image a matrix[i][j] = nums1[i] + nums2[j]
        for each row /column, they are asecnding order.

        use heap with optimization

        1) initialize the heap with matrix[i][0]
        2) keep pop heap (i, j) and extend by (i, j + 1) if j < len(nums2) - 1.
        3) stop at the kth pop

        """

        if not nums1 or not nums2:
            return []

        hp = []
        for i, num in enumerate(nums1):
            heappush(hp, (num + nums2[0], i, 0))

        ans = []
        while hp and k > 0:
            _, i, j = heappop(hp)
            k -= 1
            ans.append([nums1[i], nums2[j]])
            if j < len(nums2) - 1:
                heappush(hp, (nums1[i] + nums2[j+1], i, j+1))
        return ans
