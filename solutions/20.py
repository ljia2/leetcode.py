class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in [s[i] for i in range(len(s))]:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')':
                if not stack:
                    if stack.pop() != '(':
                        return False
                else:
                    return False
            elif c == '}':
                if not stack:
                    if stack.pop() != '{':
                        return False
                else:
                    return False
            elif c == ']':
                if not stack:
                    if stack.pop() != '[':
                        return False
                else:
                    return False
        return stack == []