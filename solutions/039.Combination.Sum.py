class BackTrackingSolution(object):
    def combinationSum(self, candidates, target):
        """

        Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
        find all unique combinations in candidates where the candidate numbers sums to target.

        The same repeated number may be chosen from candidates unlimited number of times.

        Note:

        All numbers (including target) will be positive integers.
        The solution set must not contain duplicate combinations.
        Example 1:

        Input: candidates = [2,3,6,7], target = 7,
        A solution set is:
        [
          [7],
          [2,2,3]
        ]
        Example 2:

        Input: candidates = [2,3,5], target = 8,
        A solution set is:
        [
          [2,2,2,2],
          [2,3,3],
          [3,5]
        ]

        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates is None or not candidates:
            return []
        if target <= 0:
            return []

        candidates.sort()
        if candidates[0] > target:
            return []
        elif candidates[0] == target:
            return [[candidates[0]]]
        else:
            # without using the first element
            res1 = self.combinationSum(candidates[1:], target)
            # use the first element one time
            res2 = self.combinationSum(candidates, target - candidates[0])
            # modify res2 to reflect the fact that the first element is used
            for r in res2:
                r.append(candidates[0])
                r.sort()

            return res1 + res2


class DFSSolution(object):
    def combinationSum(self, candidates, target):
        """

        Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
        find all unique combinations in candidates where the candidate numbers sums to target.

        The same repeated number may be chosen from candidates unlimited number of times.

        Note:

        All numbers (including target) will be positive integers.
        The solution set must not contain duplicate combinations.
        Example 1:

        Input: candidates = [2,3,6,7], target = 7,
        A solution set is:
        [
          [7],
          [2,2,3]
        ]
        Example 2:

        Input: candidates = [2,3,5], target = 8,
        A solution set is:
        [
          [2,2,2,2],
          [2,3,3],
          [3,5]
        ]

        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        combination = []
        candidates.sort()
        self.dfs(candidates, target, 0, combination, ans)
        return ans

    def dfs(self, candidates, target, s, combination, ans):
        if target == 0:
            # hint, we must append a deep copy of combination, otherwise combination will change.
            ans.append(combination.copy())
            return
        else:
            # only considering the numbers starting at s
            for i in range(s, len(candidates)):
                if candidates[i] > target:
                    break
                # considering the combination only using candidates[i:];
                # if use candidates[i], update target = target - candidates[i]
                # since duplication is allowed, we set start unchanged.
                combination.append(candidates[i])
                self.dfs(candidates, target - candidates[i], i, combination, ans)
                combination.pop()

            return

def main():
    s = DFSSolution()
    print(s.combinationSum([2,3,6,7], 7))
    #print(s.combinationSum([2,3,5], 8))

if __name__ == "__main__":
    main()