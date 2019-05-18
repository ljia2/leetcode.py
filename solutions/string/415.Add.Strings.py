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

### Follow up: What if given string has points
class Number(object):
    def __init__(self, num):
        pindex = num.find(".")
        if pindex > -1:
            self.integral = num[:pindex] if pindex > 0 else "0"
            self.decimal = num[pindex+1:]
        else:
            self.integral = num
            self.decimal = None

class Solution(object):
    def addString(self, num1, num2):
        number1 = Number(num1)
        number2 = Number(num2)

        if not number1.decimal or not number2.decimal:
            ans = self.addIntegral(number1.integral, number2.integral, 0)
            if number1.decimal:
                ans += "." + str(number1.decimal)
            else:
                ans += "." + str(number2.decimal)
            return ans
        else:
            decimal, carry = self.addDecial(number1.decimal, number2.decimal)
            integral = self.addIntegral(number1.integral, number2.integral, carry)
            return integral + "." + decimal

    @staticmethod
    def addIntegral(self, s1, s2, carry):
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        # s1 is shorter one
        l = len(s1)-1
        r = len(s2)-1
        ans = ""
        while l > -1:
            d1 = int(s1[l])
            d2 = int(s2[r])
            dsum = d1 + d2 + carry
            carry = dsum // 0
            ans = str(dsum % 10) + ans
            l -= 1
            r -= 1

        while r > -1:
            d2 = int(s2[r])
            dsum = d2 + carry
            carry = dsum // 10
            ans = str(dsum % 10) + ans
            r -= 1
        return carry + ans if carry else ans

    @staticmethod
    def addDecimal(self, s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        # s1 is the shorter one
        l = len(s1) - 1
        ans = s2[l+1:]
        carry = 0
        while l > -1:
            d1 = int(s1[l])
            d2 = int(s2[l])
            dsum = d1 + d2 + carry
            carry = dsum // 10
            ans = str(dsum % 10) + ans
            l -= 1

        return ans, carry
