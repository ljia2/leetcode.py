class Solution:
    def rob(self, nums):
        """
        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
        All houses at this place are arranged in a circle.
        That means the first house is the neighbor of the last one.
        Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

        Given a list of non-negative integers representing the amount of money of each house,
        determine the maximum amount of money you can rob tonight without alerting the police.

        Example 1:

        Input: [2,3,2]
        Output: 3
        Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
                     because they are adjacent houses.
        Example 2:

        Input: [1,2,3,1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.

        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        house_num = len(nums)
        max_rob = [0] * house_num

        for i in range(house_num):
            if i == 0:
                max_rob[i] = nums[i]
            elif i == 1:
                max_rob[i] = nums[0]
            elif 1 < i < house_num - 1:
                max_rob[i] = max(max_rob[i-1], max_rob[i-2] + nums[i])
            else:
                max_rob[i] = max_rob[i-1]

        max_results = max_rob[house_num-1]

        for i in range(house_num):
            if i == 0:
                max_rob[i] = 0
            elif i == 1:
                max_rob[i] = nums[i]
            else:
                max_rob[i] = max(max_rob[i-1], max_rob[i-2] + nums[i])

        if max_results < max_rob[house_num-1]:
            max_results = max_rob[house_num-1]

        return max_results


class SolutionII:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        house_num = len(nums)
        include = 0
        exclude = 0

        for i in range(house_num):
            if i == 0:
                # always not include the first house
                include, exclude = 0, 0
            elif i == 1:
                include, exclude = nums[i], include
            else:
                include, exclude = exclude + nums[i], max(include, exclude)

        max_result = max(include, exclude)

        for i in range(house_num):
            if i == 0:
                include, exclude = nums[i], 0
            elif i < house_num - 1:
                include, exclude = exclude + nums[i], max(include, exclude)
            else:
                # always include the first house and exclude the last house
                include, exclude = max(include, exclude), max(include, exclude)
        if max_result < max(include, exclude):
            max_result = max(include, exclude)
        return max_result
