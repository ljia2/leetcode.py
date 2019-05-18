class Solution(object):
    def minAddToMakeValid(self, S):
        """
        Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

        Formally, a parentheses string is valid if and only if:

        It is the empty string, or
        It can be written as AB (A concatenated with B), where A and B are valid strings, or
        It can be written as (A), where A is a valid string.
        Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.



        Example 1:

        Input: "())"
        Output: 1
        Example 2:

        Input: "((("
        Output: 3
        Example 3:

        Input: "()"
        Output: 0
        Example 4:

        Input: "()))(("
        Output: 4


        Note:

        S.length <= 1000
        S only consists of '(' and ')' characters.

        :type S: str
        :rtype: int

        Intuition:
        To make a string valid,
        we can add some ( on the left,
        and add some ) on the right.

        We need to find the number of each.

        Explanation:
        left records the number of ( we need to add.

        right records the current opened parentheses.

        Loop char i on the string:
        If right == 0 && i == ')',
            it means no left parentheses can match this right parentheses,
            we have to add one more left parentheses on the left of the string.

        Otherwise, we update right.

        Return left + right in the end

        """
        left = right = 0
        for i in S:
            # unmatched ")"
            if left == 0 and i == ')':
                right += 1
            else:
                # unmatched "("
                left += 1 if i == '(' else -1

        return left + right
