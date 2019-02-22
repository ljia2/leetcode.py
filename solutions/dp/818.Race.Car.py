import math

class Solution(object): # TLE
    def racecar(self, target):
        """
        Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

        Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

        When you get an instruction "A", your car does the following: position += speed, speed *= 2.

        When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 ,
        otherwise speed = 1.  (Your position stays the same.)

        For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

        Now for some target position, say the length of the shortest sequence of instructions to get there.

        Example 1:
        Input:
        target = 3
        Output: 2
        Explanation:
        The shortest instruction sequence is "AA". Your position goes from 0->1->3.

        Example 2:
        Input:
        target = 6
        Output: 5

        Explanation:
        The shortest instruction sequence is "AAARA". Your position goes from 0->1->3->7->7->6.

        :type target: int
        :rtype: int

        Note: 1 <= target <= 10000.

        whenever the car is reversed, the speed is reset to 1 and direction (+/-) is reversed.

        dp[i][0] is the minimum steps of reaching i while facing right.(+)
        dp[i][1] is the minimum steps of reaching i while facing left (-)

        """

        if target == 0:
            return 0
        if target == 1:
            return 1

        targetMax = 10000
        dp = [[0 for _ in range(2)] for _ in range(targetMax + 1)]

        for t in range(1, len(dp)+1):
            # the least steps to reach or exceed t.
            n = int(math.ceil(math.log(t+1, 2)))
            if 1 << n == t + 1:
                dp[t][0] = n
                dp[t][1] = n + 1 # just reverse once
                if t == target:
                    break

                continue
            # initialize as hiting 2^n and return l distance
            l = (1 << n) - t - 1
            # n steps to 2^n, 1 step reverse and the subproblem reaching reaching l distance
            # for dp[t][0] the subproblem is min(dp[l][0] + 1 (reverse to face right), dp[l][1])
            # for dp[t][1] the subproblem is min(dp[l][0], dp[l][1] + 1 (reverse to face left)
            dp[t][0] = n + 1 + min(dp[l][0]+1, dp[l][1])
            dp[t][1] = n + 1 + min(dp[l][0], dp[l][1]+1)
            # find the restart position
            for k in range(1, t):
                dp[t][0] = min(dp[t][0], min(dp[t-k][0] + dp[k][0] + 2, dp[t-k][0] + dp[k][1] + 1))
                dp[t][1] = min(dp[t][1], min(dp[t-k][1] + dp[k][0] + 2, dp[t-k][1] + dp[k][1] + 1))

            if t == target:
                break
        return min(dp[target][0], dp[target][1])

s = Solution()
#print(s.racecar(3))
print(s.racecar(5))