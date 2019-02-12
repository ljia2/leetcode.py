# class Solution: # TLE
#     def numberOfArithmeticSlices(self, A):
#         """
#         A sequence of number is called arithmetic if it consists of at least three elements
#         and if the difference between any two consecutive elements is the same.
#
#         For example, these are arithmetic sequence:
#
#         1, 3, 5, 7, 9
#         7, 7, 7, 7
#         3, -1, -5, -9
#         The following sequence is not arithmetic.
#
#         1, 1, 2, 5, 7
#
#         A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.
#
#         A slice (P, Q) of array A is called arithmetic if the sequence:
#         A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
#
#         The function should return the number of arithmetic slices in the array A.
#
#
#         Example:
#
#         A = [1, 2, 3, 4]
#
#         return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
#
#         :type A: List[int]
#         :rtype: int
#         """
#         if not A or len(A) == 0:
#             return 0
#         else:
#             slices = [[False] * len(A) for r in range(len(A)+1)]
#             for l in range(3, len(A)+1):
#                 for i in range(len(A)-l+1):
#                     j = l + i - 1
#                     if l == 3:
#                         if A[i+1] - A[i] == A[j] - A[i+1]:
#                             slices[l][i] = True
#                     else:
#                         if slices[l-1][i] and A[i+1]-A[i] == A[i+l-1]-A[i+l-2]:
#                             slices[l][i] = True
#             return sum([sum(r) for r in slices])


class BestSolution:
    def numberOfArithmeticSlices(self, A):
        """
        A sequence of number is called arithmetic if it consists of at least three elements
        and if the difference between any two consecutive elements is the same.

        For example, these are arithmetic sequence:

        1, 3, 5, 7, 9
        7, 7, 7, 7
        3, -1, -5, -9
        The following sequence is not arithmetic.

        1, 1, 2, 5, 7

        A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

        A slice (P, Q) of array A is called arithmetic if the sequence:
        A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

        The function should return the number of arithmetic slices in the array A.


        Example:

        A = [1, 2, 3, 4]

        return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) < 3:
            return 0
        else:
            # dp[i] means the number of arithmetic slices ending with A[i]
            dp = [0] * len(A)
            if A[1] - A[0] == A[2] - A[1]:
                dp[2] = 1
            result = dp[2]
            for i in range(3, len(A)):
                if A[i] - A[i-1] == A[i-1]-A[i-2]:
                    # the nubmer of a slices ending with i is equal to
                    # the number of a-slices ending with i-1 after appending i + one additional a-slice of original length ending at i
                    dp[i] = dp[i-1] + 1
                result += dp[i]
            return result

s = BestSolution()
print(s.numberOfArithmeticSlices([3, -1, -5, -9, -13]))
