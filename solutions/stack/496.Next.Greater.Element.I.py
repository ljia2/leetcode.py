class Solution: # Brute Force
    def nextGreaterElement(self, nums1, nums2):
        """
        You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
        Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

        The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
        If it does not exist, output -1 for this number.

        Example 1:
        Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
        Output: [-1,3,-1]
        Explanation:
            For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
            For number 1 in the first array, the next greater number for it in the second array is 3.
            For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

        Example 2:
        Input: nums1 = [2,4], nums2 = [1,2,3,4].
        Output: [3,-1]
        Explanation:
            For number 2 in the first array, the next greater number for it in the second array is 3.
            For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

        Note:
        All elements in nums1 and nums2 are unique.
        The length of both nums1 and nums2 would not exceed 1000.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        T: O(n^2)
        S: O(n)

        """

        if not nums1 or not nums2:
            return []

        ng = dict()
        for i in range(len(nums2)):
            for j in range(i, len(nums2)):
                if nums2[j] > nums2[i]:
                    ng[nums2[i]] = nums2[j]
                    break
            if nums2[i] not in ng.keys():
                ng[nums2[i]] = -1

        results = []
        for i in range(len(nums1)):
            results.append(ng[nums1[i]])
        return results

class LinearSolution: # Linear Time
    def nextGreaterElement(self, nums1, nums2):
        """
        You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
        Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

        The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
        If it does not exist, output -1 for this number.

        Example 1:
        Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
        Output: [-1,3,-1]
        Explanation:
            For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
            For number 1 in the first array, the next greater number for it in the second array is 3.
            For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

        Example 2:
        Input: nums1 = [2,4], nums2 = [1,2,3,4].
        Output: [3,-1]
        Explanation:
            For number 2 in the first array, the next greater number for it in the second array is 3.
            For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

        Note:
        All elements in nums1 and nums2 are unique.
        The length of both nums1 and nums2 would not exceed 1000.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Can you do better than O(n^2)

        Scaning from rear to the begining:
        if nums[j] < nums[j+1]: ng[j] = nums[j+1]
        otherwise:
           found = false
           next = ng[j+1]
           while -1 < next < len(nums2) and nums2[next] <= nums2[j]:
                next = ng[nums2[next]]
           ....
        """

        if not nums1 or not nums2:
            return []

        ng = dict()
        ng[nums2[len(nums2)-1]] = -1
        for i in range(len(nums2)-2, -1, -1):
            if nums2[i] < nums2[i+1]:
                ng[nums2[i]] = i+1
            else:
                next = ng[nums2[i+1]]
                while -1 < next < len(nums2) and nums2[next] < nums2[i]:
                    next = ng[nums2[next]]
                if -1 < next < len(nums2):
                    ng[nums2[i]] = next
                else:
                    ng[nums2[i]] = -1

        results = []
        for i in range(len(nums1)):
                j = ng.get(nums1[i], -1)
                results.append(nums2[j] if j > -1 else -1)

        return results

class LinearSolutionII: # Linear Time
    def nextGreaterElement(self, nums1, nums2):
        """
        You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
        Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

        The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
        If it does not exist, output -1 for this number.

        Example 1:
        Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
        Output: [-1,3,-1]
        Explanation:
            For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
            For number 1 in the first array, the next greater number for it in the second array is 3.
            For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

        Example 2:
        Input: nums1 = [2,4], nums2 = [1,2,3,4].
        Output: [3,-1]
        Explanation:
            For number 2 in the first array, the next greater number for it in the second array is 3.
            For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

        Note:
        All elements in nums1 and nums2 are unique.
        The length of both nums1 and nums2 would not exceed 1000.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Can you do better than O(n^2)

        Scaning from rear to the begining:
        if nums2[j] < nums2[j+1]: ng[nums2[j]] = j + 1
        otherwise:
          use a monotonic stack to store all indexes of the numbers > nums2[i]

        """

        if not nums1 or not nums2:
            return []

        ng = dict()
        mstack = []
        for i in range(len(nums2)-1, -1, -1):
            # keep poping index of numbers <= nums[j], because all numbers < nums[i] will not be used ng number for numbers before i.
            while mstack and nums2[i] >= nums2[mstack[-1]]:
                mstack.pop()

            if mstack:
                ng[nums2[i]] = mstack[-1]
            else:
                ng[nums2[i]] = -1

            mstack.append(i)

        results = []
        for i in range(len(nums1)):
            j = ng.get(nums1[i], -1)
            results.append(nums2[j] if j > -1 else -1)

        return results

s = LinearSolutionII()
print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
print(s.nextGreaterElement([2, 4], [1, 2, 3, 4]))