class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

        Example 1:

        Input: A = [4,5,0,-2,-3,1], K = 5
        Output: 7

        Explanation: There are 7 subarrays with a sum divisible by K = 5:
        [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

        Note:
        1 <= A.length <= 30000
        -10000 <= A[i] <= 10000
        2 <= K <= 10000
        :type A: List[int]
        :type K: int
        :rtype: int

        I noted above that we need to find all prefix sum pairs (i,j) such tha (p[j] - p[i]) % K == 0.

        trick of number theory:

        (p[j] - p[i]) % K <=> p[i] % K == p[j] % K

        """
        if not A:
            return []

        if K == 0:
            raise Exception("K is zero! ")

        # key is mod and value is the frequency of indexes.
        modmap = dict()
        prefix_sum = 0
        for i, a in enumerate(A):
            prefix_sum += a
            # mod function of a positive always return positive
            # -9 % 2 == 1
            mod = prefix_sum % K
            modmap[mod] = modmap.get(mod, 0) + 1

        # then count the pair of prefix sum sharing the same reminder by % K.
        ans = 0
        for mod, c in modmap.items():
            # there are c subarries whose sum % k == mod
            # pair c subarrays to get c * (c - 1) // 2 subarrays whose sum % K == 0
            ans += c * (c - 1) // 2

        # there are also modmap[0] subarrys (if exists) whose sum is divisible by K.
        # they do not need pair.
        return ans + modmap.get(0, 0)


s = Solution()
print(s.subarraysDivByK([4,5,0,-2,-3,1], 5))
print(s.subarraysDivByK([-1,2,9], 2))
print(s.subarraysDivByK([5, 10], 5))