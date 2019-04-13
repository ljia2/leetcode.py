class Solution(object):
    def baseNeg2(self, N):
        """
        Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

        The returned string must have no leading zeroes, unless the string is "0".

        Example 1:

        Input: 2
        Output: "110"
        Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
        Example 2 :

        Input: 3
        Output: "111"
        Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
        Example 3:

        Input: 4
        Output: "100"
        Explantion: (-2) ^ 2 = 4

        Note:

        0 <= N <= 10^9
        :type N: int
        :rtype: str


        def convert2baseK(N):
             s = ""
             while n != 0:
                r = n % K
                n //= K
                s = str(r) + 1
             return s

        when N and K are negative, r could be negative and we make it positive by minus K.

        python div is rounding down.

        For example:
            -3 // 2 = -2 => -3 % 2 = -1 (-2 * 2 + 1 = -3).
            3 // -2 = -1 => 3 % -2 = 1 ( -1 * -2 + 1 = 3)
            -3 // -2 = 1 => -3 % -2 = -1 (1 * -2 + (-1) = -3)

        N1 = N0 * (-2) + (-1)
        N1 = N0 * (-2) + (-1) - (-2)
        N1 = (N0 + 1) + 1
        N1 = N0 + 1 if r is negative.

        """
        if N == 0:
            return "0"

        ans = ""
        while N != 0:
            r = N % (-2)
            N //= -2
            if r < 0:
                r += 2
                N += 1
            ans = str(r) + ans
        return ans


s = Solution()
print(s.baseNeg2(6))
print(s.baseNeg2(8))
print(s.baseNeg2(9))
print(s.baseNeg2(11))
print(s.baseNeg2(24))
print(s.baseNeg2(63628))

