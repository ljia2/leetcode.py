class Solution:
    def maxArea(self, height):
        """
        Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
        n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
        Find two lines, which together with x-axis forms a container, such that the container contains the most water.

        Note: You may not slant the container and n is at least 2.

        https://leetcode.com/problems/container-with-most-water/description/

        The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
        In this case, the max area of water (blue section) the container can contain is 49.

        Example:

        Input: [1,8,6,2,5,4,8,3,7]
        Output: 49

        :type height: List[int]
        :rtype: int


        use two pointers start and end moving towards to each other.

        calculate the bucket that can hold waters to find the maximum volume.

        """

        if height is None or not height:
            return 0

        max_area = 0
        # two pointers from start and end
        left = 0
        right = len(height)-1
        while left < right:
            max_left = height[left]
            max_right = height[right]
            area = min(max_left, max_right) * (right - left)
            if max_area < area:
                max_area = area
            # update the smaller pointer, to find the next higher alternative.
            if max_left < max_right:
                while left < len(height) and height[left] <= max_left:
                    left += 1
            else:
                while right > -1 and height[right] <= max_right:
                    right -= 1
        return max_area
