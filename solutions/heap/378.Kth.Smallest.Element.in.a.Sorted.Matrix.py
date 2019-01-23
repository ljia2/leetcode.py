from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix, k):
        """

        Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

        Note that it is the kth smallest element in the sorted order, not the kth distinct element.

        Example:

        matrix = [
           [ 1,  5,  9],
           [10, 11, 13],
           [12, 13, 15]
        ],
        k = 8,

        return 13.
        Note:
        You may assume k is always valid, 1 ≤ k ≤ n^2.

        :type matrix: List[List[int]]
        :type k: int
        :rtype: int

        given sorted matrix, use binary search between matrix[0][0] and matrix[-1][-1] to find the kth element.

        """
        if not matrix or not matrix[0] or k <= 0:
            return None
        hp = []
        for c in range(len(matrix[0])):
            heappush(hp, (matrix[0][c], 0, c))
        ans = None
        while k > 0:
            v, r, c = heappop(hp)
            k -= 1
            if k == 0:
                ans = v
                break
            if r + 1 < len(matrix):
                heappush(hp, (matrix[r+1][c], r+1, c))
        return ans

s = Solution()
print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))