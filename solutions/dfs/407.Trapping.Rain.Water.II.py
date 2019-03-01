
class Solution:
    def trapRainWater(self, heightMap):
        """
        Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map,
        compute the volume of water it is able to trap after raining.

        Note:
        Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

        Example:

        Given the following 3x6 height map:
        [
          [1,4,3,1,3,2],
          [3,2,1,3,2,4],
          [2,3,3,2,3,1]
        ]

        Return 4.

        The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.
        After the rain, water is trapped between the blocks. The total volume of water trapped is 4.
        :type heightMap: List[List[int]]
        :rtype: int


        DFS over heightMap????

        """






s = Solution()
results = s.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]])
print(results)