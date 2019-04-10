class Solution(object):
    def minDeletionSize(self, A):
        """
        We are given an array A of N lowercase letter strings, all of the same length.
        Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

        For example, if we have an array A = ["babca","bbazb"] and deletion indices {0, 1, 4}, then the final array after deletions is ["bc","az"].

        Suppose we chose a set of deletion indices D such that after deletions, the final array has every element (row) in lexicographic order.

        For clarity, A[0] is in lexicographic order (ie. A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]),
        A[1] is in lexicographic order (ie. A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]), and so on.

        Return the minimum possible value of D.length.

        Example 1:
        Input: ["babca","bbazb"]
        Output: 3
        Explanation: After deleting columns 0, 1, and 4, the final array is A = ["bc", "az"].
        Both these rows are individually in lexicographic order (ie. A[0][0] <= A[0][1] and A[1][0] <= A[1][1]).
        Note that A[0] > A[1] - the array A isn't necessarily in lexicographic order.

        Example 2:
        Input: ["edcba"]
        Output: 4
        Explanation: If we delete less than 4 columns, the only row won't be lexicographically sorted.

        Example 3:
        Input: ["ghi","def","abc"]
        Output: 0
        Explanation: All rows are already lexicographically sorted.

        Note:
        1 <= A.length <= 100
        1 <= A[i].length <= 100

        :type A: List[str]
        :rtype: int

        return minimum hints DP,
        1 <= A.length <= 100 hints at most O(n^3)

        convert the problem to maximum subsequence in lexicographic order:
            dp[j] is the longest lexicographically ordered subsequence ending with the jth char in any word.

        for j in range(len(A)):
            for i in range(j):
                dp[j] = max[dp[j], dp[i] + 1) for all (A[k][i] < A[k][j] for k in range(len(A)).
        """

        if not A or not A[0]:
            return 0

        m, n = len(A), len(A[0])
        dp = [1] * n

        for j in range(n):
            for i in range(j):
                # all function iterative[bool] -> bool
                # return True if all elements are True.
                if all(A[k][i] <= A[k][j] for k in range(m)):
                    dp[j] = max(dp[j], dp[i]+1)
        return n - max(dp)


s = Solution()
print(s.minDeletionSize(["babca","bbazb"]))
print(s.minDeletionSize(["ghi","def","abc"]))
