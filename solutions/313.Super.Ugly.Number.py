class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        Write a program to find the nth super ugly number.

        Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

        Example:

        Input: n = 12, primes = [2,7,13,19]
        Output: 32
        Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
        super ugly numbers given primes = [2,7,13,19] of size 4.

        Note

        1 is a super ugly number for any given primes.
        The given numbers in primes are in ascending order.
        0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
        The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        prime_index = [0] * len(primes)
        max_num = max(primes) ** n
        ugly = [0] * n
        ugly[0] = 1
        for i in range(1, n, 1):
            next_ugly = max_num
            for j in range(len(primes)):
                if next_ugly > ugly[prime_index[j]] * primes[j]:
                    next_ugly = ugly[prime_index[j]] * primes[j]
            for j in range(len(primes)):
                if next_ugly == ugly[prime_index[j]] * primes[j]:
                    prime_index[j] += 1
            ugly[i] = next_ugly
        return ugly[n-1]

s = Solution()
print(s.nthSuperUglyNumber(12, [2,7,13,19]))




