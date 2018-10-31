class DPSolution:
    def canPartition(self, nums):
        """
        Given a non-empty array containing only positive integers,
        find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

        Note:
        Each of the array element will not exceed 100.
        The array size will not exceed 200.

        Example 1:

        Input: [1, 5, 11, 5]

        Output: true

        Explanation: The array can be partitioned as [1, 5, 5] and [11].
        Example 2:

        Input: [1, 2, 3, 5]

        Output: false

        Explanation: The array cannot be partitioned into equal sum subsets.
        :type nums: List[int]
        :rtype: bool


        for each element, it either in the first subset or not.

        Note:
        Each of the array element will not exceed 100.
        The array size will not exceed 200.

        The sum of all elements at most 20000.

        when the sum is small, which hints a 2D dp problem.



        dp[i][j] whether we can use a subset of the first i element whose sum if j.

        base case:
        dp[0][0] = True
        Transition:
        dp[i][j] = True if dp[i-1][j - nums[i]] or dp[i-1][j]
        Results:
        dp[n][sum / 2]

        T: O(n*sum)
        S: O(n*sum)
        """

        if not nums:
            return True

        s = sum(nums)
        if s % 2 != 0:
            return False

        dp = [[False] * (s + 1) for i in range(len(nums) + 1)]
        # base case
        dp[0][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(s + 1):
                if dp[i-1][j]:
                    dp[i][j] = True # not using the i number
                    dp[i][j + nums[i-1]] = True # using the i number
        return dp[len(nums)][s//2]


class DPSolutionII:
    def canPartition(self, nums):
        """
        Given a non-empty array containing only positive integers,
        find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

        Note:
        Each of the array element will not exceed 100.
        The array size will not exceed 200.

        Example 1:

        Input: [1, 5, 11, 5]

        Output: true

        Explanation: The array can be partitioned as [1, 5, 5] and [11].
        Example 2:

        Input: [1, 2, 3, 5]

        Output: false

        Explanation: The array cannot be partitioned into equal sum subsets.
        :type nums: List[int]
        :rtype: bool


        for each element, it either in the first subset or not.

        Note:
        Each of the array element will not exceed 100.
        The array size will not exceed 200.

        The sum of all elements at most 20000.

        when the sum is small, which hints a 2D dp problem.



        dp[i][j] whether we can use a subset of the first i element whose sum if j.

        base case:
        dp[0][0] = True
        Transition:
        dp[i][j] = True if dp[i-1][j - nums[i]] or dp[i-1][j]
        Results:
        dp[n][sum / 2]


        Can we reduce to only 1D DP problem.

        dp[i][j] = True if dp[i-1][j - nums[i]] or dp[i-1][j]

        [1, 3, 2]
            0     1     2      3    4       5   6
        0: True False False False False False False
        1: True [True] False False False False False
        2: True True False [True] [True] False False
        3: True True  [True]  True  False False [True]


        reduce to 1D dp problem when iterating j from sum to 1 backwards. (see comments below).
        
        """

        if not nums:
            return True

        s = sum(nums)
        if s % 2 != 0:
            return False

        dp = [False] * (s + 1)
        dp[0] = True

        for i in range(1, len(nums) + 1):
            for j in range(s, 0, -1):
                # if use a subset of first i-1 numbers can summing to j - nums[i-1],
                # then we can generate a subset of first i numbers summing to j by using nums[i-1]
                # (of course dp[j-nums[i-1]] naturally inherits from last iteration to be True (i.e. without using the ith number).
                if dp[j-nums[i-1]]:
                    dp[j] = True
        return dp[s//2]

s = DPSolutionII()
print(s.canPartition([1, 5, 11, 5]))