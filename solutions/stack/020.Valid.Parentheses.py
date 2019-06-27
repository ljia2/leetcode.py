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
        pdict = {"(": ")", "{": "}", "[":"]"}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c in [")", "}", "]"]:
                if stack:
                    if stack[-1] != pdict[c]:
                        return False
                    stack.pop()
                else:
                    return False

        return not stack

s = Solution()
print(s.isValid("()[]{}"))

### Follow up: only have ( and ), we just record the unmatched open parethesis by a number via one pass.
