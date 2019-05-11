class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.



        Example:

        Input:
        [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]

        Output:  [1,2,4,7,5,3,6,8,9]

        Explanation:

        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix or not matrix[0]:
            return matrix

        m, n = len(matrix), len(matrix[0])
        ans = [0] * m * n
        r = c = 0
        for i in range(len(ans)):
            ans[i] = matrix[r][c]
            # move up
            if (r + c) % 2 == 0:
                if r == 0 and c < n - 1:
                    c += 1
                elif c == n - 1 and r < m - 1:
                    r += 1
                elif r > 0 and c < n - 1:
                    r -= 1
                    c += 1
                else:
                    # ending with move up
                    break
            # move down.
            else:
                if c == 0 and r < m - 1:
                    r += 1
                elif r == m - 1 and c < n - 1:
                    c += 1
                elif r < m - 1 and c > 0:
                    r += 1
                    c -= 1
                else:
                    # ending with move down
                    break
        return ans

s = Solution()
print(s.findDiagonalOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]))