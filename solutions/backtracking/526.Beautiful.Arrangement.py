class Solution:
    def countArrangement(self, N):
        """
        Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array
        that is constructed by these N numbers successfully
        if one of the following is true for the ith position (1 <= i <= N) in this array:

        The number at the ith position is divisible by i.
        i is divisible by the number at the ith position.

        Now given N, how many beautiful arrangements can you construct?

        Example 1:

        Input: 2
        Output: 2
        Explanation:

        The first beautiful arrangement is [1, 2]:
        Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
        Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

        The second beautiful arrangement is [2, 1]:
        Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
        Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

        Note:
        N is a positive integer and will not exceed 15.

        :type N: int
        :rtype: int

        Typical usage of Permutation!

        How about use permutation of N and determine whether it is feasible.

        Trick!!!!!

        Since position 1 can hold any number, we should not use top-down.
        Instead, we should start from N to 1 (bottom-up).

        """
        if not N:
            return 0

        if N <= 2:
            return N

        used = [False] * (N + 1)
        ans = [0]
        self.dfs(N, N-1, [], used, ans)
        return ans[0]

    # backtracking/dfs to generate all permutation that satisfying the two rules.
    def dfs(self, N, index, permutation, used, ans):
        # EXIT: all positions have been filed.
        if index == -1:
            # count the number
            ans[0] += 1
            # if all possible results, we need to add  the copy of permutation to ans.
            # ans.append(permutation.copy())
            return

        for n in range(1, N+1):
            if used[n]:
                continue

            pos = index + 1
            # try put number i at pos
            if n % pos != 0 and pos % n != 0:
                continue

            # try to fill the position next to start_pos
            used[n] = True
            self.dfs(N, index - 1, permutation, used, ans)
            used[n] = False
        return


s = Solution()
print(s.countArrangement(15))
