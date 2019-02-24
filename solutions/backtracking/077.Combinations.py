# class Solution(object):
#     def combine(self, n, k):
#         """
#         Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
#         Example:
#
#         Input: n = 4, k = 2
#         Output:
#         [
#           [2,4],
#           [3,4],
#           [2,3],
#           [1,2],
#           [1,3],
#           [1,4],
#         ]
#
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#
#         """
#         if n is None or n == 0:
#             return []
#         if k == 0 or k > n:
#             return []
#         if k == 1:
#             return [[i+1] for i in range(n)]
#
#         n_set = [i+1 for i in range(n)]
#         res1 = self.combine_set(n_set[1:], k-1)
#         for r in res1:
#             r.append(n_set[0])
#         res2 = self.combine_set(n_set[1:], k)
#         return res1 + res2
#
#     def combine_set(self, n_set, k):
#         if n_set is None or not n_set:
#             return []
#         if k == 0 or k > len(n_set):
#             return []
#         if k == 1:
#             return [[i] for i in n_set]
#         else:
#             res1 = self.combine_set(n_set[1:], k-1)
#             for r in res1:
#                 r.append(n_set[0])
#             res2 = self.combine_set(n_set[1:], k)
#             return res1 + res2



class DFSSolution(object):
    def combine(self, n, k):
        """
        Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

        Example:

        Input: n = 4, k = 2
        Output:
        [
          [2,4],
          [3,4],
          [2,3],
          [1,2],
          [1,3],
          [1,4],
        ]

        :type n: int
        :type k: int
        :rtype: List[List[int]]

        """
        if n is None or n == 0:
            return []
        if k == 0 or k > n:
            return []
        if k == 1:
            return [[i+1] for i in range(n)]

        ans = []
        self.dfs(1, n, k, set(), [], ans)
        return ans

    def dfs(self, start, n, k, used, combination, ans):
        if len(combination) == k:
            ans.append(combination.copy())
            return

        # !!!!! COMBINATION: always iterate starting from start !!!!
        for num in range(start, n+1):
            if num in used:
                continue

            used.add(num)
            combination.append(num)
            self.dfs(num+1, n, k, used, combination, ans)
            combination.pop()
            used.remove(num)
        return

s = DFSSolution()
print(s.combine(4, 2))