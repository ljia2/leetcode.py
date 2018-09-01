class Solution:
    def repeatedStringMatch(self, A, B):
        """
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


