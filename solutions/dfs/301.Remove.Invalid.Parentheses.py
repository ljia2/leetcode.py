class DFSSolution:
    def removeInvalidParentheses(self, s):
        """

        Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

        Note: The input string may contain letters other than the parentheses ( and ).

        Example 1:

        Input: "()())()"
        Output: ["()()()", "(())()"]
        Example 2:

        Input: "(a)())()"
        Output: ["(a)()()", "(a())()"]
        Example 3:

        Input: ")("
        Output: [""]

        :type s: str
        :rtype: List[str]

        Note: return all possible results, a hint for backtracking via DFS algorithm.

        """
        if not s:
            return [""]

        results = []
        l, r = self.countUnMatchParethesises(s)
        # from left to right scan, use start to define the substring s[start:]
        self.dfs(s, 0, l, r, results)
        return results


    # try all possible removals of a parenthes and try whether it is valid for (l, r-1) first then (l-1, r)
    def dfs(self, s, start, l, r, results):
        if l == 0 and r == 0:
            if self.isValid(s):
                results.append(s)
            return

        for i in range(start, len(s)):
            # we only remove the first parenthesis if there are consecutive ones to avoid duplications.
            if i != start and s[i] == s[i-1]:
                continue
            if s[i] == '(' or s[i] == ')':
                newS = s[:i] + s[i+1:]
                # remove the unmatched right parethes first avoid )( situation.
                if r > 0:
                    # always try the (l, r-1) first with the new substring
                    self.dfs(newS, i, l, r-1, results)
                elif l > 0:
                    # then try the (l-1, r) with the new substring
                    self.dfs(newS, i, l-1, r, results)
        return

    def countUnMatchParethesises(self, s):
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        return l, r

    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    # def countUnMatchParethesises(self, s):
    #     r = 0
    #     stack = []
    #     for c in s:
    #         if c == '(':
    #             stack.append(c)
    #         elif c == ')':
    #             if stack:
    #                 stack.pop()
    #             else:
    #                 r += 1
    #     return len(stack), r

    # def isValid(self, s):
    #     stack = []
    #     for c in s:
    #         if c == '(':
    #             stack.append(c)
    #         elif c == ')':
    #             if stack:
    #                 stack.pop()
    #             else:
    #                 return False
    #     return not stack


s = DFSSolution()
print(s.removeInvalidParentheses(")d))"))
print(s.removeInvalidParentheses(")()m)(((()((()(((("))