class DCSolution:
    def beautifulArray(self, N):
        """
        For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

        For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

        Given N, return any beautiful array A.  (It is guaranteed that one exists.)

        Example 1:

        Input: 4
        Output: [2,1,4,3]
        Example 2:

        Input: 5
        Output: [3,1,2,5,4]

        Note:

        1 <= N <= 1000

        1000 hints O(n^2)

        :type N: int
        :rtype: List[int]
        """

        if N == 1:
            return [1]
        else:
            k = (N + 1) // 2
            base = self.beautifulArray(k)
            odd = [2*i - 1 for i in base]
            even = [2*i for i in base]
            res = odd + even
            return list(filter(lambda x: x<=N, res))

s = DCSolution()
print(s.beautifulArray(5))
print(s.beautifulArray(6))