import math

class Solution(object):
    def numDupDigitsAtMostN(self, N):
        """
        Given a positive integer N,
        return the number of positive integers less than or equal to N that have at least 1 repeated digit.

        Example 1:

        Input: 20
        Output: 1
        Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.

        Example 2:
        Input: 100
        Output: 10
        Explanation: The positive numbers (<= 100) with at least 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99 and 100.

        Example 3:
        Input: 1000
        Output: 262

        Note:
        1 <= N <= 10^9
        :type N: int
        :rtype: int

        see LC902, LC788

        Count res the Number Without Repeated Digit, Then the number with repeated digits = N - res
        """
        digits = list(map(int, str(N+1)))
        n = len(digits)

        # record the digits of prefix.
        s = set()
        res = 0
        for i, x in enumerate(digits):
            # for the first digit of x, search integer staring with y (from 1 to x -1) without repeated digits
            # for the remaining digit of x, search integer starting with y (from 0 to x - 1) without repeated digits
            for y in range(0 if i else 1, x):
                # y is not in the prefix set.
                if y not in s:
                    # i = 0, y in 1 to x -1 but no in s;
                    # C(9, n - 1) is picking 9 number for the remaining n - 1 digits

                    # i = 1, y in 0 to x - 1 but no in s;
                    # C(8, n - 2) is picking from 8 number for the remaining n - 2 digits
                    res += self.permutation(9 - i, n - i - 1)

            # if x digits is repeated
            # the prefix has repeated digits
            # all integer sharing the prefix do not qualify; stop search!
            if x in s:
                break

            s.add(x)

        count = 0
        for i in range(1, n):
            count += 9*self.permutation(9, i-1)

        return N - (count + res)


    # m * (m - 1) * ... * (m - n + 1)
    def permutation(self, m, n):
        if n == 0:
            return 1
        return (m - n + 1) * self.permutation(m, n - 1)

s = Solution()
print(s.numDupDigitsAtMostN(20))
print(s.numDupDigitsAtMostN(100))
print(s.numDupDigitsAtMostN(1000))