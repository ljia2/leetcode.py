class Solution(object):
    def hammingDistance(self, x, y):
        """
        The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

        Given two integers x and y, calculate the Hamming distance.

        Note:
        0 ≤ x, y < 231.

        Example:

        Input: x = 1, y = 4

        Output: 2

        Explanation:
        1   (0 0 0 1)
        4   (0 1 0 0)
               ↑   ↑

        The above arrows point to positions where the corresponding bits are different.

        :type x: int
        :type y: int
        :rtype: int
        """

        if x is None or y is None:
            raise Exception("Invalid Input")
        return self.oneBit(x^y)

    # count how many 1 bit of number n.
    def oneBit(self, n):
        count = 0
        while n != 0:
            n = n&(n-1)
            count += 1
        return count

