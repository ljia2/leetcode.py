class Solution(object):
    def isPowerOfTwo(self, n):
        """
        Given an integer, write a function to determine if it is a power of two.

        Example 1:

        Input: 1
        Output: true
        Explanation: 20 = 1
        Example 2:

        Input: 16
        Output: true
        Explanation: 24 = 16
        Example 3:

        Input: 218
        Output: false


        :type n: int
        :rtype: bool
        """

        if n == 1:
            return True
        if n == 0 or n % 2 == 1:
            return False

        return self.isPowerOfTwo(n//2)


class BitSolution(object):
    def isPowerOfTwo(self, n):
        """
        Given an integer, write a function to determine if it is a power of two.

        Example 1:

        Input: 1
        Output: true
        Explanation: 20 = 1
        Example 2:

        Input: 16
        Output: true
        Explanation: 24 = 16
        Example 3:

        Input: 218
        Output: false


        :type n: int
        :rtype: bool
        """

        if n == 0:
            return False
        elif n == 1:
            return True

        return n & (n-1) == 0