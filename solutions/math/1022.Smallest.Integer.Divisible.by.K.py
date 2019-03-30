class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

        Return the length of N.  If there is no such N, return -1.

        Example 1:

        Input: 1
        Output: 1
        Explanation: The smallest answer is N = 1, which has length 1.
        Example 2:

        Input: 2
        Output: -1
        Explanation: There is no such positive integer N divisible by 2.
        Example 3:

        Input: 3
        Output: 3
        Explanation: The smallest answer is N = 111, which has length 3.


        Note:

        1 <= K <= 10^5

        :type K: int
        :rtype: int

        For a given K, we evaluate 1 % K, 11 % K, 111 % K, ..., 11...1 (K '1's) % K.

        If any remainder is 0, then the current number is the smallest integer divisible by K.
        If none of the remainders is 0, then at some point,
        there must be some duplicate remainders (due to Pigeonhole principle),
        as the K remainders can only take at most K-1 different values excluding 0.

        In this case, no number with the pattern 1...1 is divisible by K.


        [This is because once a remainder has a duplicate, the next remainder will be in a loop, as the previous remainder determines the next_mod,]



        i.e., next_mod = (10 * prev_mod + 1) % K. Therefore, we will never see remainder==0.

        A simple example is when K is 6. Once we see 1111 % 6 = 1, we immediately know 11111 % 6 will be 5,
        since 1 % 6 = 1 and 11 % 6 = 5. Therefore, there will be no such number that is divisible by 6.

        1 % 6 = 1
        11 % 6 = 5
        111 % 6 = 3
        1111 % 6 = 1
        11111 % 6 = 5
        111111 % 6 = 3

        """
        if K % 10 not in {1, 3, 7, 9}: return -1

        mod, mod_set = 0, set()
        for length in range(1, K + 1):
            mod = (10 * mod + 1) % K
            if mod == 0: return length
            if mod in mod_set: return -1
            mod_set.add(mod)
        return -1


s = Solution()
print(s.smallestRepunitDivByK(19927))
