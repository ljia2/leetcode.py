class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]
        else:
            rs_list = []
            for m in range(1, n):
                left_list = self.generateParenthesis(m)
                right_list = self.generateParenthesis(n-m-1)
                for lrs in left_list:
                    for rrs in right_list:
                        rs_list.append("("+lrs+")"+rrs)
            return rs_list


## backtrack solution
class Solution2(object):
    def generateParenthesis(self, N):
        ans = []

        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
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