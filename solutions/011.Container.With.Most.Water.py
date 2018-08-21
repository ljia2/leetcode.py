class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None or not height:
            return 0
        max_area = 0
        left = 0
        right = len(height)-1
        while left < right:
            max_left = height[left]
            max_right = height[right]
            area = min(max_left, max_right) * (right - left)
            if max_area < area:
                max_area = area
            if max_left < max_right:
                while left < len(height) and height[left] <= max_left:
                    left += 1
            else:
                while right > -1 and height[right] <= max_right:
                    right -= 1
        return max_area
