class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """

        Given an array of integers and an integer k,
        find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
        and the absolute difference between i and j is at most k.

        Example 1:

        Input: nums = [1,2,3,1], k = 3
        Output: true
        Example 2:

        Input: nums = [1,0,1,1], k = 1
        Output: true
        Example 3:

        Input: nums = [1,2,3,1,2,3], k = 2
        Output: false

        :type nums: List[int]
        :type k: int
        :rtype: bool

        """

        if not nums or k < 1:
            return False

        # key is the number and value is the index
        pos = dict()
        for i in range(len(nums)):
            if nums[i] not in pos.keys():
                pos[nums[i]] = i
            else:
                lp = pos[nums[i]]
                if i - lp > k:
                    pos[nums[i]] = i
                else:
                    return True
        return False


