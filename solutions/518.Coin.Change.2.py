class Solution(object): # TLE
    def change(self, amount, coins):
        """

        You are given coins of different denominations and a total amount of money.
        Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

        Note: You can assume that

        0 <= amount <= 5000
        1 <= coin <= 5000
        the number of coins is less than 500
        the answer is guaranteed to fit into signed 32-bit integer


        Example 1:

        Input: amount = 5, coins = [1, 2, 5]
        Output: 4
        Explanation: there are four ways to make up the amount:
        5=5
        5=2+2+1
        5=2+1+1+1
        5=1+1+1+1+1


        Example 2:

        Input: amount = 3, coins = [2]
        Output: 0
        Explanation: the amount of 3 cannot be made up just with coins of 2.


        Example 3:

        Input: amount = 10, coins = [10]
        Output: 1

        :type amount: int
        :type coins: List[int]
        :rtype: int

        comb_count[i][j] denotes the nubmer of combinations summing to j with only the first i types of coins
        """

        comb_count = [[0] * (amount + 1) for i in range(len(coins) + 1)]

        # given no coins and 0 amount, there is only one combination of nothing
        comb_count[0][0] = 1

        # given no coins but a positive amount, there is no combinations
        for j in range(1, amount+1):
            comb_count[0][j] = 0
        # given a coin set but 0 amount, there is only one combination of nothing
        for i in range(1, len(coins)+1):
            comb_count[i][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(1, amount+1):
                # use coins[j-1] k times
                for k in range(0, j//coins[i-1] + 1):
                    comb_count[i][j] += comb_count[i-1][j-k*coins[i-1]]

        return comb_count[len(coins)][amount]

class BestSolution(object):
    def change(self, amount, coins):
        """

        You are given coins of different denominations and a total amount of money.
        Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

        Note: You can assume that

        0 <= amount <= 5000
        1 <= coin <= 5000
        the number of coins is less than 500
        the answer is guaranteed to fit into signed 32-bit integer


        Example 1:

        Input: amount = 5, coins = [1, 2, 5]
        Output: 4
        Explanation: there are four ways to make up the amount:
        5=5
        5=2+2+1
        5=2+1+1+1
        5=1+1+1+1+1


        Example 2:

        Input: amount = 3, coins = [2]
        Output: 0
        Explanation: the amount of 3 cannot be made up just with coins of 2.


        Example 3:

        Input: amount = 10, coins = [10]
        Output: 1

        :type amount: int
        :type coins: List[int]
        :rtype: int

        comb_count[i][j] denotes the number of combinations summing to j with only the first i types of coins
        """

        comb_count = [[0] * (amount + 1) for i in range(len(coins) + 1)]

        # given no coins and 0 amount, there is only one combination of nothing
        comb_count[0][0] = 1

        # given no coins but a positive amount, there is no combinations
        for j in range(1, amount+1):
            comb_count[0][j] = 0
        # given a coin set but 0 amount, there is only one combination of nothing
        for i in range(1, len(coins)+1):
            comb_count[i][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(1, amount+1):
                if j >= coins[i-1]:
                    # 1) only use the first i-1 types of coins for amount j and 2) use the first i types of coins but amount j - coins[i-1]
                    comb_count[i][j] = comb_count[i-1][j] + comb_count[i][j-coins[i-1]]
                else:
                    comb_count[i][j] = comb_count[i-1][j]

        return comb_count[len(coins)][amount]


s = BestSolution()
print(s.change(5, [1, 2, 5]))
print(s.change(3, [2]))
print(s.change(10, [10]))


