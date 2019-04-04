class Solution(object):
    def largestPerimeter(self, A):
        """
        Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area,
        formed from 3 of these lengths.

        If it is impossible to form any triangle of non-zero area, return 0.

        Example 1:

        Input: [2,1,2]
        Output: 5
        Example 2:

        Input: [1,2,1]
        Output: 0
        Example 3:

        Input: [3,2,3,4]
        Output: 10
        Example 4:

        Input: [3,6,2,3]
        Output: 8


        Note:

        3 <= A.length <= 10000
        1 <= A[i] <= 10^6

        :type A: List[int]
        :rtype: int

        sort A and find the biggest A[i] s.t. A[i] < A[i-1] + A[i-2].
        """
        if not A or len(A) < 3:
            return 0

        A.sort()
        # find the first end s.t. A[end-2] + A[end-1] > A[end]
        end = len(A) - 1
        while end > 1 and A[end-2] + A[end-1] <= A[end]:
            end -= 1

        if end >= 2:
            return sum(A[end-2:end+1])
        else:
            return 0

