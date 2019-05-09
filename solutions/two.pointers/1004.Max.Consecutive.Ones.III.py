class Solution(object):
    def longestOnes(self, A, K):
        """
        Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

        Return the length of the longest (contiguous) subarray that contains only 1s.

        Example 1:

        Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
        Output: 6
        Explanation:
        [1,1,1,0,0,1,1,1,1,1,1]
        Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

        Example 2:

        Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
        Output: 10
        Explanation:
        [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
        Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


        Note:

        1 <= A.length <= 20000
        0 <= K <= A.length
        A[i] is 0 or 1

        :type A: List[int]
        :type K: int
        :rtype: int

        1 <= A.length <= 20000 hints either O(nlogn) or O(n).

        keep a sliding window of start and end.

        keep expanding the window by moving end to right until the maximum window with zero quota of 0s; update the max_length;

        keep shrinking the window by moving start to end to find a new window with nonzero quota of 0s; go to step 2.

        """

        if len(A) <= 2:
            return len(A)

        start = end = 0
        max_length = -1
        zero_quota = K
        while end < len(A):
            # keep expanding to the maximum window with zero quota.
            while end < len(A) and (A[end] == 1 or zero_quota > 0):
                if A[end] == 0:
                    zero_quota -= 1
                end += 1
            # a window with at most zero_quoto 0s is found; update the max length of the qualified window.
            max_length = max(max_length, end - start)

            if end < len(A):
                # retreat start to find the start of another window with non-zero quota.
                while start <= end and zero_quota == 0:
                    if A[start] == 0:
                        zero_quota += 1
                    start += 1
        return max_length


s = Solution()
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 0))

