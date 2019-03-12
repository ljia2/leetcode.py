class Solution(object):
    def addToArrayForm(self, A, K):
        """
        For a non-negative integer X, the array-form of X is an array of its digits in left to right order.
        For example, if X = 1231, then the array form is [1,2,3,1].

        Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

        Example 1:

        Input: A = [1,2,0,0], K = 34
        Output: [1,2,3,4]
        Explanation: 1200 + 34 = 1234
        Example 2:

        Input: A = [2,7,4], K = 181
        Output: [4,5,5]
        Explanation: 274 + 181 = 455
        Example 3:

        Input: A = [2,1,5], K = 806
        Output: [1,0,2,1]
        Explanation: 215 + 806 = 1021
        Example 4:

        Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
        Output: [1,0,0,0,0,0,0,0,0,0,0]
        Explanation: 9999999999 + 1 = 10000000000


        Note：

        1 <= A.length <= 10000
        0 <= A[i] <= 9
        0 <= K <= 10000
        If A.length > 1, then A[0] != 0

        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """

        if K == 0:
            return A

        kdigits = []
        while K > 0:
            kdigits.append(K % 10)
            K = int(K / 10)
        kdigits.reverse()

        if not A:
            return kdigits

        carry = 0
        a = len(A) - 1
        k = len(kdigits) - 1
        ans = []
        while a > -1 and k > -1:
            nd = A[a] + kdigits[k] + carry
            carry = nd // 10
            ans.append(nd % 10)
            a -= 1
            k -= 1

        if a > -1:
            while a > -1:
                nd = A[a] + carry
                carry = nd // 10
                ans.append(nd % 10)
                a -= 1
        elif k > -1:
            while k > -1:
                nd = kdigits[k] + carry
                carry = nd // 10
                ans.append(nd % 10)
                k -= 1

        # do not forget the carry after existing while loop
        if carry > 0:
            ans.append(carry)
        ans.reverse()
        return ans

s = Solution()
print(s.addToArrayForm([1, 2, 0, 0], 34))

