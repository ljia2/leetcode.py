class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        A positive integer is magical if it is divisible by either A or B.

        Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.

        Example 1:

        Input: N = 1, A = 2, B = 3
        Output: 2
        Example 2:

        Input: N = 4, A = 2, B = 3
        Output: 6
        Example 3:

        Input: N = 5, A = 2, B = 4
        Output: 10
        Example 4:

        Input: N = 3, A = 6, B = 4
        Output: 8

        :type N: int
        :type A: int
        :type B: int
        :rtype: int

        4 points to figure out:

        1. Get gcd (greatest common divisor) and lcm (least common multiple) of (A, B).
            (a, b) = (A, B) while b > 0: (a, b) = (b, a % b)
            then, gcd = a and lcm = A * B / a

        2. How many magic numbers <= x ?
            By inclusion exclusion principle, we have: x / A + x / B - x / lcm

        3. Set our binary search range
            Lower bound is min(A, B), I just set left = 2.
            Upper bound is N * min(A, B), I just set right = 10 ^ 14.

        4. binary search, find the smallest x that x / A + x / B - x / lcm = N
        """

        l = 2
        r = 10 ** 14
        mod = 10 ** 9 + 7
        lcm = A * B // self.gcd(A, B)
        # l and r are searching integer space
        # find the smallest number (lower bound) where mid // A + mid // B - mid // lcm = N, similar to bisect_left
        while l < r:
            mid = (l + r) // 2
            tmp = mid // A + mid // B - mid // lcm
            if tmp >= N:
                r = mid
            else:
                l = mid + 1
        return l % mod

    def gcd(self, A, B):
        if B == 0:
            return A

        if A < B:
            return self.gcd(B, A)

        return self.gcd(B, A % B)


s = Solution()
print(s.nthMagicalNumber(10, 6, 4))
print(s.nthMagicalNumber(1, 2, 3))
print(s.nthMagicalNumber(5, 2, 4))