import bisect

class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        """
        A sorted list A contains 1, plus some number of primes.
        Then, for every p < q in the list, we consider the fraction p/q.

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


       Remarks:

        The kth smallest fraction is known to be in the range [0, 1], so we initialize the search space with this range (i.e., l = 0 and r = 1).

        We need the pair (p, q) to record the maximum fraction in the matrix that is no greater than each candidate solution. This is necessary because on the one hand, the candidate solution itself cannot tell us what the numerator and denominator of the fraction are (remember the candidate solution is just a floating-point number); on the other hand, even if we can get the numerator and denominator of the candidate solution, these values may not be contained in the input array (remember all the fractions must be formed by pair of integers from the input array). This is different from the case when the matrix elements are integers, where at the end of the binary search, the candidate solution must be equal to the kth smallest element in the matrix.

        The above solution only works when there are no duplicate fractions in the matrix (which is indeed the case for prime fractions). Otherwise, we need two counts, cnt_le and cnt_lt, to account for duplicates, similar to what we did in the ZigzagSearch solution below.

        The time complexity is computed as follows: the binary search loop will terminate when the count of elements no greater than a candidate solution reaches K. This is guaranteed to happen when the size of the search range [l, r] becomes smaller than the smallest absolute distance between any pair of fractions in the matrix, which is >= 1/MAX^2. Since each iteration will reduce the search range by half, the binary search loop will terminate after at most log(MAX^2) steps. Each iteration is done in linear time, therefore the total time complexity is O(n * log(MAX^2)), which is equivalent to O(n * log(MAX)).


        """
        l = 0
        r = 1
        # NOTE THAT l and r are searching floating space and they never meet !!!!!
        while True:
            m = (l + r) / 2
            lt, ans = self.count(A, m)
            if lt == K:
                return ans

            if lt > K:
                r = m
            elif lt < K:
                l = m

    def count(self, A, r):
        cnt = 0
        ans = [0, 1]
        for i, a in enumerate(A):
            # want to find all b s.t. a/b < r and a < b => b > a/r
            # j is the first index of b s.t. a/b < r
            j = bisect.bisect_right(A, a/r)
            if j < len(A):
                cnt += len(A) - j
                # update ans to record the maximum fraction existing a/b < r.
                if ans[0]/ans[1] < A[i] / A[j]:
                    ans[0] = A[i]
                    ans[1] = A[j]
        return cnt, ans

s = Solution()
#print(s.kthSmallestPrimeFraction([1, 2, 3, 5], 3))
#print(s.kthSmallestPrimeFraction([1, 29, 47], 1))
print(s.kthSmallestPrimeFraction([1,13,17,59], 6))