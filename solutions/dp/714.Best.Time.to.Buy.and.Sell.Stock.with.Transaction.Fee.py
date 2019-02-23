class Solution(object):
    def maxProfit(self, prices, fee):
        """
        Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i;
        and a non-negative integer fee representing a transaction fee.

        You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
        You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

        Return the maximum profit you can make.

        Example 1:

        Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
        Output: 8
        Explanation: The maximum profit can be achieved by:
        Buying at prices[0] = 1
        Selling at prices[3] = 8
        Buying at prices[4] = 4
        Selling at prices[5] = 9
        The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
        Note:

        0 < prices.length <= 50000.
        0 < prices[i] < 50000.
        0 <= fee < 50000.

        :type prices: List[int]
        :type fee: int
        :rtype: int

        hold[i]: the maximum profit if holding a share at the ith day.
        sell[i]: the maximum profit if selling a share at the ith day.
        noshare[i]: the maximum profit of having no share at the ith day.
        """
        if not prices:
            return 0
        days = len(prices)

        sell = [0 for _ in range(days)]
        hold = [0 for _ in range(days)]
        noshare = [0 for _ in range(days)]

        sell[0] = 0
        hold[0] = -prices[0]
        noshare[0] = 0

        for i in range(1, days):
            # only if holding a share at day i - 1 and sell at day i.
            sell[i] = hold[i-1] + prices[i] - fee
            # 1) continue hold a share from day i-1
            # 2) sell a share at day i - 1 and then purchase a share at day i
            # 3) no share at day i - 1 and then purchase a share at day 1
            hold[i] = max(max(hold[i-1], sell[i-1] - prices[i]), noshare[i-1] - prices[i])
            # 1) sell a share at day i - 1
            # 2) continue to have no share at day i - 1
            noshare[i] = max(sell[i-1], noshare[i-1])

        return max(sell[-1], max(noshare[-1], hold[-1]))

s = Solution()
print(s.maxProfit([1, 3, 2, 8, 4, 9], 2))