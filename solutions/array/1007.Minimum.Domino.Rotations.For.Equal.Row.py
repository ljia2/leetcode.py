import collections

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.
        (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

        We may rotate the i-th domino, so that A[i] and B[i] swap values.

        Return the minimum number of rotations so that all the values in A are the same,
        or all the values in B are the same.

        If it cannot be done, return -1.

        Example 1:
        Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
        Output: 2
        Explanation:
        The first figure represents the dominoes as given by A and B: before we do any rotations.
        If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2,
        as indicated by the second figure.

        Example 2:

        Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
        Output: -1
        Explanation:
        In this case, it is not possible to rotate the dominoes to make one row of values equal.


        Note:

        1 <= A[i], B[i] <= 6
        2 <= A.length == B.length <= 20000
        :type A: List[int]
        :type B: List[int]
        :rtype: int

        general solution!!!


        """
        ansA = self.equalRowA(A, B)
        ansB = self.equalRowA(B, A)
        if ansA > -1 and ansB > -1:
            return min(ansA, ansB)
        elif ansA > -1:
            return ansA
        else:
            return ansB

    def equalRowA(self, A, B):
        num2pos = collections.defaultdict(list)
        for i in range(len(A)):
            a = A[i]
            b = B[i]
            num2pos[a].append((i, 0))
            if a != b:
                num2pos[b].append((i, 1))

        ans = -1
        for k, v in num2pos.items():
            if len(v) != len(A):
                continue
            if ans < 0:
                ans = sum(map(lambda x:x[1], v))
            else:
                ans = min(ans, sum(map(lambda x:x[1], v)))
        return ans

s = Solution()
print(s.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))
print(s.minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))
print(s.minDominoRotations([1,2,1,1,1,2,2,2],[2,1,2,2,2,2,2,2]))
print(s.minDominoRotations([1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]))