# class Solution: # (TLE)
#     def maxProfit(self, prices):
#         """
#         Say you have an array for which the ith element is the price of a given stock on day i.
#
#         Design an algorithm to find the maximum profit. You may complete as many transactions as you
#         (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
#
#         You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#         After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
#         Example:
#
#         Input: [1,2,3,0,2]
#         Output: 3
#         Explanation: transactions = [buy, sell, cooldown, buy, sell]
#
#         :type prices: List[int]
#         :rtype: int
#
#         max_prifits[i] denotes the max profit up to day i
#         if max_profits[i] > max_profits[i-1] then sell a stock on day i otherwise no stock is sold on day i
#
#         max_profits[i] = max{ max_profits[k-1] + prices[i-1] - prices[k-1] | k from 1 to i (exclusive) } if max_profits[k-1] == max_profits[k-2]
#         or max{ max_profits[k-2] + prices[i-1] - prices[k-1] | k from 1 to i (exclusive) } if max_prifits[k-1] > max_profits[k-2]
#
#         """
#
#         if not prices or len(prices) < 2:
#             return 0
#         else:
#             if len(prices) == 2:
#                 return prices[1] - prices[0] if prices[1] > prices[0] else 0
#             else:
#                 max_profits = [0] * (len(prices) + 1)
#                 max_profits[1] = 0
#                 max_profits[2] = max(0, prices[1] - prices[0])
#                 for i in range(3, len(prices)+1):
#                     # initialize the best buy in
#                     best_buy_in = max_profits[1] - prices[0]
#                     for k in range(2, i):
#                         if max_profits[k-1] == max_profits[k-2]:
#                                 if max_profits[k-1] - prices[k-1] > best_buy_in:
#                                     best_buy_in = max_profits[k-1] - prices[k-1]
#                         else: # max_profits[k-1] > max_profits[k-2]
#                             if max_profits[k-2] - prices[k-1] > best_buy_in:
#                                 best_buy_in = max_profits[k-2] - prices[k-1]
#
#                     max_profits[i] = max(max_profits[i-1], prices[i-1] + best_buy_in)
#                 return max_profits[len(prices)]

class BestSolution:
    def maxProfit(self, prices):
        """
        Say you have an array for which the ith element is the price of a given stock on day i.

        Design an algorithm to find the maximum profit. You may complete as many transactions as you
        (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

        You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
        After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
        Example:

        Input: [1,2,3,0,2]
        Output: 3
        Explanation: transactions = [buy, sell, cooldown, buy, sell]

        :type prices: List[int]
        :rtype: int

        hint on one day you either can buy, sell or rest

        when calculate the profit, we can assume hold stock (i.e. buy in stock, profit is negative stock price buyin
        and sell stock the profit is plus the stock price sold.

        T: O(n)
        S: O(n)
        

        """

        if not prices or len(prices) < 2:
            return 0

        # hold stores the maximum profits by holding a stock on day i
        hold = [0] * len(prices)
        # sell stores the maximum profits by selling a stock on day i
        sell = [0] * len(prices)
        # rest stores the maximum profits by either do nothing or cooldown on day i
        rest = [0] * len(prices)

        sell[0] = 0
        hold[0] = -prices[0]
        rest[0] = 0

        for i in range(1, len(prices)):
            # max profit of holding a stock on day i
            # 1) holding a stock on day i - 1 and keep holding on day i
            # 2) given having no stock on day i - 1, buy a stock on day i with a negative profit of -prices[i-1]
            hold[i] = max(rest[i-1] - prices[i], hold[i-1])
            # max profit of selling a stock on day i
            # 1) holding a stock on day i - 1 plus the profit of selling a stock at prices[i-1]
            sell[i] = hold[i-1] + prices[i]
            # max profit of resting on day i (neither buy stock nor hold stock)
            # 1) given having no stock on day i - 1, continue do nothing on day i
            # 2) just sell a stock on day i-1 and have to cool down on day i
            rest[i] = max(rest[i-1], sell[i-1])
        return max(sell[-1], rest[-1])


s = BestSolution()
print(s.maxProfit([1,2,3,0,2]))


