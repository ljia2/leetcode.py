class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

        Formally, we can partition the array if we can find indexes i+1 < j
        with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])



        Example 1:

        Input: [0,2,1,-6,6,-7,9,1,2,0,1]
        Output: true
        Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
        Example 2:

        Input: [0,2,1,-6,6,7,9,-1,2,0,1]
        Output: false
        Example 3:

        Input: [3,3,6,5,-2,2,5,1,-9,4]
        Output: true
        Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


        Note:

        3 <= A.length <= 50000
        -10000 <= A[i] <= 10000
        :type A: List[int]
        :rtype: bool
        """

        if not A or len(A) < 3:
            return False

        Asum = sum(A)
        if Asum % 3 != 0:
            return False
        tsum = int(Asum / 3)

        ans = 0
        psum = 0
        for a in A:
            if psum != tsum:
                psum += a
            else:
                ans += 1
                psum = a

        if psum > 0:
            if psum != tsum:
                return False
            else:
                ans += 1
                return ans == 3
        else:
            if psum % tsum != 0:
                return False
            ans -= int(psum / tsum)
            return ans == 3


s = Solution()
print(s.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
print(s.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(s.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
print(s.canThreePartsEqualSum([12,-4,16,-5,9,-3,3,8,0]))