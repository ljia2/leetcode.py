class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        else:
            # use this array to store a tuple (max_profit by selling at day i, lowest_price before i)
            mplp = []
            for i in range(len(prices)):
                if i == 0:
                    mplp.append((0, max(prices)))
                else:
                    mp, lp = mplp[i-1]
                    # if day i-1's price is lower than lowest price before day i-1, calc max_profit and use prices[i-1] as the lowest price before day i
                    if prices[i-1] < lp:
                        mplp.append((prices[i] - prices[i-1], prices[i-1]))
                    else:
                        # if day i-1's price is higher than lowest price before day i-1, calc max_profit and keep lp as the lowest price before day i
                        mplp.append((prices[i] - lp, lp))
            return max(map(lambda x: x[0], mplp))