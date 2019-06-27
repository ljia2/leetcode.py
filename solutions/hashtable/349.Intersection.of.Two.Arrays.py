from collections import Counter


class SolutionI(object):
    def intersection(self, nums1, nums2):
        """
        Given two arrays, write a function to compute their intersection.

        Example 1:

        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2]
        Example 2:

        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [9,4]
        Note:

        Each element in the result must be unique.
        The result can be in any order.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if not nums1 or not nums2:
            return []
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        ans = []
        for k in counter1.keys():
            if k in counter2.keys():
                ans.append(k)
        return ans


class SolutionII(object):
    def intersection(self, nums1, nums2):
        """
        Given two arrays, write a function to compute their intersection.

        Example 1:

        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2]
        Example 2:

        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [9,4]
        Note:

        Each element in the result must be unique.
        The result can be in any order.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if not nums1 or not nums2:
            return []

        set1 = set(nums1)
        set2 = set(nums2)
        # use build-in intersect &
        return list(set1 & set2)

### Follow up: If two arrays are sorted and one long and one short?
import bisect
class VarationSolution(object):
    def intersection(self, nums1, nums2):
        """
        Given two sorted arrays, one long and one short, write a function to compute their intersection.

        Example 1:

        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2]
        Example 2:

        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [9,4]
        Note:

        Each element in the result must be unique.
        The result can be in any order.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if not nums1 or not nums2:
            return []

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        ans = []
        for num in nums1:
            index = bisect.bisect_left(nums2, num)
            if index < len(nums2) and nums2[index] == num:
                ans.append(num)
        return ans
