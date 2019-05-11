class DNCSolution:
    def reversePairs(self, nums):
        """
        Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

        You need to return the number of important reverse pairs in the given array.

        Example1:

        Input: [1,3,2,3,1]
        Output: 2
        Example2:

        Input: [2,4,3,5,1]
        Output: 3
        Note:
        The length of the given array will not exceed 50,000.
        All the numbers in the input array are in the range of 32-bit integer.

        :type nums: List[int]
        :rtype: int

        divide and conquer.

        1) the sum of # of reverse pairs in the left and right
        2) sorted left and right half and use two pointers to find all possible reverse pairs.

        """

        # note that divide and conquer must have a input larger than 2.
        if len(nums) <= 1:
            return 0
        elif len(nums) == 2:
            if nums[0] > 2*nums[1]:
                return 1
            else:
                return 0

        s = 0
        e = len(nums)
        m = (s + e) // 2

        ans1 = self.reversePairs(nums[s:m+1])
        ans2 = self.reversePairs(nums[m+1:e])
        nums1 = sorted(nums[s:m+1])
        nums2 = sorted(nums[m+1:e])
        i = s
        j = m + 1
        ans = ans1 + ans2
        while i < m + 1 and j < e:
            if nums1[i] > 2*nums2[j-m-1]:
                ans += m + 1 - i
                j += 1
            else:
                i += 1
        return ans

s = DNCSolution()
print(s.reversePairs([1,3,2,3,1]))

