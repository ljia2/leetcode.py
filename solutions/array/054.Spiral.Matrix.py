class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        srow = scol = 0
        erow, ecol = len(matrix) - 1, len(matrix[0]) - 1
        ans = []
        while srow <= erow and scol <= ecol:
            # from left to right
            for c in range(scol, ecol+1):
                ans.append(matrix[srow][c])
            srow += 1

            # from top to bottom
            for r in range(srow, erow+1):
                ans.append(matrix[r][ecol])
            ecol -= 1

            if srow <= erow:
                # from right to left
                for c in range(ecol, scol-1, -1):
                    ans.append(matrix[erow][c])
            erow -= 1
            if scol <= ecol:
                # from bottom to top
                for r in range(erow, srow-1, -1):
                    ans.append(matrix[r][scol])
            scol += 1
        return ans


s = Solution()

print(s.spiralOrder([[1, 2, 3 ],
                     [4, 5, 6 ],
                     [7, 8, 9 ]]))

print(s.spiralOrder([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9,10,11,12]]))

print(s.spiralOrder([[5, 4, 2, 1]]))

print(s.spiralOrder([[5], [4], [3], [2]]))

print(s.spiralOrder([[1, 2,  3,  4],
                     [9, 10, 11, 12]]))