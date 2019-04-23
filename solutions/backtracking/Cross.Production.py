class Solution:
    def cross_product(self, S):
        """
        给一个字符串比如"a{b,c}{d,e}"，可能的输出有"abd","abe","acd","ace", 写一个function来实现。
        follow up 1：如果有"{}"嵌套的情况怎么处理，比如a{b,d,{e,f}} = ab, ad, ae, af
        follow up 2: 如果括号不是成对出现怎么处理，比如 "a{b, d, {, c}", 结果有"ab","ad","a{","ac"。
        :param S: List[List[Str]]
        :return: List[str]
        """
        if not S:
            return []

        inputs = self.flatten_parser(S)

        target = len(inputs)
        ans = []
        self.dfs(inputs, 0, target, [], ans)
        return ans

    def dfs(self, inputs, level, target, res, ans):
        if level == target:
            ans.append("".join(res))
            return

        for i in range(len(inputs[level])):
            res.append(inputs[level][i])
            self.dfs(inputs, level+1, target, res, ans)
            res.pop()
        return

    def flatten_parser(self, S):
        inputs = []
        input = []
        index = 0
        lpt = 0
        while index < len(S):
            if S[index] == ",":
                index += 1
                continue

            if self.is_left_pt(S, index):
                if lpt == 0 and input:
                    inputs.append(input)
                    input = []
                lpt += 1
            elif self.is_right_pt(S, index):
                lpt -= 1
                if lpt == 0 and input:
                    inputs.append(input)
                    input = []
            else:
                input.append(S[index])
            index += 1

        if input:
            inputs.append(input)
        return inputs

    def is_left_pt(self, S, i):
        if S[i] == '{':
            # {, or { is last is not a left parenthesis
            if i + 1 < len(S) and S[i+1] == ",":
                return False
            elif i + 1 == len(S):
                return False
            else:
                return True
        else:
            return False

    def is_right_pt(self, S, i):
        if S[i] == '}':
            # ,} is not a right parenthesis
            if i > 0 and S[i-1] == ',':
                return False
            elif i == 0:
                return False
            else:
                return True
        else:
            return False



s = Solution()
print(s.cross_product("{b,c}"))
print(s.cross_product("a{bf,c}{dg,e}"))
print(s.cross_product("a{b,c}{d,e}f"))
print(s.cross_product("a{c,g}{b,d,{e,{f,g},h},i}"))
print(s.cross_product("}{a,{,b,},{c,d}}{"))
