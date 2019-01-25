class Solution:
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

        1) binary search over range [1, m*n]
        2) l = 1 and r = m*n
        3) for each candidate solution m = (l + r)//2,
           3.1) we need to verify # of number in the table count(m) <= k, return the solution
           3.2) if count(m) >= k:
                    r = m
                else:
                    l = m + 1

        O(m * logK)
        """

        l = 1
        r = m*n
        while l < r:
            t = (l + r) // 2

            le = self.count(m, n, t)

            if le >= k:
                r = t
            else:
                l = t + 1
        return l

    def count(self, m, n, t):
        cnt = 0
        for i in range(1, m + 1):
            cnt += min(t // i, n)
        return cnt

s = Solution()
print(s.findKthNumber(3, 3, 5))
