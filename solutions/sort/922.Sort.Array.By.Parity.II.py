class Solution:
    def sortArrayByParityII(self, A):
        """
        Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
        Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
        You may return any answer array that satisfies this condition.

        Example 1:

        Input: [4,2,5,7]
        Output: [4,5,2,7]
        Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

        Note:
        2 <= A.length <= 20000
        A.length % 2 == 0
        0 <= A[i] <= 1000

        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        ans = [0] * len(A)
        for i in range(len(even)):
            ans[2*i] = even[i]
            ans[2*i+1] = odd[i]
        return ans


