class Solution:
    def maxProfit(self, prices):
        """
        Say you have an array for which the ith element is the price of a given stock on day i.

        Design an algorithm to find the maximum profit. You may complete at most two transactions.

        Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

        Example 1:

        Input: [3,3,5,0,0,3,1,4]
        Output: 6
        Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
                     Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
        Example 2:

        Input: [1,2,3,4,5]
        Output: 4
        Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                     Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
                     engaging multiple transactions at the same time. You must sell before buying again.
        Example 3:

        Input: [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transaction is done, i.e. max profit = 0.


        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        else:
            day_num = len(prices)
            # DP: max_profit[t][i] stores the max profit when t transactions have been executed on the ith day
            # Note that the t transaction may not sold on the ith day.
            max_profit = [[0] * day_num for _ in range(3)]
            for t in range(1, 3):
                # keep track of the best opportunity to buy-in for executing the t transaction.
                # i.e. max profit combining the highest profits from previous t-1 transactions and low price)
                # for executing the t transaction on i day.
                tempMax = max_profit[t-1][0] - prices[0]
                for i in range(1, day_num, 1):
                    max_profit[t][i] = max(max_profit[t][i-1], prices[i] + tempMax)
                    tempMax = max(tempMax, max_profit[t-1][i-1] - prices[i])
            return max_profit[2][-1]

s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))