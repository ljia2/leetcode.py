class Solution:
    def firstMissingPositive(self, nums):
        """
        Given an unsorted integer array, find the smallest missing positive integer.

        Example 1:

        Input: [1,2,0]
        Output: 3

        Example 2:

        Input: [3,4,-1,1]
        Output: 2
        Example 3:

        Input: [7,8,9,11,12]
        Output: 1

        Note:
        Your algorithm should run in O(n) time and uses constant extra space.

        :type nums: List[int]
        :rtype: int

        Basic idea:
            1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
                so we only have to care about those elements in this range and remove the rest.
            2. we can use the array index as the hash to restore the frequency of each number within
                 the range [1,...,l+1]

        same as LC268.

        """
        if not nums:
            return 1
        # expand nums from l to l + 1 space.
        nums.append(0)
        n = len(nums)

        # delete those useless elements
        for i, num in enumerate(nums):
            if num >= n or num < 0:
                nums[i] = 0
        # use nums[i] as the index to restore the frequency of num within [1, l + 1]
        # if num[i] = 1, update nums[1] += n (the original number plusing n).
        for i in range(n):
            nums[nums[i] % n] += len(nums)

        for i in range(1, n):
            # if nums[i] < n, there is no number i.
            if int(nums[i] / len(nums)) == 0:
                return i
        return n


s = Solution()
print(s.firstMissingPositive([1, 2, 0]))
print(s.firstMissingPositive([0, 3]))

