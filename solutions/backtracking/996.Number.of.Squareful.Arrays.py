import math

class Solution(object):
    def numSquarefulPerms(self, A):
        """
        Given an array A of non-negative integers,
        the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

        Return the number of permutations of A that are squareful.
        Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

        Example 1:

        Input: [1,17,8]
        Output: 2
        Explanation:
        [1,8,17] and [17,8,1] are the valid permutations.
        Example 2:

        Input: [2,2,2]
        Output: 1


        Note:

        1 <= A.length <= 12
        0 <= A[i] <= 1e9

        :type A: List[int]
        :rtype: int


        # an application of permutation
        1) the permutation has to be unique.
        2) every adjacent elements whose sum is perfect square.

        Therefore, we need to early pruning based on these rules.

        """

        if not A:
            return 0

        ans = [0]
        self.dfs(A, 0, set(), [], ans)
        return ans[0]

    def dfs(self, A, level, used, perm, ans):
        if level == len(A):
            ans[0] += 1
            return

        handled = set()
        for i, num in enumerate(A):
            # the num at position i has been used in the previous level
            if i in used:
                continue
            # the num has been considered in this level
            # avoid double count permutations of same nums at different level.
            if num in handled:
                continue

            if perm and not self.perfect_square(perm, num):
                continue

            # num is added to handled to ensure it is considered in this level
            handled.add(num)

            used.add(i)
            perm.append(num)
            self.dfs(A, level + 1, used, perm, ans)
            perm.pop()
            used.remove(i)
        return

    def perfect_square(self, perm, num):
        lnum = perm[-1]
        sr = math.sqrt(lnum + num)
        if sr == int(sr):
            return True
        else:
            return False

s = Solution()
print(s.numSquarefulPerms([1,17,8]))
print(s.numSquarefulPerms([2,2,2]))
