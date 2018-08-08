class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]
        else:
            rs_dict = dict()
            pre_rs_list = self.generateParenthesis(n-1)
            for r in pre_rs_list:
                rs_list = ["(" + r + ")", "()" + r, r + "()"]
                for nr in rs_list:
                    if nr not in rs_dict.keys():
                        rs_dict[nr] = 1
                    else:
                        rs_dict[nr] += 1
                if n == 4:
                    print(rs_dict.keys())
            return list(rs_dict.keys())


def main():
    s = Solution()
    results = s.generateParenthesis(4)
    print(results.sorted())


if __name__ == "__main__":
    main()