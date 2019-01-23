from heapq import heappop, heappush

class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        """
        A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.

        What is the K-th smallest fraction considered?
        Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

        Examples:
        Input: A = [1, 2, 3, 5], K = 3
        Output: [2, 5]
        Explanation:

        The fractions to be considered in sorted order are:
        1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
        The third fraction is 2/5.

        Input: A = [1, 7], K = 1
        Output: [1, 7]

        Note:
        A will have length between 2 and 2000.
        Each A[i] will be between 1 and 30000.
        K will be between 1 and A.length * (A.length - 1) / 2.

        :type A: List[int]
        :type K: int
        :rtype: List[int]

        1) matrix[i][j] = A[i] / A[j]
        2) initialize the heap with matrix[1][j] 2 <= j < len(A).
        3) keep pop element (i, j) and add the new number i + 1, j if i + 1 < j.
        4) repeat the kth fraction is poped.
        """

        hp = []
        for j in range(1, len(A)):
            heappush(hp, (A[0]/A[j], 0, j))

        ans = []
        while hp and K > 0:
            _, i, j = heappop(hp)
            K -= 1
            if K == 0:
                ans.append(A[i])
                ans.append(A[j])
                break
            if i + 1 < j:
                heappush(hp, (A[i+1]/A[j], i+1, j))
        return ans

s = Solution()
print(s.kthSmallestPrimeFraction([1, 2, 3, 5], 3))