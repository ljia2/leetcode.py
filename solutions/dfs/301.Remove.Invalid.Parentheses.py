class DFSSolution:
    def removeInvalidParentheses(self, s):
        """

        Remove the minimum number of invalid parentheses in order to make the input string valid.
        Return all possible results.

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
        # find # of open left/right parenthesis
        l, r = self.countUnMatchParethesises(s)
        # from left to right scan, use start to define the substring s[start:]
        results = []
        self.dfs(s, 0, l, r, results)
        return results

    # try all possible removals of a parenthesis and try whether it is valid for (l, r-1) first then (l-1, r)
    def dfs(self, s, start, l, r, results):
        # exit of recursive dfs
        if l == 0 and r == 0:
            if self.isValid(s):
                results.append(s)
            return

        for i in range(start, len(s)):
            # IMPORTANT!!!!! we only remove the first parenthesis if there are consecutive ones to avoid duplications.
            if i + 1 < len(s) and s[i+1] == s[i]:
                continue

            # try to remove parenthesis at index i
            if s[i] == '(' or s[i] == ')':
                # remove parenthesis at index i to form the new string
                ns = s[:i] + s[i+1:]

                if r > 0:
                    # remove the unmatched right parenthesis first avoid )( situation.
                    # always try the (l, r-1) first with the new substring
                    self.dfs(ns, i, l, r-1, results)
                elif l > 0:
                    # then try the (l-1, r) with the new substring
                    self.dfs(ns, i, l-1, r, results)
        return

    def countUnMatchParethesises(self, s):
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1
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


s = DFSSolution()
print(s.removeInvalidParentheses(")d))"))
print(s.removeInvalidParentheses(")()m)(((()((()(((("))

######## What if only return one possible result.
class VarationSolution:
    def removeInvalidParentheses(self, s):
        """

        Remove the minimum number of invalid parentheses in order to make the input string valid.
        Return ONE possible results.

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
        :rtype: s

        one scan from left to right for unmatched ")" and one scan from right to left for unmatched "("
        """
        l = 0
        removed = set()
        for i, c in enumerate(s):
            if c == '(':
                l += 1
            elif c == ')':
                if l > 0:
                    l -= 0
                else:
                    # record the locations of unmatched ) in prefix
                    removed.add(i)
            else:
                continue

        r = 0
        for i in range(len(s)-1, -1, -1):
            if i in removed or (s[i] != '(' and s[i] != ')'):
                continue
            if c == ')':
                r += 1
            elif c == '(':
                if r > 0:
                    r -= 1
                else:
                    # record the location of unmatched ( in suffix
                    removed.add(i)

        res = ""
        for i, c in enumerate(s):
            if i not in removed:
                res += c
        return res


vs = VarationSolution()
print(vs.removeInvalidParentheses(")d))"))
