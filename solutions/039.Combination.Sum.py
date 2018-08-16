class Solution(object):
    def combinationSum(self, candidates, target):
        """
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
            res1 = self.combinationSum(candidates[1:], target)
            res2 = self.combinationSum(candidates, target - candidates[0])
            for r in res2:
                r.append(candidates[0])
                r.sort()

            return res1 + res2


def main():
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))
    print(s.combinationSum([2,3,5], 8))

if __name__ == "__main__":
    main()