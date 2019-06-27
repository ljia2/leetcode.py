class Solution(object):
    def addBinary(self, a, b):
        """
        Given two binary strings, return their sum (also a binary string).

        The input strings are both non-empty and contains only characters 1 or 0.

        Example 1:

        Input: a = "11", b = "1"
        Output: "100"
        Example 2:

        Input: a = "1010", b = "1011"
        Output: "10101"

        :type a: str
        :type b: str
        :rtype: str
        """

        if not a and not b:
            return None
        elif not a:
            return b
        elif not b:
            return a

        al, bl = len(a), len(b)
        ai = al - 1
        bi = bl - 1
        carry = 0
        ans = ""
        while ai > -1 or bi > -1:
            ca = int(a[ai]) if ai > -1 else 0
            cb = int(b[bi]) if bi > -1 else 0
            cc = (ca + cb + carry) % 2
            carry = (ca + cb + carry) // 2
            ans = str(cc) + ans
            ai -= 1
            bi -= 1

        return str(carry) + ans if carry else ans

### Follow up: optimizat by bid operation
class BitSolution(object):
    def addBinary(self, a, b):
        """
        Given two binary strings, return their sum (also a binary string).

        The input strings are both non-empty and contains only characters 1 or 0.

        Example 1:

        Input: a = "11", b = "1"
        Output: "100"
        Example 2:

        Input: a = "1010", b = "1011"
        Output: "10101"

        :type a: int
        :type b: int
        :rtype: int

        we can directly operates bid ops on binary strings.

        """
        if a == 0:
            return b
        elif b == 0:
            return a
        # simulate a + b bit operations
        # first take xor -> a
        # second carry is take and ans << 1 -> b
        # repeat first and second until b == 0
        while b != 0:
            carry = a & b
            a, b = a ^ b, carry << 1
        return a

s = BitSolution()
print(s.addBinary(5, 6))