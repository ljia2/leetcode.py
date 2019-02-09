class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Give 1, 2, 3, 2, 4, we want to find the contineous uptrend interval, trade within one traction and keep find such uptrends interfvals.
        For example, 1, 2, 3 is the first uptrend interval and profit is 3 - 1 = 2 and the 2, 4 is the second uptrend and profit is 4-2=2
        Such solution is better than 4 - 1 = 3, because profits from two vally/peak pairs, better than one vally/peak pair.
        """
        if not prices:
            return 0
        else:
            maxProfit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    maxProfit += prices[i] - prices[i-1]
            return maxProfit