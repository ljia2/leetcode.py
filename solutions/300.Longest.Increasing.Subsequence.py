class Solution: # Time Limit Exceeded O(n^2)
    def lengthOfLIS(self, nums):
        """
        Given an unsorted array of integers, find the length of longest increasing subsequence.

        Example:

        Input: [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
        Note:

        There may be more than one LIS combination, it is only necessary for you to return the length.
        Your algorithm should run in O(n2) complexity.
        Follow up: Could you improve it to O(n log n) time complexity?

        :type nums: List[int]
        :rtype: int

        max_len[i] denotes the longest increaing subsequence ending with num[i]
        """
        if not nums:
            return 0
        else:
            """
            Stores the longest length of subsequence ending at nums[i]
            """
            max_len = [1] * len(nums)
            """
            stores the second last index of subsequence ending at nums[i]; 
            can be used to backtrace the longest subsequence
            """
            last_index = [-1] * len(nums)

            max_len[0] = 1
            for i in range(1, len(nums)):
                ml = 1
                l_index = -1
                for j in range(i):
                    if nums[i] > nums[j] and ml < max_len[j] + 1:
                        ml = max_len[j] + 1
                        l_index = j
                max_len[i] = ml
                last_index[i] = l_index
            return max(max_len)


class BinarySearchSolution:
    def lengthOfLIS(self, nums):
        """
        Given an unsorted array of integers, find the length of longest increasing subsequence.

        Example:

        Input: [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
        Note:

        There may be more than one LIS combination, it is only necessary for you to return the length.
        Your algorithm should run in O(n2) complexity.
        Follow up: Could you improve it to O(n log n) time complexity?

        :type nums: List[int]
        :rtype: int

        max_len[i] denotes the longest increaing subsequence ending with num[i-1]
        """

        if not nums:
            return 0

        parent = [-1] * len(nums)
        # lis[i] stores the index of the prefix of potentially longest subsequence so far
        lis = [0]
        max_length = 1

        for i in range(1, len(nums)):
            li = lis[-1]
            if nums[i] > nums[li]:
                lis.append(i)
                parent[i] = li
                max_length += 1
            else:
                # find out the first element in lis is bigger than nums[i], replace it with nums[i]
                # Example 1, given 1, 5, 7, 2, 3, 4, lis = [1, 5, 7] and nums[i] = 2
                # Example 2, given 1, 5, 7, 2, 8, 9, lis = [1, 5, 7] and nums[i] = 2
                # we need to replace the first element bigger than nums[i] with nums[i],
                # i.e. replace 5 with 2 but keep 7 (see examples above)
                # because 1, 2 is potentially the length 2 prefix of the longest subsequence (For example 1, if 7 might be replace later) than that of 1, 5.
                ri = self.binarySearch(nums, lis, i, 0, len(lis))
                if ri < 0:
                    ri = 0
                li = lis[ri]
                # record the parent of nums[i]
                parent[i] = parent[li]
                lis[ri] = i
        return max_length

    def binarySearch(self, nums, lis, t, start, end):
        if start < end - 1:
            mid = (start + end) // 2
            if nums[t] > nums[lis[mid-1]]:
                return self.binarySearch(nums, lis, t, mid, end)
            else:
                return self.binarySearch(nums, lis, t, start, mid)
        else: # start == end - 1 or start == end
            return start



s = BinarySearchSolution()
print(s.lengthOfLIS([1, 5, 7, 2, 3, 4]))