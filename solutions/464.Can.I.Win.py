class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        In the "100 game," two players take turns adding, to a running total, any integer from 1..10.
        The player who first causes the running total to reach or exceed 100 wins.

        What if we change the game so that players cannot re-use integers?

        For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

        Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

        You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

        Example

        Input:
        maxChoosableInteger = 10
        desiredTotal = 11

        Output:
        false

        Explanation:
        No matter which integer the first player choose, the first player will lose.
        The first player can choose an integer from 1 up to 10.
        If the first player choose 1, the second player can only choose integers from 2 up to 10.
        The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
        Same with other integers chosen by the first player, the second player will always win.

        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        ssum = (maxChoosableInteger + 1) * maxChoosableInteger // 2
        # no play can win, return False
        if ssum < desiredTotal:
            return False
        # player 1 automatically win.
        if desiredTotal <= 0:
            return True

        # bid list to indicate the previous state of player 1 and 2 have choosen.
        memory = [None] * (1 << maxChoosableInteger)
        return self.winorloss(maxChoosableInteger, desiredTotal, memory, 0)

    def winorloss(self, M, T, memory, state):
        """
        :type M: int
        :type T: int
        :param memory: the previous selection has been resolved.
        :param state:
        :return:
        """
        if T <= 0:
            return False
        # if the state has been resolved, directly return its results memory[state]
        if memory[state]:
            return memory[state]

        for i in range(M):
            # the ith number has been used.
            if state & (1 << i) > 0:
                continue
            # the next player can not win, then the current player wins
            if not self.winorloss(M, T - (i + 1), memory, state | (1 << i)):
                memory[state] = True
                return True
        # no matter what number the current players picks, he/she always loses
        memory[state] = False
        return False

s = Solution()
print(s.canIWin(6, 16))