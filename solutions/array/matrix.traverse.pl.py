class Solution(object):
    def mostLeftColumn(self, matrix):
        """

        :param matrix:
        :return:
        """
        if not matrix or not matrix[0]:
            raise Exception("InValid Input")

        rnum, cnum = len(matrix), len(matrix[0])
        r, c = 0, cnum-1
        while r < rnum - 1 and c > 0:
            # keep moving left until next element is not 1.
            while c - 1 > -1 and matrix[r][c-1] == 1:
                c -= 1
            # if ecountering the first column, return
            if c > 0:
                # move to next row.
                r += 1
                # keep moving down until next element is 1.
                while r + 1 < rnum and matrix[r+1][c] == 0:
                    r += 1
        return c

s = Solution()
print(s.mostLeftColumn([[0,0,0,1,1], [0,1,1,1,1], [0, 0, 0, 0, 1]]))