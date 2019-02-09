class Solution:
    def triangleNumber(self, nums):
        """
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