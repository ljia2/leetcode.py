class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        There are two sorted arrays nums1 and nums2 of size m and n respectively.

        Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

        You may assume nums1 and nums2 cannot be both empty.

        Example 1:

        nums1 = [1, 3]
        nums2 = [2]

        The median is 2.0
        Example 2:

        nums1 = [1, 2]
        nums2 = [3, 4]

        The median is (2 + 3)/2 = 2.5

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        O(log(m + n)) implies binary search


        C[:K] consists of the first m1 elements from nums1 and the first m2 elements from nums2 where m1 + m2 = k = (m + n + 1) // 2

        if (m + n) % 2 == 0:
            median = (C[K-1] + C[K]) / 2
        else:
            median = C[K-1]

        C[K-2 = min(A[m1-1], B[m2-1])


        C[K-1] = max(A[m1-1], B[m2-1]) # c1 for code below
        C[K] = min(A[m1], B[m2]) # c2 for code below

        C[K+1] = max(A[m1], B[m2])

        Therefore, we only need A[m1-1], A[m1], B[m2-1], B[m2] to calculate the median

        given m1, binary search on A while A[m1] < B[m2-1] until A[m1] >= B[m2-1]


        """

        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        k = (n1 + n2 + 1) // 2

        l = 0
        r = n1
        while l < r:
            m1 = (l + r) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]: # try to find nums[m1] >= nums2[m2-1]
                l = m1 + 1
            else:
                r = m1

        m1, m2 = l, k - l
        c1 = max(-2**31 if m1 <= 0 else nums1[m1-1], -2**31 if m2 <= 0 else nums2[m2-1])

        if (n1 + n2) % 2 == 1:
            return c1

        c2 = min(2**31-1 if m1 >= n1 else nums1[m1], 2**31-1 if m2 >= n2 else nums2[m2])

        return (c1 + c2) * 0.5

s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))



        