import math

class Solution:
    def threeSumMulti(self, A, target):
        """
        Given an integer array A, and an integer target, return the number of tuples i, j, k
        such that i < j < k and A[i] + A[j] + A[k] == target.

        As the answer can be very large, return it modulo 10^9 + 7.

        Example 1:

        Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
        Output: 20
        Explanation:
        Enumerating by the values (A[i], A[j], A[k]):
        (1, 2, 5) occurs 8 times;
        (1, 3, 4) occurs 8 times;
        (2, 2, 4) occurs 2 times;
        (2, 3, 3) occurs 2 times.
        Example 2:

        Input: A = [1,1,2,2,2,2], target = 5
        Output: 12
        Explanation:
        A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
        We choose one 1 from [1,1] in 2 ways,
        and two 2s from [2,2,2,2] in 6 ways.

        Note:

        3 <= A.length <= 3000
        0 <= A[i] <= 100
        0 <= target <= 300

        :type A: List[int]
        :type target: int
        :rtype: int

        Three sum problem variation: two pointer, given a solution (x, y, z), calculate frequency hash and use combination to count.
        then move pointers until a new different solution is encoutered.
        """
        modnum = int(10**9 + 7)
        numfreq = dict()
        for num in A:
            numfreq[num] = numfreq.get(num, 0) + 1

        A.sort()
        ans = 0
        for i in range(len(A)-2):
            if i > 0 and A[i] == A[i-1]:
                continue
            j = i + 1
            k = len(A)-1
            while j < k:
                numsum = A[i] + A[j] + A[k]
                if numsum == target:
                    ans += self.count([A[i], A[j], A[k]], numfreq)

                    j += 1
                    while j < len(A) and A[j] == A[j-1]:
                        j += 1

                    k -= 1
                    while k > -1 and A[k] == A[k+1]:
                        k -= 1
                elif numsum < target:
                    j += 1
                    while j < len(A) and A[j] == A[j-1]:
                        j += 1
                else:
                    k -= 1
                    while k > -1 and A[k] == A[k+1]:
                        k -= 1

        return int(ans % modnum)

    def count(self, solution, gfreq):
        lfreq = dict()
        for num in solution:
            lfreq[num] = lfreq.get(num, 0) + 1

        ans = 1
        for num in lfreq.keys():
            lf = lfreq[num]
            gf = gfreq[num]
            if gf == lf:
                ans *= 1
            else:
                # calculate combination lf out of gf.
                ans *= math.factorial(gf) / (math.factorial(lf) * math.factorial(gf - lf))

        return ans

s = Solution()
print(s.threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))