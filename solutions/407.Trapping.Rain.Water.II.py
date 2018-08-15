
class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """

        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        else:
            # store the water trapped for the list of row-wise
            row_dict = dict()
            for r in range(len(heightMap)):
                print(heightMap[r])
                r_result = self.trap(heightMap[r])
                for (c, w) in r_result:
                    row_dict[(r, c)] = w
            print(row_dict)

            raw_water_dict = dict()
            # find out the water trapped for the list of column-wise
            for c in range(len(heightMap[0])):
                c_result = self.trap([r[c] for r in heightMap])
                for (r, w) in c_result:
                    if (r, c) in row_dict.keys() and r != 0 and r != len(heightMap)-1 and c != 0 and c != len(heightMap[0])-1:
                        raw_water_dict[(r,c)] = min(w, row_dict.get((r, c)))
            waterHeighMap = list.copy(heightMap)
            for (k, v) in raw_water_dict.items():
                (r, c) = k
                heightMap[r][c] += v
            # each contain's water is determined by the minimum of the virtual (height + water) height of four walls
            for (k, v) in raw_water_dict.items():
                (r, c) = k
                raw_water_dict[(r,c)] = min(w, min(waterHeighMap[r-1][c],
                                                   min(waterHeighMap[r+1][c],
                                                       min(waterHeighMap[r][c-1],
                                                           waterHeighMap[r][c+1]))))

            return sum(raw_water_dict.values())

    def trap(self, height):
        """
        :type height: List[Int]
        :rtype: int
        """
        if len(height) < 3:
            return []
        else:
            left_max = [0] * len(height)
            m = 0
            for i in range(len(height)):
                if height[i] > m:
                    m = height[i]
                left_max[i] = m
            right_max = [0] * len(height)

            m = 0
            for i in range(len(height)-1, 0, -1):
                if height[i] > m:
                    m = height[i]
                right_max[i] = m

            results = []
            for i in range(len(height)):
                water = max(0, min(left_max[i], right_max[i]) - height[i])
                if water > 0:
                    results.append((i, water))
            return results


def main():
    s = Solution()
    results = s.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]])
    print(results)


if __name__ == '__main__':
    main()