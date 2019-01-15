class Solution:
    def longestMountain(self, A):
        """
        Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

        B.length >= 3
        There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
        (Note that B could be any subarray of A, including the entire array A.)

        Given an array A of integers, return the length of the longest mountain.

        Return 0 if there is no mountain.

        Example 1:

        Input: [2,1,4,7,3,2,5]
        Output: 5
        Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
        Example 2:

        Input: [2,2,2]
        Output: 0
        Explanation: There is no mountain.
        Note:

        0 <= A.length <= 10000
        0 <= A[i] <= 10000

        Follow up:

        Can you solve it using only one pass?
        Can you solve it in O(1) space?
        
        :type A: List[int]
        :rtype: int

        O(n^2)

        """

        if not A or len(A) < 3:
            return 0
        ans = 0
        for i in range(1, len(A)-1):
            ans = max(ans, self.mountain(A, i))
        return ans

    def mountain(self, A, top):
        l = top - 1
        r = top + 1

        if A[l] < A[top] > A[r]:
            l -= 1
            while l > -1 and A[l] < A[l+1]:
                l -= 1
            r += 1
            while r < len(A) and A[r] < A[r-1]:
                r += 1
            return r - l - 1
        else:
            return -1




class SolutionII:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) < 3:
            return 0
        ans = 0
        found_top = pass_top = False
        s = e = 0
        while s < len(A) - 2 and e < len(A):
            if not found_top:
                while e + 1 < len(A) and A[e] < A[e+1]:
                    if not found_top:
                        found_top = True
                    e += 1

                if not found_top:
                    # no mountain, restart the new search
                    found_top = False
                    pass_top = False
                    s = e + 1
                    e = s
            else:
                while e + 1 < len(A) and A[e] > A[e+1]:
                    pass_top = True
                    e += 1

                if found_top and pass_top:
                    ans = max(ans, e - s + 1)
                    # a mountain is found, reset the search starting from e.
                    s = e
                    found_top = False
                    pass_top = False
                else:
                    # no mountain, restart the new search
                    found_top = False
                    pass_top = False
                    s = e + 1
                    e = s

        # do not forget the last mountain if exists
        if found_top and pass_top:
            ans = max(ans, e - s + 1)
        return ans

# class BestSolution:
#     def longestMountain(self, A):
#         """
#         Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
#
#         B.length >= 3
#         There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
#         (Note that B could be any subarray of A, including the entire array A.)
#
#         Given an array A of integers, return the length of the longest mountain.
#
#         Return 0 if there is no mountain.
#
#         Example 1:
#
#         Input: [2,1,4,7,3,2,5]
#         Output: 5
#         Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
#         Example 2:
#
#         Input: [2,2,2]
#         Output: 0
#         Explanation: There is no mountain.
#         Note:
#
#         0 <= A.length <= 10000
#         0 <= A[i] <= 10000
#
#         Follow up:
#
#         Can you solve it using only one pass?
#         Can you solve it in O(1) space?
#
#         :type A: List[int]
#         :rtype: int
#         """
#
#         if not A or len(A) < 3:
#             return 0
#         ans = 0
#         up = down = 0
#         for i in range(1, len(A)):
#             if (down and A[i-1] < A[i]) or A[i-1] == A[i]:
#                 up = down = 0
#             up += A[i - 1] < A[i]
#             down += A[i - 1] > A[i]
#             if up and down:
#                 ans = max(ans, up + down + 1)
#         return ans

s = SolutionII()
# print(s.longestMountain([2,1,4,7,3,2,5]))
# print(s.longestMountain([1,2,2,2]))
print(s.longestMountain([0, 1, 0, 2, 2]))
# print(s.longestMountain([0, 1, 2, 3, 4, 5, 6, 7, 98, 9]))