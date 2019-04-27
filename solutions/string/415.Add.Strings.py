class Solution(object):
    def addStrings(self, num1, num2):
        """
        Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

        Note:

        The length of both num1 and num2 is < 5100.
        Both num1 and num2 contains only digits 0-9.
        Both num1 and num2 does not contain any leading zero.
        You must not use any built-in BigInteger library or convert the inputs to integer directly.

        :type num1: str
        :type num2: str
        :rtype: str
        """

        if not num1 and not num2:
            raise Exception("Invalid Input!")
        elif not num1:
            return num2
        elif not num2:
            return num1

        i, j = len(num1), len(num2)
        carry = 0
        ans = ""
        while i > 0 and j > 0:
            a, b = int(num1[i]), int(num2[j])
            c = (a + b + carry) % 10
            carry = (a + b + carry) // 10
            ans += str(c)
            i -= 1
            j -= 1

        while i > 0:
            a = int(num1[i])
            c = (a + carry) % 10
            carry = (a + carry) // 10
            ans += str(c)
            i -= 1

        while j > 0:
            b = int(num2[j])
            c = (b + carry) % 10
            carry = (b + carry) // 10
            ans += str(c)
            j -= 1

        if carry > 0:
            ans += str(carry)

        return ans