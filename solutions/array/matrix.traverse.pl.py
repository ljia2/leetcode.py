class Solution(object):
    def mostLeftColumn(self, matrix):
        """
        :param matrix:
        :return:
        """
        if not matrix or not matrix[0]:
            raise Exception("InValid Input")

        rnum, cnum = len(matrix), len(matrix[0])
        # find the first row with 1 at the last column
        r, c = 0, cnum-1
        while r < rnum and matrix[r][c] == 0:
            r += 1

        # matrix[r][c] = 1
        # if r == rnum, skip the following while and return -1
        while r < rnum and c > -1:
            # keep moving left until next element is not 1.
            while c - 1 > -1 and matrix[r][c-1] == 1:
                c -= 1

            if c == 0:
                return c
            else:
                # keep moving down until next element is 1.
                while r + 1 < rnum and matrix[r+1][c] == 0:
                    r += 1

                if r == rnum - 1:
                    return c
                else:
                    r += 1
        return -1

s = Solution()
print(s.mostLeftColumn([[0,0,0,1,1], [0,1,1,1,1], [0, 0, 0, 0, 1]]))