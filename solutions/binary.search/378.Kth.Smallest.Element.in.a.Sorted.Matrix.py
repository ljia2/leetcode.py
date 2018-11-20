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
        n = len(matrix)
        l = matrix[0][0]
        r = matrix[n-1][n-1]

        while l < r:
            m = (l + r) // 2

            total = 0
            for row in matrix:
                if row[-1] < m:
                    total += n
                else:
                    for c in row:
                        if c > m:
                            break
                        total += 1
            # find smallest m that is the kth smallest element.
            if total >= k:
                r = m
            else:
                l = m + 1

        # when l == r exits
        return l

s = Solution()
print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))