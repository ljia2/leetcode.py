class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        Hint: For a position index i, its amount trapped water at index only is determined by left_max (highest bar before i)
        and right_max (highest bar after i).

        The mound = min(left_max, left_right) - height[i]
        """
        if len(height) < 3:
            return 0
        else:
            left_max = [0] * len(height)
            m = 0
            for index in range(len(height)):
                if height[index] > m:
                    m = height[index]
                left_max[index] = m

            m = 0
            right_max = [0] * len(height)
            for index in range(len(height)-1, 0, -1):
                if height[index] > m:
                    m = height[index]
                right_max[index] = m

            ans = 0
            for index in range(len(height)):
                ans += max(0, min(left_max[index], right_max[index]) - height[index])
            return ans


s2 = Solution()
results = s2.trap([0, 3, 1, 0, 3, 1, 0, 1])
print(results)
results = s2.trap([0, 3, 1, 0, 0, 1, 0, 0])
print(results)
results = s2.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(results)
results = s2.trap([9,6,8,8,5,6,3])
print(results)
