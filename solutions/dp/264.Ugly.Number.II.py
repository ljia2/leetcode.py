from heapq import heappush, heappop

# class Solution:
#     def nthUglyNumber(self, n):
#         """'
#         Write a program to find the n-th ugly number.
#
#         Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
#         Example:
#
#         Input: n = 10
#         Output: 12
#         Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
#
#         Note:
#
#         1 is typically treated as an ugly number.
#         n does not exceed 1690.
#         :type n: int
#         :rtype: int
#         """
#         pfs = [2, 3, 5]
#         unums = [1]
#         unum_count = 0
#         while unum_count < n:
#             unum_count += 1
#             unum = heappop(unums)
#             for pf in pfs:
#                 if unum * pf not in unums:
#                     heappush(unums, unum * pf)
#         return unum

class DPSolution:
    def nthUglyNumber(self, n):
        """'
        Write a program to find the n-th ugly number.

        Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

        Example:

        Input: n = 10
        Output: 12
        Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

        Note:

        1 is typically treated as an ugly number.
        n does not exceed 1690.
        :type n: int
        :rtype: int

        use t2, t3, t5 to keep track the number primary numbers



        """
        if n <= 0:
            return None
        elif n == 1:
            return 1
        else:
            t2, t3, t5 = 0, 0, 0
            dp = [1] * n
            for i in range(1, n, 1):
                dp[i] = min(min(dp[t2]*2, dp[t3]*3), dp[t5]*5)
                if dp[i] == dp[t2] * 2:
                    t2 += 1
                if dp[i] == dp[t3] * 3:
                    t3 += 1
                if dp[i] == dp[t5] * 5:
                    t5 += 1
            return dp[n-1]


s = DPSolution()
print(s.nthUglyNumber(1))
print(s.nthUglyNumber(10))

