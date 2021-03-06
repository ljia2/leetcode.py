class DPSolution:
    def maxCoins(self, nums):
        """
        Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
        You are asked to burst all the balloons.
        If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
        Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

        Find the maximum coins you can collect by bursting the balloons wisely.

        Note:

        You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
        0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
        Example:

        Input: [3,1,5,8]
        Output: 167
        Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
        coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

        :type nums: List[int]
        :rtype: int

        Note that n <= 500 implies O(n^3)

        dp[i][j] denotes the max sum by bursting balloons from i to j (inclusive and i <= j)
        dp[i][j] = 0 where i > j.

        transition functions:
        dp[i][j] = max{dp[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + dp[k+1][j] | i <= k <= j}

        results is dp[1][n]
        """
        if not nums:
            return 0
        else:
            # padding with 1 at the beginning and the end
            padding_nums = [1] + nums + [1]
            n = len(padding_nums)

            # dp is (n + 2) * (n + 2)
            dp = [[0] * n for _ in range(n)]

            # iterate over subsequence balloons with the length of l
            for l in range(1, n-1):
                # start the first balloon to the last balloon that can form a length of l
                for i in range(1, n-l):
                    j = i + l - 1
                    # iterate from i to j (inclusive)
                    for k in range(i, j+1):
                        dp[i][j] = max(dp[i][j], dp[i][k-1] + padding_nums[i-1]*padding_nums[k]*padding_nums[j+1] + dp[k+1][j])
            return dp[1][n-1]


s = DPSolution()
print(s.maxCoins([2,3,7,9,1,8,2]))



