class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Typical Backtracking via DFS

        T: O(n!) because there are n! possible.
        S: O(n)

        """
        if not nums:
            return []

        used = [False] * len(nums)
        p = []
        ans = []
        self.dfs(nums, 0, len(nums), used, p, ans)
        return ans

    def dfs(self, nums, level, target_level, used, permutation, ans):
        if level == target_level:
            # note that append a copy of permutation
            ans.append(permutation.copy())
            return
        else:
            for i in range(len(nums)):
                if used[i]:
                    continue
                # assuming using nums[i] at level (i.e. position) and put nums[i] to current permutation
                used[i] = True
                permutation.append(nums[i])
                self.dfs(nums, level+1, target_level, used, permutation, ans)
                # change back permutation for backtracking 
                permutation.pop()
                used[i] = False

