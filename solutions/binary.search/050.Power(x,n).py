class Solution:
    def myPow(self, x, n):
        """
        Implement pow(x, n), which calculates x raised to the power n (xn).

        Example 1:

        Input: 2.00000, 10
        Output: 1024.00000
        Example 2:

        Input: 2.10000, 3
        Output: 9.26100
        Example 3:

        Input: 2.00000, -2
        Output: 0.25000
        Explanation: 2-2 = 1/22 = 1/4 = 0.25
        Note:

        -100.0 < x < 100.0
        n is a 32-bit signed integer, within the range [−231, 231 − 1]

        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n == -1:
            return 1.0 / x
        elif n % 2 == 0:
            half = self.myPow(x, n//2)
            return half * half
        else:
            # int just take the integer part
            half = self.myPow(x, int(n/2))
            if n > 0:
                return x * half * half
            else:
                return (1.0 / x) * half * half

s = Solution()
print(s.myPow(34.00515, -3))


###### Follow up, what if iteratively

class IterativeSolution:
    def myPow(self, x, n):
        """
        Implement pow(x, n), which calculates x raised to the power n (xn).

        Example 1:

        Input: 2.00000, 10
        Output: 1024.00000
        Example 2:

        Input: 2.10000, 3
        Output: 9.26100
        Example 3:

        Input: 2.00000, -2
        Output: 0.25000
        Explanation: 2-2 = 1/22 = 1/4 = 0.25
        Note:

        -100.0 < x < 100.0
        n is a 32-bit signed integer, within the range [−231, 231 − 1]

        :type x: float
        :type n: int
        :rtype: float


        N = 9 = 2^3 + 2^0 = 1001 in binary. Then:

        x^9 = x^(2^3) * x^(2^0)

        We can see that every time we encounter a 1 in the binary representation of N,
        we need to multiply the answer with x^(2^i) where i is the ith bit of the exponent.
        Thus, we can keep a running total of repeatedly squaring x - (x, x^2, x^4, x^8, etc)
        and multiply it by the answer when we see a 1.
        """
        if n == 0:
            return 1.0

        pown = abs(n)
        ans = 1
        while pown > 0:
            # if encounter a 1.
            if pown & 1 == 1:
                ans *= x
            # move 1 bit right
            pown = pown >> 1
            x *= x

        return ans if n > 0 else 1.0 / ans