class Solution:
    def isHappy(self, n):
        """
        Write an algorithm to determine if a number is "happy".

        A happy number is a number defined by the following process:
        Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
        or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

        Example:

        Input: 19
        Output: true
        Explanation:
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        else:
            explored = [n]
            next_num = self.next_num(n)
            while next_num != 1 and next_num not in explored:
                explored.append(next_num)
                next_num = self.next_num(next_num)
            return next_num == 1

    def next_num(self, num):
        next_num = 0
        while num > 0:
            next_num += (num % 10) ** 2
            num = int(num/10)
        return next_num