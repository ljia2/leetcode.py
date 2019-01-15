class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        In an array A of 0s and 1s, how many non-empty subarrays have sum S?
        Example 1:

        Input: A = [1,0,1,0,1], S = 2
        Output: 4
        Explanation:
        The 4 subarrays are bolded below:
        [1,0,1,0,1]
        [1,0,1,0,1]
        [1,0,1,0,1]
        [1,0,1,0,1]


        Note:

        A.length <= 30000
        0 <= S <= A.length
        A[i] is either 0 or 1.

        :type A: List[int]
        :type S: int
        :rtype: int
        """
        if not A or S < 0:
            return 0

        s = e = 0
        subarray = [A[s]]


