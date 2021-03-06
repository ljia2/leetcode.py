##### Follow up: Could you improve it to O(n log n) time complexity?
import bisect

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
        Your algorithm should run in O(n^2) complexity.

        Follow up: Could you improve it to O(n log n) time complexity?

        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        parent = [-1] * len(nums)
        # monotonic stack
        lis = [nums[0]] # lis[i] stores the index of the prefix of potentially longest subsequences so far
        lisnums = [nums[0]]
        max_length = 1
        for i in range(1, len(nums)):
            lindex = lis[-1]
            if nums[i] > nums[lindex]:
                lis.append(i)
                lisnums.append(nums[i])
                parent[i] = lindex
                max_length += 1
            else:
                # find out the first element in lis is bigger than nums[i], replace it with nums[i]
                # Example 1, given 1, 5, 7, 2, 3, 4, lis = [1, 5, 7] and nums[i] = 2
                # Example 2, given 1, 5, 7, 2, 8, 9, lis = [1, 5, 7] and nums[i] = 2
                # we need to replace the first element bigger than nums[i] with nums[i],
                # i.e. replace 5 with 2 but keep 7 (see examples above)
                # because 1, 2 is potentially the length 2 prefix of the longest subsequence
                # (For example 1, if 7 might be replace later) than that of 1, 5.
                ri = bisect.bisect_right(lisnums, nums[i])
                lindex = lis[ri]
                lis[ri] = i
                lisnums[ri] = nums[i]
                # record the parent of nums[i]
                parent[i] = parent[lindex]
        return max_length

s = BinarySearchSolution()
print(s.lengthOfLIS([1, 5, 7, 2, 3, 4]))


# Follow up: what if we want to return the number of longest subsequences.
class VarationSolution:
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

        max_len[i] denotes (the # of longest increasing subsequence ending with num[i] and the lengh)
        """
        if not nums:
            return 0
        dp = [(1, 1)] * len(nums)
        for i in range(1, len(nums)):
            ml = -1
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][1] + 1 > ml:
                        dp[i] = (dp[j][0], dp[j][1] + 1)
                        ml = max(ml, dp[j][1] + 1)

        ml = max(map(lambda x: x[1], dp))

        ans = 0
        for c, l in dp:
            if l == ml:
                ans += c
        return ans

s = VarationSolution()
print(s.lengthOfLIS([1, 5, 7, 2, 3, 4]))