class Solution:
    def generateParenthesis(self, n):
        ans = []
        self.dfs(0, 0, n, "", ans)
        return ans

    def dfs(self, l, r, n, cur_str, ans):
        if l + r == n:
            if l == r:
                ans.append(cur_str)
            return
        if l < r:
            return
        # must l > r
        self.dfs(l+1, r, n, cur_str + "(", ans)
        self.dfs(l, r+1, n, cur_str + ")", ans)



s = Solution()
results = s.generateParenthesis(4)
print(results)