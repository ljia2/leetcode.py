import copy

class DFSSolution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        ans = []
        n = len(nums)
        # for subset of size l
        for l in range(n+1):
            self.dfs(nums, 0, l, 0, [], ans)
        return ans

    def dfs(self, nums, level, target, start, subset, ans):
        if level == target:
            ans.append(copy.copy(subset))
            return
        # combination from start to len(nums)
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, level+1, target, i + 1, subset, ans)
            subset.pop()
        return


class IterativeSolution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        For example, {1,2,3} intially we have an emtpy set as result [ [ ] ]
        Considering 1, if not use it, still [ ], if use 1, add it to [ ], so we have [1] now
        Combine them, now we have [ [ ], [1] ] as all possible subset

        Next considering 2, if not use it, we still have [ [ ], [1] ], if use 2, just add 2 to each previous subset, we have [2], [1,2]
        Combine them, now we have [ [ ], [1], [2], [1,2] ]

        Next considering 3, if not use it, we still have [ [ ], [1], [2], [1,2] ], if use 3, just add 3 to each previous subset, we have [ [3], [1,3], [2,3], [1,2,3] ]
        Combine them, now we have [ [ ], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3] ]
        """

        if not nums:
            return []

        answers = [[]]
        n = len(nums)
        for num in nums:
            new_answers = []
            for ans in answers:
                # ans + [num] is a new list
                new_answers.append(ans + [num])
            answers += new_answers
        return answers

s = IterativeSolution()
print(s.subsets([1, 2, 3]))



