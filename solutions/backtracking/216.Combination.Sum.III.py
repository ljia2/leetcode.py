import copy
class Solution(object):
    def combinationSum3(self, k, n):
        """
        Find all possible combinations of k numbers that add up to a number n,
        given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

        Note:

        All numbers will be positive integers.
        The solution set must not contain duplicate combinations.
        Example 1:

        Input: k = 3, n = 7
        Output: [[1,2,4]]
        Example 2:

        Input: k = 3, n = 9
        Output: [[1,2,6], [1,3,5], [2,3,4]]
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        if n <= 0 or k <= 0:
            return 0
        ans = []
        self.dfs(1, k, n, set(), [], ans)
        return ans

    def dfs(self, start, k, target, used, comb, ans):
        if target == 0 and len(comb) == k:
            ans.append(copy.copy(comb))
            return
        if len(comb) > k or target < 0:
            return

        for num in range(start, 10):
            if num in used:
                continue

            used.add(num)
            comb.append(num)
            # note that new start is the numbers after num, i.e. num + 1.
            self.dfs(num + 1, k, target - num, used, comb, ans)
            comb.pop()
            used.remove(num)
        return

s = Solution()
print(s.combinationSum3(3, 9))