## backtrack solution ????
class Solution2(object):
    def generateParenthesis(self, n):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

def main():
    s = Solution2()
    results = s.generateParenthesis(4)
    print(results)


if __name__ == "__main__":
    main()