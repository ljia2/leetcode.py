class DPSolutionI(object):
    def mergeStones(self, stones, K):
        """
        There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

        A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

        Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

        Example 1:

        Input: stones = [3,2,4,1], K = 2
        Output: 20
        Explanation:
        We start with [3, 2, 4, 1].
        We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
        We merge [4, 1] for a cost of 5, and we are left with [5, 5].
        We merge [5, 5] for a cost of 10, and we are left with [10].
        The total cost was 20, and this is the minimum possible.
        Example 2:

        Input: stones = [3,2,4,1], K = 3
        Output: -1
        Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
        Example 3:

        Input: stones = [3,5,1,2,6], K = 3
        Output: 25
        Explanation:
        We start with [3, 5, 1, 2, 6].
        We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
        We merge [3, 8, 6] for a cost of 17, and we are left with [17].
        The total cost was 25, and this is the minimum possible.


        Note:

        1 <= stones.length <= 30
        2 <= K <= 30
        1 <= stones[i] <= 100

        :type stones: List[int]
        :type K: int
        :rtype: int

        1 <= stones.length <= 30 hints at most O(n^4).

        dynamic programming for optimization count.

        dp[i][j][k] stores the minimum cost of merging stones[i] ~ stones[j] into k piles.

        base case:
        dp[i][i][1] = 0

        Transition:
        dp[i][j][k] = min(dp[i][m][1] + dp[m+1][j][k-1]) for i <= m < j and 2 <= k < K.

        merging K piles into 1 pile.
        dp[i][j][1] = dp[i][j][K] + sum(stones[i] .. stones[j])

        ans: dp[0][n-1][1]

        T: O(n^4)
        S: O(K*n^2)
        """
        if not stones:
            return 0

        n = len(stones)
        if n == 1:
            return 0
        if K <= 1:
            return -1
        if (n - 1) % (K - 1) != 0:
            return -1

        # sums[i] store the sum of first i stones:
        # sums[0] stores 0 (zero stone).
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i+1] = sums[i] + stones[i]

        dp = [[[1e9] * (K + 1) for _ in range(n) ] for _ in range(n)]
        for i in range(n):
            dp[i][i][1] = 0

        # iterate over the length of subarray A[i] ~ A[j]
        for l in range(2, n+1):
            # start A[i]
            for i in range(n - l + 1):
                # end A[j]
                j = i + l - 1
                # iterate k piles (not necessarily merge).
                for k in range(2, K+1):
                    # iterate over the split into 1 pile and k-1 piles.
                    for m in range(i, j):
                        dp[i][j][k] = min(dp[i][j][k], dp[i][m][1] + dp[m+1][j][k-1])
                # there is a way to merge A[i] ~ A[j] into K piles (j - i + 1 < K)
                if dp[i][j][K] < 1e9:
                    dp[i][j][1] = dp[i][j][K] + (sums[j+1] - sums[i])
        return dp[0][n-1][1]


