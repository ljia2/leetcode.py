class Solution(object):
    def singleNumber(self, nums):
        """
        Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

        Example:

        Input:  [1,2,1,3,2,5]
        Output: [3,5]
        Note:

        The order of the result is not important. So in the above example, [5, 3] is also correct.
        Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

        :type nums: List[int]
        :rtype: List[int]

        *以前有个经典例子，使用异或可以不借助中间变量交换两个数字：
        In [203]: a, b = 1, 2
        In [204]: a = a ^ b
        In [205]: b = a ^ b
        In [206]: a = a ^ b
        In [207]: print a, b
        2 1

        一些其他特性：
        0 ^ n = n
        n ^ n = 0

        假定：
        l = [a, b, c1, c2, d1, d2, ......, z1, z2]

        中，a，b 是唯一的两个数，其它字母相同的是同样的数。
        那么：
        c1 ^ c2 = 0
        ...
        z1 ^ z2 = 0

        a ^ b ^ c1 ^ c2 ^ ... ^ z1 ^ z2 = a ^ b ^ (c1 ^ c2) ^ ... ^ (z1 ^ z2) = a ^ b ^ 0 ^ ... ^ 0 = a ^ b

        因为 a 和 b 是不同的，即 a ^ b != 0，因此他们至少有一位是不同的，如对于 3 和 5 而言，

           011  -> 3
        ^  101  -> 5
        ----------
           110  -> 6

        6 的右数第二、三位均为 1，即 3 和 5 的右数第二、三位是不同的，因此我们可以用这一位来区分 3 和 5。
        如取第二位，则为 10，值为2。

        2 & 3 = 2
        2 & 5 = 0

        """
        bit_num = 0
        for num in nums:
            bit_num ^= num

        # find the lowest bit 1, meaning both single numbers differ at that bit.
        mask = 1
        a = b = bit_num
        while bit_num & mask == 0:
            mask = mask << 1

        # separate numbers into two groups different at the second bit
        # then do the same trick of xor.
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]

s = Solution()
print(s.singleNumber([1,2,1,3,2,5]))