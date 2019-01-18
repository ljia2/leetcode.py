class Solution:
    def myPow(self, x, n):
        """
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
            half = self.myPow(x, n/2)
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