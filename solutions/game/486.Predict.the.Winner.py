class Solution(object):
    def PredictTheWinner(self, nums):
        """
        Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array
        followed by the player 2 and then player 1 and so on. Each time a player picks a number,
        that number will not be available for the next player. This continues until all the scores have been chosen.
        The player with the maximum score wins.

        Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

        Example 1:
        Input: [1, 5, 2]
        Output: False

        Explanation: Initially, player 1 can choose between 1 and 2.
        If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
        So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
        Hence, player 1 will never be the winner and you need to return False.

        Example 2:
        Input: [1, 5, 233, 7]
        Output: True
        Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose,
        player 1 can choose 233.
        Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

        :type nums: List[int]
        :rtype: bool

        n = len(nums)
        if n % 2 == 0:
            return True
        else:
           if odd >= even:
              return True
           else:
              return False
        """
        n = len(nums)
        if n % 2 == 0:
            return True
        odd = even = 0
        for i in range(n):
            if (i + 1) % 2 == 1:
                odd += nums[i]
            else:
                even += nums[i]
        # if player1 picks 1st or last number, a new game of even numbers
        # we need to compare new odd and new even.
        # the only condition player 2 wins if no matter what number player 1 is picked
        # the remaining new odd and new even has a bigger gap.
        if abs(odd - nums[0] - even) > nums[0] and abs(odd - nums[-1] - even) > nums[-1]:
            return False
        else:
            return True

s = Solution()
print(s.PredictTheWinner([2,4,55,6,8]))
print(s.PredictTheWinner([0,0,7,6,5,6,1]))