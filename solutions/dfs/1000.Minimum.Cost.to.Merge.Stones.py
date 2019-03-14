class Solution(object): # TLE
    def __init__(self):
        self.mem = dict()

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


        dfs over state of new stones. but Time complexity is O(n!) and will be TLE given 1 <= stones.length <= 30

        """
        if len(stones) <= 1:
            return 0

        if K <= 1:
            return -1

        if (len(stones) - 1) % (K - 1) != 0:
            return -1

        ans = [-1]
        self.dfs(stones, K, 0, ans)
        return ans[0]

    def dfs(self, stones, K, cost, ans):
        if len(stones) == 1:
            if ans[0] == -1:
                ans[0] = cost
            else:
                ans[0] = min(ans[0], cost)
            return

        for i in range(len(stones) - K + 1):
            new_stones = stones[:i] + [sum(stones[i:i+K])] + stones[i+K:]
            self.dfs(new_stones, K, cost + sum(stones[i:i+K]), ans)
        return

s = Solution()
print(s.mergeStones([9,8,3,2,9,4], 2))