# class DFSSolution: # TLE
#     def findTargetSumWays(self, nums, S):
#         """
#
#         You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
#         For each integer, you should choose one from + and - as its new symbol.
#
#         Find out how many ways to assign symbols to make sum of integers equal to target S.
#
#         Example 1:
#         Input: nums is [1, 1, 1, 1, 1], S is 3.
#         Output: 5
#         Explanation:
#
#         -1+1+1+1+1 = 3
#         +1-1+1+1+1 = 3
#         +1+1-1+1+1 = 3
#         +1+1+1-1+1 = 3
#         +1+1+1+1-1 = 3
#
#         There are 5 ways to assign symbols to make the sum of nums be target 3.
#
#         Note:
#         The length of the given array is positive and will not exceed 20.
#         The sum of elements in the given array will not exceed 1000.
#         Your output answer is guaranteed to be fitted in a 32-bit integer.
#
#         :type nums: List[int]
#         :type S: int
#         :rtype: int
#
#         use dynamic programming solution
#         # similar to coin change (use it or not use it)
#         # for each number, plus it or minus it
#
#         create a binary tree, and dfs search to find the nodes at level len(nums) whose value is S.
#         DFS over a n level of full binary tree.
#         T: O(2^n) when n = 20, O(2^n) is acceptable .
#         S: O(n)
#         """
#
#         if not nums:
#             return 0
#         ans = [0]
#         self.dfs(nums, S, 0, ans)
#         return ans[0]
#
#     def dfs(self, nums, S, level, ans):
#         if level == len(nums):
#             if S == 0:
#                 ans[0] += 1
#             return
#         else:
#             self.dfs(nums, S - nums[level], level+1, ans)
#             self.dfs(nums, S + nums[level], level+1, ans)
#             return


class DPSolution:
    def findTargetSumWays(self, nums, S):
        """

        You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
        For each integer, you should choose one from + and - as its new symbol.

        Find out how many ways to assign symbols to make sum of integers equal to target S.

        Example 1:
        Input: nums is [1, 1, 1, 1, 1], S is 3.
        Output: 5
        Explanation:

        -1+1+1+1+1 = 3
        +1-1+1+1+1 = 3
        +1+1-1+1+1 = 3
        +1+1+1-1+1 = 3
        +1+1+1+1-1 = 3

        There are 5 ways to assign symbols to make the sum of nums be target 3.

        Note:
        The length of the given array is positive and will not exceed 20.
        The sum of elements in the given array will not exceed 1000.
        Your output answer is guaranteed to be fitted in a 32-bit integer.

        :type nums: List[int]
        :type S: int
        :rtype: int

        use dynamic programming solution
        # similar to coin change (use it or not use it)
        # for each number, plus it or minus it

        # sum of nums < 1000 implies we should use sum as index of dp 2-D array
        sum[i][j] is the # of ways to sum to j using nums[0~i]

        # transitions
        sum[i][j] = sum[i-1][j - nums[i]] + sum[i-1][j + nums[i]]

        """
        numSum = sum(nums)
        if not nums or S > numSum or S < -numSum:
            return 0

        tsum = [[0] * (2 * numSum + 1) for j in range(len(nums) + 1)]
        # need to initialize base case 1, otherwise all tsum will be zero.
        # base case: there is only 1 solution where use none numbers to get zero sum.
        tsum[0][numSum] = 1

        for i in range(1, len(nums)+1):
            # all possible sum denoted by s
            for s in range(-numSum, numSum + 1):
                # the index j representing sum s
                j = s + numSum
                if j - nums[i-1] > -1 and j + nums[i-1] < 2 * numSum + 1:
                    tsum[i][j] = tsum[i-1][j-nums[i-1]] + tsum[i-1][j+nums[i-1]]
                elif j - nums[i-1] > -1:
                    tsum[i][j] = tsum[i-1][j-nums[i-1]]
                elif j + nums[i-1] < 2 * numSum + 1:
                    tsum[i][j] = tsum[i-1][j+nums[i-1]]
                else:
                    continue
        # S + numSum denoting the index of S.
        return tsum[len(nums)][S + numSum]

