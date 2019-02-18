class Solution:
    def numTrees(self, n):
        """
        Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

        Example:

        Input: 3
        Output: 5
        Explanation:
        Given n = 3, there are a total of 5 unique BST's:

           1         3     3      2      1
            \       /     /      / \      \
             3     2     1      1   3      2
            /     /       \                 \
           2     1         2                 3

        :type n: int
        :rtype: int

        use dp an array of size n + 1

        dp[i] denotes the number of unique BSTs with i numbers. note that dp[0] should be initialized with 1

        dp[0] = 1, dp[1] = 1, dp[2] = 2,

        iterate with BST rooted by 1, 2, 3.
        For BST with root 1, left tree has 0 node and right tree has 2 nodes.
        For BST with root 2, left tree has 1 nodes and right tree has 1 node.
        For BST with root 3, left tree has 2 nodes and right tree has 0 node.
        dp[3] = 5 = (dp[0] * dp[2] + dp[1]*dp[1] + dp[2]dp[0] = 1 * 2 + 1 * 1 + 2 * 1

        """
        if n == 0:
            return 0
        elif n == 1:
            return 1

        # declare dp array of size n + 1
        dp = [0] * (n + 1)
        # initialize for the base cases
        dp[0] = 1
        dp[1] = 1
        # start the dynamic programming iteration.
        for i in range(2, n+1, 1):
            for r in range(1, i+1, 1):
                dp[i] += dp[r-1]*dp[i-r]
        return dp[-1]

s = Solution()
print(s.numTrees(3))



