class Solution:
    def repeatedStringMatch(self, A, B):
        """
        Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it.
        If no such solution, return -1.

        For example, with A = "abcd" and B = "cdabcdab".

        Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

        Note:
        The length of A and B will be between 1 and 10000.
        :type A: str
        :type B: str
        :rtype: int
        Note; repeatively expand A to matchA until each substring in matched A starting at last char in A covers B
        """
        res = 1
        expansionA = A
        while len(expansionA) - len(A) + 1 < len(B) and expansionA.find(B) < 0:
            expansionA += A
            res += 1
        if expansionA.find(B) > -1:
            return res
        else:
            return -1