class DPSolution2:
    def findTargetSumWays(self, nums, S):
        """

        You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
        For each integer, you should choose one from + and - as its new symbol.

        Find out how many ways to assign symbols to make sum of integers equal to target S.

        Example 1:
        Input: nums is [1, 1, 1, 1, 1], S is 3.
        Output: 5
        Explanation:

        -1+1+1+1+1 = 3
        +1-1+1+1+1 = 3
        +1+1-1+1+1 = 3
        +1+1+1-1+1 = 3
        +1+1+1+1-1 = 3

        There are 5 ways to assign symbols to make the sum of nums be target 3.

        Note:
        The length of the given array is positive and will not exceed 20.
        The sum of elements in the given array will not exceed 1000.
        Your output answer is guaranteed to be fitted in a 32-bit integer.

        :type nums: List[int]
        :type S: int
        :rtype: int

        use dynamic programming solution
        # similar to coin change (use it or not use it)
        # for each number, plus it or minus it

        # sum of nums < 1000 implies we should use sum as index of dp 2-D array
        sum[i][j] is the # of ways to sum to j using nums[0~i]

        # transitions
        sum[i][j] = sum[i-1][j - nums[i]] + sum[i-1][j + nums[i]]

        since i only use i-1,
        we can use only 1D array.

        """
        numSum = sum(nums)
        if not nums or S > numSum or S < -numSum:
            return 0

        ways = [0] * (2 * numSum + 1)
        # need to initialize base case 1, otherwise all tsum will be zero.
        # base case: there is only 1 solution where use none numbers to get zero sum.
        ways[numSum] = 1

        tmp = [0] * (2 * numSum + 1)

        for i in range(len(nums)):
            # all possible sum denoted by s
            for s in range(-numSum, numSum + 1):
                # the index j representing sum s
                j = s + numSum
                if j - nums[i] > -1 and j + nums[i] < 2 * numSum + 1:
                    tmp[j] = ways[j-nums[i]] + ways[j+nums[i]]
                elif j - nums[i] > -1:
                    tmp[j] = ways[j-nums[i]]
                elif j + nums[i-1] < 2 * numSum + 1:
                    tmp[j] = ways[j+nums[i]]
                else:
                    continue
            tmp, ways = ways, tmp
        # S + numSum denoting the index of S.
        return ways[S + numSum]


class BestDPSolution:
    def findTargetSumWays(self, nums, S):
        """

        You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
        For each integer, you should choose one from + and - as its new symbol.

        Find out how many ways to assign symbols to make sum of integers equal to target S.

        Example 1:
        Input: nums is [1, 1, 1, 1, 1], S is 3.
        Output: 5
        Explanation:

        -1+1+1+1+1 = 3
        +1-1+1+1+1 = 3
        +1+1-1+1+1 = 3
        +1+1+1-1+1 = 3
        +1+1+1+1-1 = 3

        There are 5 ways to assign symbols to make the sum of nums be target 3.

        Note:
        The length of the given array is positive and will not exceed 20.
        The sum of elements in the given array will not exceed 1000.
        Your output answer is guaranteed to be fitted in a 32-bit integer.

        :type nums: List[int]
        :type S: int
        :rtype: int

        subset sum
        P = set of numbers have + sign
        N = set of numbers have - sign

        P U N = nums and P inter N = empty set

        Sum(P) - Sum(N) = S

        2*SUM(P) = S + sum(nums)

        Sum(P) = (S + sum(nums) / 2  <- 0-1 knapsack problem

        find a subset P of nums to ensure the equation above holds.

        Simper Questions:

        V[i] denotes the set of the possible sums by using any subset of the first i elements

        V[0] = {0}
        V[i] = V[i-1] U {V[i-1] + nums[i]}
        answer: check target in V[len(nums)]


        dp[i][j] = # of ways of using any set of the first i element to sum up j if j in Vi (all possible values in Vi is from 0 to S).
        dp[0][0] = True

        """
        S = abs(S)

        numSum = sum(nums)
        if not nums or S > numSum or (S + numSum) % 2 != 0:
            return 0

        # for each iteration of i, dp denotes dp[i-1]
        dp = [0] * (S + 1)
        # base case: use none of numbers to achieve a zero.
        dp[0] = 1
        for num in nums:
            tmp = dp.copy() # use as dp[i]
            for j in range(0, S + 1 - num):
                if j + num < S + 1:
                    # hint tmp[j] = dp[j] already when considering only use the first i - 1 nubmers
                    # Then update tmp if using the i number
                    tmp[j + num] += dp[j]
            dp = tmp

        return dp[S]

s = BestDPSolution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))