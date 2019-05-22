class DPSolution:
    def maxProfit(self, prices):
        """

        Say you have an array for which the ith element is the price of a given stock on day i.

        If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
        design an algorithm to find the maximum profit.

        Note that you cannot sell a stock before you buy one.

        Example 1:

        Input: [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                     Not 7-1 = 6, as selling price needs to be larger than buying price.
        Example 2:

        Input: [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transaction is done, i.e. max profit = 0.

        :type prices: List[int]
        :rtype: int


        classic 1D DP problem.

        mp[i] is the max profit up to day i
        lp[i] is the lowest price up to day i

        Transitions:

        mp[i] = max(mp[i-1], prices[i] - lp[i-1])
        lp[i] = min(prices[i], lp[i-1])

        base cases:
        mp[0] = 0
        lp[0] = prices[0]

        Complexity:

        T: O(n)
        S: O(n) -> O(1) since i only depends on i-1
        """
        if not prices:
            return 0

        # store the maximum profits up to day i
        mp = [0] * len(prices)
        # store the lowest prices up to day i
        lp = [0] * len(prices)

        mp[0] = 0
        lp[0] = prices[0]
        for i in range(1, len(prices)):
            mp, lp = mp[i-1], lp[i-1]
            mp[i] = max(mp[i-1], prices[i] - lp[i-1])
            lp[i] = min(prices[i], lp[i-1])
        return mp[-1]



class DPSolution2:
    def maxProfit(self, prices):
        """
        Say you have an array for which the ith element is the price of a given stock on day i.

        If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
        design an algorithm to find the maximum profit.

        Note that you cannot sell a stock before you buy one.

        Example 1:

        Input: [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                     Not 7-1 = 6, as selling price needs to be larger than buying price.
        Example 2:

        Input: [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transaction is done, i.e. max profit = 0.

        :type prices: List[int]
        :rtype: int


        classic 1D DP problem.

        gain[i] = prices[i] - prices[i-1]


        prices: [7, 1, 5, 3, 6, 4]
        gains of each day: [0, -6, 4, -2, 3, -2]

        the problem can be reduced to find the subarray whose sum is max (leetcode 53)

        profit[i]: the maximum profit for the subarray ending at i

        Transition:
        # sell at day i but buy a previous day or sell at day i after buy at day i-1
        profit[i] = max{profit[i-1] + gain[i], gain[i]}

        """
        if not prices:
            return 0
        # store the maximum profits up to day i
        gains = [0]
        for i in range(1, len(prices)):
            gains.append(prices[i] - prices[i-1])

        mp = [0] * len(prices)
        for i in range(len(prices)):
            mp[i] = max(mp[i-1] + gains[i], gains[i])
        return max(mp)