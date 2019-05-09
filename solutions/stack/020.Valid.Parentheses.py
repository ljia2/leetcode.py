class Solution(object):
    def isValid(self, s):
        """
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Note that an empty string is also considered valid.

        Example 1:

        Input: "()"
        Output: true
        Example 2:

        Input: "()[]{}"
        Output: true
        Example 3:

        Input: "(]"
        Output: false

        :type s: str
        :rtype: bool
        """
        stack = []
        for c in [s[i] for i in range(len(s))]:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c in [")", "}", "]"]:
                if c == ')':
                    cmatch = '('
                elif c == '}':
                    cmatch = '{'
                else:
                    cmatch = '['
                if stack:
                    if stack.pop() != cmatch:
                        return False
                else:
                    return False

        return not stack