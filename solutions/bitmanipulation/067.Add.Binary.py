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
        while ai > -1 and bi > -1:
            ca, cb = int(a[ai]), int(b[bi])
            cc = (ca + cb + carry) % 2
            carry = (ca + cb + carry) // 2
            ans = str(cc) + ans
            ai -= 1
            bi -= 1

        while ai > -1:
            ca = int(a[ai])
            cc = (ca + carry) % 2
            carry = (ca + carry) // 2
            ans = str(cc) + ans
            ai -= 1

        while bi > -1:
            cb = int(b[bi])
            cc = (cb + carry) % 2
            carry = (cb + carry) // 2
            ans = str(cc) + ans
            bi -= 1

        if carry == 1:
            ans = str(carry) + ans

        return ans

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

        :type a: str
        :type b: str
        :rtype: str


        """
        if a == "0":
            return b
        elif b == "0":
            return a
        ia, ib = int(a), int(b)
        while ib != 0:
            carry = ia & ib
            ia = ia ^ ib
            ib = carry << 1
        return str(ia)

s = BitSolution()
print(s.addBinary(5, 6))