from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
        You can only see the k numbers in the window. Each time the sliding window moves right by one position.
        Return the max sliding window.

        Example:

        Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
        Output: [3,3,5,5,6,7]
        Explanation:

        Window position                Max
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
         1 [3  -1  -3] 5  3  6  7       3
         1  3 [-1  -3  5] 3  6  7       5
         1  3  -1 [-3  5  3] 6  7       5
         1  3  -1  -3 [5  3  6] 7       6
         1  3  -1  -3  5 [3  6  7]      7
        Note:
        You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

        Follow up:
        Could you solve it in linear time?

        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        monotonic stack: store the sequence indices whose values are non-increasing.

        store the index of max number in a sliding window of size k.

        """

        if not nums or k < 1 or len(nums) < k:
            return []

        # Defining Deque and result list
        deq = deque()
        ans = []

        # Initialization of the sliding window of size K.
        # First traversing through K in the nums and only adding the index of the maximum value to the deque.
        # Note: We are only storing the index and not the value.
        # Now, Comparing the new value in the nums with the last index value from deque,
        #      1) if new value is bigger, we don't need any previous values in stack less than it.
        #      2) if the new value is samller, we put it into stack to ensure the stack is decreasing. .

        for i in range(k):
            while deq:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)

        # Here we will have deque with index of maximum element for the first subsequence of length k.
        # Now we will traverse from k to the end of array and do 4 things
        # 1. Appending left most indexed value to the result
        # 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
        # 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it
        # 4. Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)

        # moving the window
        for i in range(k, len(nums)):
            # store the maxinum value of the current window.
            ans.append(nums[deq[0]])

            # keep poping the maximum value in the monotonic stack if it is out of window.
            # untill all numbers in the stack are relevant.
            if deq[0] < i - k + 1:
                deq.popleft()

            while deq:
                if nums[i] > nums[deq[-1]]:
                    # nums[deq[-1]] cannot be the max of the window, because it is smaller than nums[i]; pop it.
                    deq.pop()
                else:
                    break

            deq.append(i)

        # Adding the maximum for last sliding window ending at last window.
        ans.append(nums[deq[0]])

        return ans
