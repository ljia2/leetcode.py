from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        Given two arrays, write a function to compute their intersection.

        Example 1:

        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2,2]
        Example 2:

        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [4,9]
        Note:

        Each element in the result should appear as many times as it shows in both arrays.
        The result can be in any order.
        Follow up:

        What if the given array is already sorted? How would you optimize your algorithm?
        What if nums1's size is small compared to nums2's size? Which algorithm is better?
        What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if not nums1 or not nums2:
            return []

        freq1 = Counter(nums1)
        freq2 = Counter(nums2)

        if len(freq1.keys()) > len(freq2.keys()):
            freq1, freq2 = freq2, freq1
        ans = []
        for k, v in freq1.items():
            if k in freq2.keys():
                ans += [k] * min(v, freq2[k])
        return ans


"""
Follow up:

What if the given array is already sorted? How would you optimize your algorithm? merge directly 
What if nums1's size is small compared to nums2's size? Which algorithm is better? iterate over short and bisect over long
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
segment nums2 and merge num1 and a segment of nums2. 
"""
