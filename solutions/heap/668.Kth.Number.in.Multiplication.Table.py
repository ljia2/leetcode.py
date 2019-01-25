from heapq import heappop, heappush

class Solution: # TLE
    def findKthNumber(self, m, n, k):
        """
        Nearly every one have used the Multiplication Table.
        But could you find out the k-th smallest number quickly from the multiplication table?

        Given the height m and the length n of a m * n Multiplication Table, and a positive integer k,
        you need to return the k-th smallest number in this table.

        Example 1:

        Input: m = 3, n = 3, k = 5
        Output:
        Explanation:
        The Multiplication Table:
        1	2	3
        2	4	6
        3	6	9

        The 5-th smallest number is 3 (1, 2, 2, 3, 3).
        Example 2:

        Input: m = 2, n = 3, k = 6
        Output:
        Explanation:
        The Multiplication Table:
        1	2	3
        2	4	6

        The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
        Note:

        The m and n will be in the range [1, 30000].
        The k will be in the range [1, m * n]

        :type m: int
        :type n: int
        :type k: int
        :rtype: int


        1) initialize the heap with the first col in the table.
        2) pop an element (i, j) and then extend (i, j + 1)

        O(m*logm + k*logm*n)

        """
        hp = []
        for i in range(1, m+1):
            heappush(hp, (i, i, 1))

        ans = None
        while hp and k > 0:
            num, i, j = heappop(hp)
            k -= 1
            if k == 0:
                ans = num
                break
            if j + 1 <= n:
                heappush(hp, (i*(j+1), i, j+1))
        return ans
