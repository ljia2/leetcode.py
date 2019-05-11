import math

class Solution(object):
    def bulbSwitch(self, n):
        """
        There are n bulbs that are initially off. You first turn on all the bulbs.
        Then, you turn off every second bulb.
        On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on).
        For the i-th round, you toggle every i bulb.
        For the n-th round, you only toggle the last bulb.
        Find how many bulbs are on after n rounds.

        Example:

        Input: 3
        Output: 1
        Explanation:
        At first, the three bulbs are [off, off, off].
        After first round, the three bulbs are [on, on, on].
        After second round, the three bulbs are [on, off, on].
        After third round, the three bulbs are [on, off, off].

        So you should return 1, because there is only one bulb is on.

        :type n: int
        :rtype: int


        Prove:
        We can come to the conclusion that the bulb i is toggled k times. Here, k is the number of i's factors (except 1). k + 1 will be the total number of i's factors

        For example:

        Factors of 6: 1, 2, 3, 6 (3 factors except 1, so it will be toggled 3 times)
        Factors of 7: 1, 7 (1 factors except 1, so it will be toggled once)

        Now, the key problem here is to judge whether k is even or odd.

        Since all bulbs are on at the beginning, we can get:

        If k is odd, the bulb will be off in the end.(after odd times of toggling).
        If k is even, the bulb i will be on in the end (after even times of toggling).


        As we all know, a natural number can divided by 1 and itself, and all factors appear in pairs. When we know that p is i's factor, we are sure q = i/p is also i's factor.

        If i has no factor p that makes p = i/p, k+ 1 is even.
        If i has a factor p that makes p = i/p (i = p^2, i is a perfect square of p), k+1 is odd.

        """
        if n <= 0:
            return 0

        # # the first bulb is on
        # ans = 1
        # # start from 2, count how many perfect number <= n
        # for i in range(2, n+1):
        #     # If n has odd factors (except 1), i.e. totally even factors, it is off.
        #     # If n has even factors (except 1), i.e. totally odd factors, it is on
        #     # only perfect square number has odd total factors.
        #     if int(math.sqrt(i)) ** 2 == i:
        #         ans += 1
        # return ans

        ## Why not directly count how many perfect square

        return int(math.sqrt(n))


s = Solution()
print(s.bulbSwitch(4))

