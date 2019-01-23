class Solution:
    def preimageSizeFZF(self, K):
        """

        Let f(x) be the number of zeroes at the end of x!.
        (Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)

        For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has 2 zeroes at the end.
        Given K, find how many non-negative integers x have the property that f(x) = K.

        Example 1:
        Input: K = 0
        Output: 5

        Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

        Example 2:
        Input: K = 5
        Output: 0
        Explanation: There is no x such that x! ends in K = 5 zeroes.

        Note:

        K will be an integer in the range [0, 10^9]

        :type K: int
        :rtype: int


        how many 5, because 5* 2 = 10
        how many 25 in f(x) because 25* 2 = 100 (that contribute only the first zero, because the second zero is counted by 5 already)
        how many 125 in f(x) because 125 * 8 = 1000 ......

                ans = 0
                while x > 0:
                    ans += x // 5
                    x = x // 5
                K = ans

        now we want to find the smallest number that have K zeros at the end
        K being in the range of [0, 10^9] hints binary search over K.


        """
        return self.upper_bound(K) - self.lower_bound(K)

    # finding the smallest number whose ending zeros == K
    def lower_bound(self, K):
        if K == 0:
            return 0

        l = 0
        r = 5 * (K + 1)
        # again l and r are searching integer space.
        while l < r:
            mid = (l + r) // 2
            if self.countZero(mid) >= K:
                r = mid
            else:
                l = mid + 1
        return l if self.countZero(l) == K else 0

    # find out the smallest number whose ending zeros > K
    def upper_bound(self, K):
        if K == 0:
            return 5
        l = 0
        r = 5 * (K + 1)
        # again l and r are searching integer space.
        while l < r:
            mid = (l + r) // 2
            if self.countZero(mid) > K:
                r = mid
            else:
                l = mid + 1
        return l if self.countZero(l-1) == K else 0

    def countZero(self, x):
        ans = 0
        while x > 0:
            ans += x // 5
            x //= 5
        return ans

s = Solution()
print(s.preimageSizeFZF(28246))