class Solution:
    def triangleNumber(self, nums):
        """
        Given an array consists of non-negative integers, your task is to count the number of triplets
        chosen from the array that can make triangles if we take them as side lengths of a triangle.

        Example 1:

        Input: [2,2,3,4]
        Output: 3
        Explanation:
        Valid combinations are:
        2,3,4 (using the first 2)
        2,3,4 (using the second 2)
        2,2,3

        Note:

        The length of the given array won't exceed 1000.
        The integers in the given array are in the range of [0, 1000].

        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        for a in range(len(nums)-1, 1, -1):
            # find the b + c > a
            b, c = 0, a-1
            while b < c:
                bc = nums[b] + nums[c]
                if bc > nums[a]:
                    res += c - b
                    c -= 1
                else:
                    b += 1
        return res


def main():
    s = Solution()
    print(s.triangleNumber([24,3,82,22,35,84,19]))


if __name__ == "__main__":
    main()