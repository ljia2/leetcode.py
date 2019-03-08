class Solution:
    def minEatingSpeed(self, piles, H):
        """
        Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.
        The guards have gone and will come back in H hours.

        Koko can decide her bananas-per-hour eating speed of K.
        Each hour, she chooses some pile of bananas, and eats K bananas from that pile.
        If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

        Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

        Return the minimum integer K such that she can eat all the bananas within H hours.

        Example 1:

        Input: piles = [3,6,7,11], H = 8
        Output: 4

        Example 2:

        Input: piles = [30,11,23,4,20], H = 5
        Output: 30

        Example 3:

        Input: piles = [30,11,23,4,20], H = 6
        Output: 23


        Note:

        1 <= piles.length <= 10^4
        piles.length <= H <= 10^9
        1 <= piles[i] <= 10^9

        :type piles: List[int]
        :type H: int
        :rtype: int

        Given the space of K is between 1 and 10^9, we need O(logn) -> binary search within the K space
        """
        l = 1
        r = sum(piles)
        # l and r are searching integer space.
        while l < r:
            m = (l + r) // 2
            # to find the minimum m that satisfy: self.finish_hour(piles, m) <= H
            if self.finish_hour(piles, m) <= H:
                r = m
            else:
                l = m + 1
        return l

    def finish_hour(self, piles, speed):
        hour = 0
        for p in piles:
            # ceiling of division ceil(p // speed)
            hour += int(p*1.0/speed + 0.5)
        return hour

s = Solution()
print(s.minEatingSpeed([3,6,7,11], 8))