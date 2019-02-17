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

        subarrys => presum $Time: O(N), Space: O(N)$
        store previous sum and the times of this sum, because sum[i, j] = sum[0, j] - sum[0, i - 1], this is a very very important idea!!!!

        """
        if not A or S < 0:
            return 0

        sumdict = dict()
        # assuming there is a zero sum consisting of no elements from A
        sumdict[0] = 1
        cur_sum = 0
        ans = 0
        for i in range(len(A)):
            target = cur_sum - S
            if target in sumdict.keys():
                ans += sumdict[target]
            sumdict[cur_sum] = sumdict.get(cur_sum, 0) + 1

        return ans


s = Solution()
print(s.numSubarraysWithSum([1, 0, 0, 0, 1], 1))
print(s.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
print(s.numSubarraysWithSum([1, 1, 1, 0, 0], 1))










