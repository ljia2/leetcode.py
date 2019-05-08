class Solution(object):
    def singleNumber(self, nums):
        """
        Given a non-empty array of integers, every element appears twice except for one. Find that single one.

        Note:

        Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

        Example 1:

        Input: [2,2,1]
        Output: 1
        Example 2:

        Input: [4,1,2,1,2]
        Output: 4

        :type nums: List[int]
        :rtype: int

        use XOR operation, for any number appearing twice, it will be XOR to 0. only the single number

        """

        ans = 0
        for num in nums:
            ans ^= num
        return ans

s = Solution()
print(s.singleNumber([5, 1, 2, 1, 2]))


## Varation: given a stream of characters, find determine whether it contains a character appearing in odd times. Same as above.

## Follow up I: given a array where all number but one appearing three times. Find that single number.

## Floow up 2: given an array where all number but two appearning twice. Find the pair of single numbers.