class DPSolutionII(object):
    def mergeStones(self, stones, K):
        """
        There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

        A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

        Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

        Example 1:

        Input: stones = [3,2,4,1], K = 2
        Output: 20
        Explanation:
        We start with [3, 2, 4, 1].
        We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
        We merge [4, 1] for a cost of 5, and we are left with [5, 5].
        We merge [5, 5] for a cost of 10, and we are left with [10].
        The total cost was 20, and this is the minimum possible.
        Example 2:

        Input: stones = [3,2,4,1], K = 3
        Output: -1
        Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
        Example 3:

        Input: stones = [3,5,1,2,6], K = 3
        Output: 25
        Explanation:
        We start with [3, 5, 1, 2, 6].
        We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
        We merge [3, 8, 6] for a cost of 17, and we are left with [17].
        The total cost was 25, and this is the minimum possible.


        Note:

        1 <= stones.length <= 30
        2 <= K <= 30
        1 <= stones[i] <= 100

        :type stones: List[int]
        :type K: int
        :rtype: int

        1 <= stones.length <= 30 hints at most O(n^4).

        dynamic programming for optimization count.

        dp[i][j][k] stores the minimum cost of merging stones[i] ~ stones[j] into k piles.

        base case:
        dp[i][i][1] = 0

        Transition:
        dp[i][j][k] = min(dp[i][m][1] + dp[m+1][j][k-1]) for i <= m < j and 2 <= k < K.

        merging K piles into 1 pile.
        dp[i][j][1] = dp[i][j][K] + sum(stones[i] .. stones[j])

        ans: dp[0][n-1][1]

        T: O(n^4)
        S: O(K*n^2)
        """
        if not stones:
            return 0

        n = len(stones)
        if n == 1:
            return 0
        if K <= 1:
            return -1
        if (n - 1) % (K - 1) != 0:
            return -1

        # sums[i] store the sum of first i stones:
        # sums[0] stores 0 (zero stone).
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i+1] = sums[i] + stones[i]

        dp = [[[1e9] * (K + 1) for _ in range(n) ] for _ in range(n)]
        for i in range(n):
            dp[i][i][1] = 0

        # iterate over the length of subarray A[i] ~ A[j]
        for l in range(2, n+1):
            # start A[i]
            for i in range(n - l + 1):
                # end A[j]
                j = i + l - 1
                # iterate k piles (not necessarily merge).
                for k in range(2, K+1):
                    # iterate over the split into 1 pile and k-1 piles.
                    # only there are (# stones - 1) % (K - 1) == 0 in the left can be merged into 1 pile.
                    for m in range(i, j, K-1):
                        dp[i][j][k] = min(dp[i][j][k], dp[i][m][1] + dp[m+1][j][k-1])
                # there is a way to merge A[i] ~ A[j] into K piles (j - i + 1 < K)
                if dp[i][j][K] < 1e9:
                    dp[i][j][1] = dp[i][j][K] + (sums[j+1] - sums[i])
        return dp[0][n-1][1]


class DPSolutionIII(object):
    def mergeStones(self, stones, K):
        """
        There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

        A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

        Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

        Example 1:

        Input: stones = [3,2,4,1], K = 2
        Output: 20
        Explanation:
        We start with [3, 2, 4, 1].
        We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
        We merge [4, 1] for a cost of 5, and we are left with [5, 5].
        We merge [5, 5] for a cost of 10, and we are left with [10].
        The total cost was 20, and this is the minimum possible.
        Example 2:

        Input: stones = [3,2,4,1], K = 3
        Output: -1
        Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
        Example 3:

        Input: stones = [3,5,1,2,6], K = 3
        Output: 25
        Explanation:
        We start with [3, 5, 1, 2, 6].
        We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
        We merge [3, 8, 6] for a cost of 17, and we are left with [17].
        The total cost was 25, and this is the minimum possible.


        Note:

        1 <= stones.length <= 30
        2 <= K <= 30
        1 <= stones[i] <= 100

        :type stones: List[int]
        :type K: int
        :rtype: int

        1 <= stones.length <= 30 hints at most O(n^4).

        dynamic programming for optimization count.

        dp[i][j] stores the minimum cost of merging stones[i] ~ stones[j] into (j - i) % (K - 1) + 1 piles.

        base case:
        dp[i][i] = 0

        Transition:
        dp[i][j] = min(dp[i][m] + dp[m+1][j]) for m in range(i, j, K-1)

        if possible, merging K piles into 1 pile.
        if (j - i) % (K - 1) == 0:
            dp[i][j] += dp[i][j] + sum(stones[i] .. stones[j])

        ans: dp[0][n-1]

        T: O(n^3/K)
        S: O(n^2)
        """
        if not stones:
            return 0

        n = len(stones)
        if n == 1:
            return 0
        if K <= 1:
            return -1
        if (n - 1) % (K - 1) != 0:
            return -1

        # sums[i] store the sum of first i stones:
        # sums[0] stores 0 (zero stone).
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i+1] = sums[i] + stones[i]

        # initialize the maximum costs
        dp = [[1e9] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        # iterate over the length of subarray A[i] ~ A[j]
        for l in range(2, n+1):
            # start A[i]
            for i in range(n - l + 1):
                # end A[j]
                j = i + l - 1

                # iterate over the split into 1 pile and k-1 piles.
                # only there are (j - i) % (K - 1) == 0 in the left can be merged into 1 pile.
                # j = i + p * (K-1) <=> (j - i) % (K - 1) == 0
                for m in range(i, j, K-1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m+1][j])
                if (j - i) % (K - 1) == 0:
                    dp[i][j] += sums[j+1] - sums[i]
        return dp[0][n-1]

s = DPSolutionIII()
print(s.mergeStones([3,5,1,2,6], 3))
