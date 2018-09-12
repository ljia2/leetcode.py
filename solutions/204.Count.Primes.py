class Solution:
    def countPrimes(self, n):
        """
        Count the number of prime numbers less than a non-negative number, n.

        Example:

        Input: 10
        Output: 4
        Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n

        primes[0] = primes[1] = False

        for i in range(2, int(n ** 0.5) + 1): # int(n**0.5) + 1 is the upper bound of factor of n
            if primes[i]:
                # for each prime factor i, mark all numbers < n can be multiple of i
                for j in range(i * i, n, i):
                    primes[j] = False
        return sum(primes)