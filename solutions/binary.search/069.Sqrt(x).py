class Solution:
    def mySqrt(self, x):
        """

        implement int sqrt(int x).

        Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

        Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

        Example 1:

        Input: 4
        Output: 2
        Example 2:

        Input: 8
        Output: 2
        Explanation: The square root of 8 is 2.82842..., and since
                     the decimal part is truncated, 2 is returned.


        :type x: int
        :rtype: int

        binary search within [1, x)
        """

        if x <= 1:
            return x
        # find the minimum l that l * l > x, thus (l - 1) * (l - 1) <= x.
        l = 1
        r = x
        while l < r:
            m = (l + r) // 2
            if m * m > x:
                r = m
            else:
                l = m + 1
        return l - 1
