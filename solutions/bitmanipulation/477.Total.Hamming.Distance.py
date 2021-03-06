class Solution(object):
    def totalHammingDistance(self, nums):
        """
        The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

        Now your job is to find the total Hamming distance between all pairs of the given numbers.

        Example:
        Input: 4, 14, 2

        Output: 6

        Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
        showing the four bits relevant in this case). So the answer will be:
        HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.


        Note:
        Elements of the given array are in the range of 0 to 10^9
        Length of the array will not exceed 10^4.

        :type nums: List[int]
        :rtype: int

        iterate over each bit of all numbers to count the number of 1.

        if there are bidCount 1's at position of pos, they will contribute to bitCount * (len(nums) - bitCount) hamming distance.


        """

        if not nums:
            return 0

        res = 0
        for pos in range(32):
            bitCount = 0
            for i in range(len(nums)):
                bitCount += (nums[i] >> pos) & 1
            res += bitCount * (len(nums) - bitCount)
        return res

