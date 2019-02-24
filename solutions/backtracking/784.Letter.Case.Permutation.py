class DFSSolution:
    def letterCasePermutation(self, S):
        """

        Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
        Return a list of all possible strings we could create.

        Examples:
        Input: S = "a1b2"
        Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

        Input: S = "3z4"
        Output: ["3z4", "3Z4"]

        Input: S = "12345"
        Output: ["12345"]
        Note:

        S will be a string with length between 1 and 12.
        S will consist only of letters or digits.

        :type S: str
        :rtype: List[str]

        TYPICAL SOLUTION FOR PERMUTATION!!!!

        hint: given a small S, Time complexity is O(2^S).

        a binary tree rooted with S.
        for each char in S.
        if it is a number, then proceed the next char
        else (binary):
            1) proceed to next char without changing it.
            2) proceed to next char by changing its case.
        """
        ans = []
        self.dfs(0, S, ans)
        return ans

    def dfs(self, start, S, ans):
        # exit of recursive dfs, when reaching the length of S.
        if start == len(S):
            return ans.append(S)

        # dfs without change s[start], no matter S[start] is number or alpha.
        self.dfs(start + 1, S, ans)

        # dfs with changing S[start]
        if S[start].isalpha():
            S = self.toggle(start, S)
            self.dfs(start+1, S, ans)
            S = self.toggle(start, S)

    def toggle(self, start, S):
        #return S[:start] + (S[start].lower() if S[start].isupper() else S[start].upper()) + S[start+1:]
        return S[:start] + chr(ord(S[start]) ^ (1 << 5)) + S[start+1:]

s = DFSSolution()
print(s.letterCasePermutation("1a1b"))