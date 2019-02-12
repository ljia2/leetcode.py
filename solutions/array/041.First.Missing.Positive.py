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

        nums.append(0)
        for i, num in enumerate(nums):
            if num >= len(nums) or num < 0:
                nums[i] = 0

        for i in range(len(nums)):
            if nums[i] % len(nums) == 0:
                continue
            # use nums[i] as the index to restore the frequency of num within [1, l + 1]
            # nums[1] representing 1, nums[2] representing 2 and so on.
            nums[nums[i] % len(nums)] += len(nums)

        for i in range(1, len(nums)):
            if nums[i] // len(nums) == 0:
                return i
        return len(nums)

s = Solution()
#print(s.firstMissingPositive([1, 2, 0]))
print(s.firstMissingPositive([0, 3]))

