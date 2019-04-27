"""
Given an array of integers with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);


Reservoir Sampling: Samping from Stream.


"""

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.rand = random

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ans = -1
        count = -1
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            count += 1
            # random pick from [0, count]
            if self.rand.randint(0, count) == 0:
                # keep updating ans index if there are duplication.
                ans = i

        return ans

# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3, 3 ,3])
print(obj.pick(3))
print(obj.pick(3))
print(obj.pick(3))