class Solution: # TLE
    def nextGreaterElements(self, nums):
        """
        Given a circular array (the next element of the last element is the first element of the array),
        print the Next Greater Number for every element.
        The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,
        which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

        Example 1:
        Input: [1,2,1]
        Output: [2,-1,2]
        Explanation: The first 1's next greater number is 2;
        The number 2 can't find next greater number;
        The second 1's next greater number needs to search circularly, which is also 2.

        Note: The length of given array won't exceed 10000.

        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums:
            return []

        results = [-1] * len(nums)
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[(i+j) % len(nums)] > nums[i]:
                    results[i] = nums[(i+j) % len(nums)]
                    break
        return results

class SolutionII:
    def nextGreaterElements(self, nums):
        """
        Given a circular array (the next element of the last element is the first element of the array),
        print the Next Greater Number for every element.
        The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,
        which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

        Example 1:
        Input: [1,2,1]
        Output: [2,-1,2]
        Explanation: The first 1's next greater number is 2;
        The number 2 can't find next greater number;
        The second 1's next greater number needs to search circularly, which is also 2.

        Note: The length of given array won't exceed 10000.

        :type nums: List[int]
        :rtype: List[int]

        For example, given [1, 2, 4, 3], we first expand input and scan the expanded input from tail to beginning
        we expand [1, 2, 4, 3, 1, 2, 4, 3]
                            ^  ~  ~  ~
        when calcuating for 3, we need to scan 1, 2, 4 after 3. we then know 1, 2 are smaller than 3.
                  [1, 2, 4, 3, 1, 2, 4, 3]
                         ^  ~  ~  ~
        next when we compute 4, we need to scan 3, 1, 2. But we have know that 1, 2, smaller than 3, we do not need to scan them.
        """

        if not nums:
            return []

        results = [-1] * len(nums)
        # m_stack store the indices whose values are increasing (monotonic stack)
        m_stack = []

        for i in range(2*len(nums)-1, -1, -1):
            while m_stack and nums[m_stack[-1]] <= nums[i % len(nums)]:
                m_stack.pop()
            if m_stack:
                results[i % len(nums)] = nums[m_stack[-1]]
            m_stack.append(i % len(nums))
        return results


class BestSolution:
    def nextGreaterElements(self, nums):
        """
        Given a circular array (the next element of the last element is the first element of the array),
        print the Next Greater Number for every element.
        The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,
        which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

        Example 1:
        Input: [1,2,1]
        Output: [2,-1,2]
        Explanation: The first 1's next greater number is 2;
        The number 2 can't find next greater number;
        The second 1's next greater number needs to search circularly, which is also 2.

        Note: The length of given array won't exceed 10000.

        :type nums: List[int]
        :rtype: List[int]

        For example, given [1, 2, 4, 3], we first expand input and scan the expanded input from tail to beginning
        we expand [1, 2, 4, 3, 1, 2, 4, 3]
                            ^  ~  ~  ~
        when calcuating for 3, we need to scan 1, 2, 4 after 3. we then know 1, 2 are smaller than 3.
                  [1, 2, 4, 3, 1, 2, 4, 3]
                         ^  ~  ~  ~
        next when we compute 4, we need to scan 3, 1, 2. But we have know that 1, 2, smaller than 3, we do not need to scan them.
        """

        if not nums:
            return []

        results = [-1] * len(nums)

        for i in range(2*len(nums)-1, -1, -1):
            j = i + 1
            while j < 2*len(nums):
                # if nums[j % len(nums)] > nums[i % len(nums)], we immediate find its next greater number
                if nums[j % len(nums)] > nums[i % len(nums)]:
                    results[i % len(nums)] = j % len(nums) # store the index of next greater number
                    break
                else: # if nums[j % len(nums)] <= nums[i % len(nums)]
                    if results[j % len(nums)] == -1:
                        # if nums[j % len(nums)] has no next greater number, nums[i % len(nums) must have no next greater number either
                        break
                    else:
                        # Otherwise start search from the index of the next great number of nums[j % len(nums)]
                        j = results[j % len(nums)]

        for i in range(len(nums)):
            if results[i] != -1:
                results[i] = nums[results[i]]

        return results


s = Solution()
print(s.nextGreaterElements([1, 2, 1]))
print(s.nextGreaterElements([1, -2, -2, -1]))
