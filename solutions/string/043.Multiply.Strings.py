class Solution(object):
    def multiply(self, num1, num2):
        """
        Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
        also represented as a string.

        Example 1:

        Input: num1 = "2", num2 = "3"
        Output: "6"
        Example 2:

        Input: num1 = "123", num2 = "456"
        Output: "56088"
        Note:

        The length of both num1 and num2 is < 110.
        Both num1 and num2 contain only digits 0-9.
        Both num1 and num2 do not contain any leading zero, except the number 0 itself.
        You must not use any built-in BigInteger library or convert the inputs to integer directly.

        :type num1: str
        :type num2: str
        :rtype: str

        Remember how we do multiplication?

        Start from right to left, perform multiplication on every pair of digits, and add them together. Let's draw the process! From the following draft, we can immediately conclude:

        num1[i] * num2[j]` will be placed at indices `[i + j`, `i + j + 1]

        """

        if not num1 or not num2:
            raise Exception("Invalid Input!")

        m, n = len(num1), len(num2)

        pos = [0] * (n + m)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                a, b = int(num1[i]), int(num2[j])
                pos[i+j+1] += a*b
                pos[i+j] += pos[i+j+1] // 10
                pos[i+j+1] = pos[i+j+1] % 10

        start = 0
        while start < len(pos) and pos[start] == 0:
            start += 1

        if start == len(pos):
            return "0"
        else:
            return "".join(map(str, pos[start:]))


s = Solution()
print(s.multiply("123", "456"))
