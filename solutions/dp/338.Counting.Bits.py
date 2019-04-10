class Solution:
    def countBits(self, num):
        """

        Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

        Example 1:

        Input: 2
        Output: [0,1,1]
        Example 2:

        Input: 5
        Output: [0,1,1,2,1,2]
        Follow up:

        It is very easy to come up with a solution with run time O(n*sizeof(integer)).
        But can you do it in linear time O(n) /possibly in a single pass?

        Space complexity should be O(n).
        Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

        :type num: int
        :rtype: List[int]

        First, we know that when a number * 2, it means this number shifts a bit in binary. And in every number + 1 case,
        odd number always mean add 1 count in the 1’s count of the number in binary and we can know that:
        answer[n] = answer[n >> 1] + (n & 1)
        """

        dp = [0]*(num + 1)
        for i in range(1, num+1, 1):
            if i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i >> 1] + (i & 1)
        return dp


s = Solution()
print(s.countBits(4))
