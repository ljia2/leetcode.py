# class DFSSolution:
#     def coinChange(self, coins, amount):
#         """
#         You are given coins of different denominations and a total amount of money amount.
#         Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
#         Example 1:
#
#         Input: coins = [1, 2, 5], amount = 11
#         Output: 3
#         Explanation: 11 = 5 + 5 + 1
#         Example 2:
#
#         Input: coins = [2], amount = 3
#         Output: -1
#         Note:
#         You may assume that you have an infinite number of each kind of coin.
#
#
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#
#
#
#         """
#
#         if amount < 0 or not coins:
#             return -1
#         else:
#             if amount == 0:
#                 return 0
#             else:
#                 len1 = self.coinChange(coins[1:], amount)
#                 len2 = self.coinChange(coins, amount - coins[0])
#
#                 if len1 > -1 and len2 > -1:
#                     return min(len1, len2 + 1)
#                 elif len1 > -1:
#                     return len1
#                 elif len2 > -1:
#                     return len2 + 1
#                 else:
#                     return -1

# class DFSSolutionII: TLE
#     def coinChange(self, coins, amount):
#         """
#         You are given coins of different denominations and a total amount of money amount.
#         Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
#         Example 1:
#
#         Input: coins = [1, 2, 5], amount = 11
#         Output: 3
#         Explanation: 11 = 5 + 5 + 1
#         Example 2:
#
#         Input: coins = [2], amount = 3
#         Output: -1
#         Note:
#         You may assume that you have an infinite number of each kind of coin.
#
#
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#
#
#         sort coins from high to low and greedily use coins
#
#
#         """
#
#         if amount < 0 or not coins:
#             return -1
#
#         if amount == 0:
#             return 0
#         else:
#             scoins = sorted(coins)
#             scoins.reverse()
#             ans = [amount+1]
#             self.dfs(scoins, 0, amount, 0, ans)
#             return -1 if ans[0] == amount + 1 else ans[0]
#
#     def dfs(self, coins, start, amount, count, ans):
#         if start == len(coins)-1:
#             if amount % coins[start] == 0:
#                 count += amount // coins[start]
#                 ans[0] = min(ans[0], count)
#         else:
#             coin = coins[start]
#             k = amount // coin
#             # iterate over k possible: use 0, 1, ..., k coin when amount > k
#             for i in range(k, -1, -1):
#                 # prune trees
#                 if count + i < ans[0]:
#                     self.dfs(coins, start + 1, amount - i * coin, count + i, ans)
#
#         return

class DPSolution:
    def coinChange(self, coins, amount):
        """
        You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

        Example 1:

        Input: coins = [1, 2, 5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1
        Example 2:

        Input: coins = [2], amount = 3
        Output: -1
        Note:
        You may assume that you have an infinite number of each kind of coin.


        :type coins: List[int]
        :type amount: int
        :rtype: int

        dp[i] denotes the minimum coins to represent amount i

        T: O(len(coins)*amount)
        S: O(amount)
        """

        if amount < 0 or not coins:
            return -1

        dp = [amount + 1] * (amount + 1)
        # base case: needs zero coins to represent zero.
        dp[0] = 0
        # iteration over i (amount)
        for i in range(1, amount+1):
            # iterate over coins
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        return -1 if dp[amount] > amount else dp[amount]