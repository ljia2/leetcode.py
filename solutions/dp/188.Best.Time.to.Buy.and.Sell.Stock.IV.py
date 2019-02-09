class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k <= 0:
            return 0
        else:
            day_num = len(prices)
            if k >= len(prices) // 2:
                max_profit = 0
                for i in range(len(prices)-1):
                    if prices[i+1] > prices(i):
                        max_profit += prices[i+1] - prices[i]
                return max_profit
            else:
                # max_profit[t][d] stores the max profit when t transactions have been excuted on the ith day (may not sold on the ith day).
                max_profit = [[0] * day_num for t in range(k+1)]
                for t in range(1, k+1, 1):
                    for i in range(day_num):
                        # find out the possible max profit if execute transaction t on the day i+1
                        profit = 0
                        for m in range(0, i):
                            if prices[i] > prices[m]:
                                prev_max_profit = max_profit[t-1][m-1] if m > 0 else 0
                                if profit < prices[i] - prices[m] + prev_max_profit:
                                    profit = prices[i] - prices[m] + prev_max_profit
                        # comparing with max profit if not execute transaction t before day i + 1, take the bigger one.
                        max_profit[t][i] = max(profit, max_profit[t][i-1])

                return max_profit[k][-1]


class Solution2:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k <= 0:
            return 0
        else:
            day_num = len(prices)
            if k >= len(prices) // 2:
                max_profit = 0
                for i in range(len(prices)-1):
                    if prices[i+1] > prices[i]:
                        max_profit += prices[i+1] - prices[i]
                return max_profit
            else:
                # DP: max_profit[t][i] stores the max profit when t transactions have been executed on the ith day
                # Note that the t transaction may not sold on the ith day.
                max_profit = [[0] * day_num for t in range(k+1)]
                for t in range(1, k+1, 1):
                    # keep track of the best opportunity to buy-in for executing the t transaction.
                    # i.e. max profit combining the highest profits from previous t-1 transactions and low price) for executing the t transaction on i day.
                    tempMax = max_profit[t-1][0] - prices[0]
                    for i in range(1, day_num, 1):
                        max_profit[t][i] = max(max_profit[t][i-1], prices[i] + tempMax)
                        tempMax = max(tempMax, max_profit[t-1][i-1] - prices[i])
                return max_profit[k][-1]
s = Solution2()
print(s.maxProfit(2, [3,3,5,0,0,3,1,4]))