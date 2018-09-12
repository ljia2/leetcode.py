class Solution:
    def minCostClimbingStairs(self, cost):
        """
        On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

        Once you pay the cost, you can either climb one or two steps.
        You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0,
        or the step with index 1.

        Example 1:
        Input: cost = [10, 15, 20]
        Output: 15
        Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
        Example 2:
        Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        Output: 6
        Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
        Note:
        cost will have a length in the range [2, 1000].
        Every cost[i] will be an integer in the range [0, 999]

        :type cost: List[int]
        :rtype: int

        dp = [0] * (len(cost) + 1)

        dp[i] is the minimum cost to on top of cost[i]

        """

        if not cost or len(cost) < 2:
            return 0
        else:
            min_cost = [0] * (len(cost) + 1)
            min_cost[0] = cost[0]
            min_cost[1] = cost[1]
            for i in range(2, len(cost) + 1, 1):
               if i < len(cost):
                   min_cost[i] = min(min_cost[i-2] + cost[i], min_cost[i-1] + cost[i])
               else:
                   min_cost[i] = min(min_cost[i-2], min_cost[i-1])
            return min_cost[len(cost)]

s = Solution()
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))