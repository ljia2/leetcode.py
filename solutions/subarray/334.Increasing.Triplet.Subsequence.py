class Solution:
    def increasingTriplet(self, nums):
        """
        Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

        Formally the function should:

        Return true if there exists i, j, k
        such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
        Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

        Example 1:

        Input: [1,2,3,4,5]
        Output: true
        Example 2:

        Input: [5,4,3,2,1]
        Output: false

        :type nums: List[int]
        :rtype: bool

        min1 = k, we are looking for a range > k
        min2 = j, we are looking for a range < j

        For example, [8, 3, 2, 4, 1, 5]

        initially, min1 = min2 = 8 + 1

        then iterate over nums,

        1) 8 < min1 = min2 => min1 = 8, min2 = 9
        2) 3 < min1 < min2 => min1 = 3, min2 = 9 # no need to update min2, because now we only encouter min1 = 3 without a tuple of increasing number yet
        3) 2 < min1 < min2 => min1 = 2, min2 = 9 # same above
        4) min1 < 4 < min2 => min1 = 2, min2 = 4 # we update min2, we have countered a tuple of increasing numbers and as long as the third number > 4, return True
        5) 1 < min1 < min2 => min1 = 1, min2 = 4 # Note here, no need to update min2, because min2 is a range indicator, i.e. we have two numbers a < b = 4. We just look for c > 4 to find a triple of increasing numbers.
        6) min1 < min2 < 5 => return True
        """
        if len(nums) < 3:
            return False

        max_num = max(nums) + 1
        min1 = min2 = max_num

        for i in range(len(nums)):
            if nums[i] < min1:
                # update min1, because the new min1 is more likely to get a triple than the old min2
                min1 = nums[i]
            elif min1 < nums[i] < min2:
                min2 = nums[i]
            elif nums[i] > min2:
                return True
            else:
                # other equal conditions, no updates
                continue
        return False




