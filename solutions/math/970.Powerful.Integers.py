import math

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

        Return a list of all powerful integers that have value less than or equal to bound.

        You may return the answer in any order.  In your answer, each value should occur at most once.

        Example 1:

        Input: x = 2, y = 3, bound = 10
        Output: [2,3,4,5,7,9,10]
        Explanation:
        2 = 2^0 + 3^0
        3 = 2^1 + 3^0
        4 = 2^0 + 3^1
        5 = 2^1 + 3^1
        7 = 2^2 + 3^1
        9 = 2^3 + 3^0
        10 = 2^0 + 3^2
        Example 2:

        Input: x = 3, y = 5, bound = 15
        Output: [2,4,6,8,10,14]


        Note:

        1 <= x <= 100
        1 <= y <= 100
        0 <= bound <= 10^6
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if bound <= 1:
            return []

        ans = set()
        if x == 1 and y == 1:
            return [2]
        elif x == 1:
            ypu = int(math.log(bound, y)) + 1
            for yp in range(ypu):
                if y**yp + 1 <= bound:
                    ans.add(y**yp + 1)
        elif y == 1:
            xpu = int(math.log(bound, x)) + 1
            for xp in range(xpu):
                if x**xp + 1 <= bound:
                    ans.add(x**xp + 1)
        else:
            xpu = int(math.log(bound, x)) + 1
            ypu = int(math.log(bound, y)) + 1
            for i in range(xpu):
                for j in range(ypu):
                    pi = x**i + y**j
                    if pi <= bound:
                        ans.add(pi)

        return list(ans)

s = Solution()
print(s.powerfulIntegers(3, 5, 15))