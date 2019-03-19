class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

        For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
        OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
        That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

        Return the length of a maximum size turbulent subarray of A.


        Example 1:

        Input: [9,4,2,10,7,8,8,1,9]
        Output: 5
        Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
        Example 2:

        Input: [4,8,12,16]
        Output: 2

        Example 3:

        Input: [100]
        Output: 1
        :type A: List[int]
        :rtype: int

        two pointers, start and end.
        """

        if len(A) <= 1:
            return len(A)

        start = end = 0
        max_size = 1
        while end < len(A):
            end = start + 1
            while end + 1 < len(A) and ((A[end-1] < A[end] and A[end] > A[end+1]) or (A[end-1] > A[end] and A[end] < A[end+1])):
                end += 1

            # special case: A[end-1] < A[end] or A[end-1] > A[end] only
            if end < len(A) and end == start + 1 and A[end] != A[start]:
                max_size = max(max_size, 2)
            # A[end-1] < A[end] > A[end+1] or A[end-1] > A[end] < A[end+1]
            elif end > start + 1:
                max_size = max(max_size, end - start + 1)
            # reset the start
            start = end
        return max_size

s = Solution()
print(s.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
print(s.maxTurbulenceSize([1, 1, 1, 1]))






