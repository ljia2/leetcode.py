class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        else:
            result = 0
            pre_index = 0
            index = 1
            while index < len(height):
                # when height[pre_index] > height[index], there is possible of dip bounded by height[pre_index]
                if height[pre_index] > height[index]:
                    # find the next bar greater than or equal to height[pre_index]
                    aft_index = index + 1
                    while aft_index < len(height):
                        if height[aft_index] >= height[pre_index]:
                            break
                        aft_index += 1
                    if aft_index < len(height):
                        result += min(height[pre_index], height[aft_index]) * (aft_index - pre_index - 1) - sum(height[pre_index+1: aft_index])
                        pre_index = aft_index
                        index = pre_index + 1
                    else:
                        # there is no bar >= height[pre_index], find the furthese bar bigger than height[index]
                        aft_index = index + 1
                        maxHighIndex = index
                        while aft_index < len(height):
                            if height[aft_index] >= height[maxHighIndex]:
                                maxHighIndex = aft_index
                            aft_index += 1
                        if maxHighIndex > index:
                            result += min(height[pre_index], height[maxHighIndex]) * (maxHighIndex - pre_index - 1) - sum(height[pre_index+1: maxHighIndex])
                            pre_index = maxHighIndex
                            index = pre_index + 1
                        else:
                            pre_index = index
                            index = index + 1
                elif height[pre_index] <= height[index]:
                    # try next position
                    pre_index = index
                    index = pre_index + 1
            return result


class Solution2:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        Hint: For a position index i, its amount trapped water at index only is determined by left_max (highest bar before i) and right_max (highest bar after i).
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

            results = 0
            for index in range(len(height)):
                results += max(0, min(left_max[index], right_max[index]) - height[index])
            return results

def main():
    s = Solution()

    results = s.trap([0, 3, 1, 0, 3, 1, 0, 1])
    print(results)

    results = s.trap([0, 3, 1, 0, 0, 1, 0, 0])
    print(results)

    results = s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(results)

    results = s.trap([9,6,8,8,5,6,3])
    print(results)

    s2 = Solution2()
    results = s2.trap([0, 3, 1, 0, 3, 1, 0, 1])
    print(results)

    results = s2.trap([0, 3, 1, 0, 0, 1, 0, 0])
    print(results)

    results = s2.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(results)

    results = s2.trap([9,6,8,8,5,6,3])
    print(results)


if __name__ == '__main__':
    main()