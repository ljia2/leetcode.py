class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

        Find all the elements of [1, n] inclusive that do not appear in this array.

        Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

        Example:

        Input:
        [4,3,2,7,8,2,3,1]

        Output:
        [5,6]

        :type nums: List[int]
        :rtype: List[int]

        For each number i in nums,
        we mark the number that i points as negative.
        Then we filter the list, get all the indexes
        who points to a positive number.
        Since those indexes are not visited.

        for numbers in [1, n] whose indexes should be 0 .. n - 1.

        """

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(s.findDisappearedNumbers([1, 1]))
print(s.findDisappearedNumbers([2, 1]))