class Solution:
    def nextGreaterElement(self, n):
        """

        Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n.
        If no such positive 32-bit integer exists, you need to return -1.

        Example 1:

        Input: 12
        Output: 21


        Example 2:

        Input: 21
        Output: -1

        :type n: int
        :rtype: int
        """

        if n < 10:
            return -1

        digits = [int(d) for d in str(n)]

        # from the lowest digit, find the two digits (small and big):
        # the lowest small digit and the lowest big where small precedes big.
        # Then flip small and big and sort from the big +1 to tail ascending order
        for l in range(len(digits)-2, -1, -1):
            for h in range(len(digits)-1, l, -1):
                if digits[l] < digits[h]:

                    digits[l], digits[h] = digits[h], digits[l]
                    new_digits = digits[:l+1] + sorted(digits[l+1:])
                    result = 0
                    for d in new_digits:
                        result = 10 * result + d
                    return result if result <= 2**31-1 else -1
        return -1

s = Solution()
print(s.nextGreaterElement(3120))
print(s.nextGreaterElement(230241))
print(s.nextGreaterElement(2147483647))