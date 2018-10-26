class DPSolution:
    def maxSubArray(self, nums):
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

        Example:

        Input: [-2,1,-3,4,-1,2,1,-5,4],
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.
        Follow up:

        If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


        :type nums: List[int]
        :rtype: int

        max_sum[i] stores the subarray (must consective) from the first i elements and must use the i element

        Transition:

        max_sum[i] = (max_sum[i-1] + nums[i]) if max_sum[i-1] >= 0 else nums[i]

        """
        if not nums:
            return 0
        else:
            # max_sum[i] stores the max sum value for (0, i) by using nums[i].
            # Note that when previous max_sum[i-1] is negative, max_sum[i] should only use nums[i] otherwise max_sum[i] = max_sum[i-1] + nums[i]
            # We do not want a negative sum apply to i position and only wants positive.
            max_sum = []
            for i in range(len(nums)):
                if i == 0:
                    # the max_sum by using nums[0] is the nums[0] itself
                    max_sum.append(nums[i])
                else:
                    if max_sum[i-1] < 0:
                        max_sum.append(nums[i])
                    else:
                        max_sum.append(max_sum[i-1] + nums[i])

            return max(max_sum)


class DPSolutionII:
    def maxSubArray(self, nums):
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

        Example:

        Input: [-2,1,-3,4,-1,2,1,-5,4],
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.
        Follow up:

        If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


        :type nums: List[int]
        :rtype: int

        What is return the subarray?

        """
        if not nums:
            return 0
        else:
            # max_sum[i] stores the max sum value for (0, i) by using nums[i].
            # Note that when previous max_sum[i-1] is negative, max_sum[i] should only use nums[i] otherwise max_sum[i] = max_sum[i-1] + nums[i]
            # We do not want a negative sum apply to i position and only wants positive.
            max_sum = []
            for i in range(len(nums)):
                if i == 0:
                    # the max_sum by using nums[0] is the nums[0] itself
                    max_sum.append((nums[i], 0, 0))
                else:
                    prev_max_sum, start, end = max_sum[i-1]
                    if prev_max_sum < 0:
                        # start the new subarray from i, do not include the previous subarray, because previous subarray's max_sum is negative
                        max_sum.append((nums[i], i, i))
                    else:
                        # extend the subarray from its start to a new end at i, because prev_max_sum is positive. 
                        max_sum.append((prev_max_sum + nums[i], start, i))

            return max(map(lambda x: x[0], max_sum))

