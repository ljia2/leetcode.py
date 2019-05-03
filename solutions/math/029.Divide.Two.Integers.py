import math

class Solution(object):
    def divide(self, dividend, divisor):
        """
        Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

        Return the quotient after dividing dividend by divisor.

        The integer division should truncate toward zero.

        Example 1:

        Input: dividend = 10, divisor = 3
        Output: 3
        Example 2:

        Input: dividend = 7, divisor = -3
        Output: -2
        Note:

        Both dividend and divisor will be 32-bit signed integers.
        The divisor will never be 0.
        Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
        For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if divisor == 0:
            raise Exception("Invalid divisor!")

        # in case overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31-1

        if dividend == 0 or divisor == 1:
            return dividend

        if divisor == -1:
            return -dividend

        l = 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            r = abs(dividend)
        else:
            r = - abs(dividend)

        while abs(l - r) > 1:
            m = (l + r) // 2
            if abs(m * divisor) == abs(dividend):
                return m
            elif abs(m * divisor) > abs(dividend):
                r = m
            else:
                l = m
        # return l because always truncate towards to 0
        return l


s = Solution()
print(s.divide(1, 1))