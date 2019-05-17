class Solution(object):
    def checkValidString(self, s):
        """
        Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

        Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        Any right parenthesis ')' must have a corresponding left parenthesis '('.
        Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
        An empty string is also valid.
        Example 1:
        Input: "()"
        Output: True
        Example 2:
        Input: "(*)"
        Output: True
        Example 3:
        Input: "(*))"
        Output: True
        Note:
        The string size will be in the range [1, 100].

        :type s: str
        :rtype: bool

        the string size is 100 hints O(N^3).

        """
        if not s:
            return True

        return self.dfs(s, 0, 0, set())

    def dfs(self, s, start, count, mem):
        if start == len(s):
            return count == 0

        if (start, count) in mem:
            return mem[(start, count)]

        if count < 0:
            mem[(start, count)] = False
            return False

        if s[start] == '(':
            r = self.dfs(s, start, count + 1)
            mem[(start, count)] = r
        elif s[start] == ')':
            r = self.dfs(s, start + 1, count - 1)
            mem[(start, count)] = r
        else:
            r1 = self.dfs(s, start, count)
            r2 = self.dfs(s, start, count + 1)
            r3 = self.dfs(s, start, count - 1)
            mem[(start, count)] = r1 or r2 or r3

        return mem[(start, count)]


class DPSolution(object):
    def checkValidString(self, s):
        """
        Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

        Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        Any right parenthesis ')' must have a corresponding left parenthesis '('.
        Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
        An empty string is also valid.
        Example 1:
        Input: "()"
        Output: True
        Example 2:
        Input: "(*)"
        Output: True
        Example 3:
        Input: "(*))"
        Output: True
        Note:
        The string size will be in the range [1, 100].

        :type s: str
        :rtype: bool

        the string size is 100 hints O(N^3).

        dp[i][j] denotes whether string from i to j is a valid parenthsis

        """

        if not s:
            return True
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # base case:
        for i in range(n):
            if s[i] == "*":
                dp[i][i] = True
            if i < n - 1 and (s[i:i+2] == '()' or s[i:i+2] == '(*' or s[i:i+2] == '*)' or s[i:i+2] == '**'):
                dp[i][i+1] = True

        # transition
        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if s[i] == "*" and dp[i+1][j]:
                    dp[i][j] = True
                elif s[i] == '(' or s[i] == '*':
                    for k in range(i+1, j+1):
                        if s[k] == ')' or s[k] == '*':
                            if (k == i + 1 or dp[i+1][k-1]) and (k == j or dp[k+1][j]):
                                dp[i][j] = True
                                break

        return dp[0][n-1]

s = DPSolution()
print(s.checkValidString("(*)"))

class GreedySolution(object):
    def checkValidString(self, s):
        """
        Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

        Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        Any right parenthesis ')' must have a corresponding left parenthesis '('.
        Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
        An empty string is also valid.
        Example 1:
        Input: "()"
        Output: True
        Example 2:
        Input: "(*)"
        Output: True
        Example 3:
        Input: "(*))"
        Output: True
        Note:
        The string size will be in the range [1, 100].

        :type s: str
        :rtype: bool

        When checking whether the string is valid, we only cared about the "balance":
        the number of extra, open left brackets as we parsed through the string.
        For example, when checking whether '(()())' is valid, we had a balance of 1, 2, 1, 2, 1, 0
        as we parse through the string: '(' has 1 left bracket, '((' has 2, '(()' has 1, and so on.
        This means that after parsing the first i symbols, (which may include asterisks,) we only need to keep track of what the balance could be.

        For example, if we have string '(***)', then as we parse each symbol,
        the set of possible values for the balance is [1] for '('; [0, 1, 2] for '(*';
        [0, 1, 2, 3] for '(**';
        [0, 1, 2, 3, 4] for '(***',
        and [0, 1, 2, 3] for '(***)'.

        Furthermore, we can prove these states always form a contiguous interval.
        Thus, we only need to know the left and right bounds of this interval.
        That is, we would keep those intermediate states described above as [lo, hi] = [1, 1], [0, 2], [0, 3], [0, 4], [0, 3].


        Algorithm

        Let lo, hi respectively be the smallest and largest possible number of open left brackets after processing the current character in the string.

        If we encounter a left bracket (c == '('), then lo++, otherwise we could write a right bracket, so lo--.
        If we encounter what can be a left bracket (c != ')'), then hi++, otherwise we must write a right bracket, so hi--.
        If hi < 0, then the current prefix can't be made valid no matter what our choices are.
        Also, we can never have less than 0 open left brackets.
        At the end, we should check that we can have exactly 0 open left brackets.


        """

        if not s:
            return True
        # the smallest and largest possible open left parethesis.
        l = h = 0
        for c in s:
            if c == '(':
                l += 1
                h += 1
            elif c == ')':
                if l > 0:
                    l -= 1
                h -= 1
            else:
                # c == "*"
                # if c == ')'
                if l > 0:
                    l -= 1
                # if c == '('
                h += 1
            # the current prefix can't be made valid no matter how * is used.
            if h < 0:
                return False

        # the samllest open left parenthsis must be 0
        return l == 0
