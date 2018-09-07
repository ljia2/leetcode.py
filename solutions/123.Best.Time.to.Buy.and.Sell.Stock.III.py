class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        else:
            day_num = len(prices)
            # DP: max_profit[t][i] stores the max profit when t transactions have been executed on the ith day
            # Note that the t transaction may not sold on the ith day.
            max_profit = [[0] * day_num for t in range(3)]
            for t in range(1, 3, 1):
                # keep track of the best opportunity to buy-in for executing the t transaction.
                # i.e. max profit combining the highest profits from previous t-1 transactions and low price) for executing the t transaction on i day.
                tempMax = max_profit[t-1][0] - prices[0]
                for i in range(1, day_num, 1):
                    max_profit[t][i] = max(max_profit[t][i-1], prices[i] + tempMax)
                    tempMax = max(tempMax, max_profit[t-1][i-1] - prices[i])
            return max_profit[2][-1]

s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))