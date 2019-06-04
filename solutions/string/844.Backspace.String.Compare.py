class Solution(object):
    def backspaceCompare(self, S, T):
        """
        Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

        Example 1:

        Input: S = "ab#c", T = "ad#c"
        Output: true
        Explanation: Both S and T become "ac".
        Example 2:

        Input: S = "ab##", T = "c#d#"
        Output: true
        Explanation: Both S and T become "".
        Example 3:

        Input: S = "a##c", T = "#a#c"
        Output: true
        Explanation: Both S and T become "c".
        Example 4:

        Input: S = "a#c", T = "b"
        Output: false
        Explanation: S becomes "c" while T becomes "b".
        Note:

        1 <= S.length <= 200
        1 <= T.length <= 200
        S and T only contain lowercase letters and '#' characters.
        :type S: str
        :type T: str
        :rtype: bool
        """

        sword = self.backspace(S)
        tword = self.backspace(T)

        return sword == tword

    def backspace(self, word):
        if not word:
            return ""

        stack = []
        for c in word:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


