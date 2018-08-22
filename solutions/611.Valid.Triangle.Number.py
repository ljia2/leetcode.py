class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        for a in range(len(nums)-2):
            b, c = a + 1, len(nums)-1
            while b < c:
                ab = nums[a] + nums[b]
                if ab > nums[c]:
                    res += c - b
                elif ab < nums[c]:
                    c -= 1
                    while c > b and ab <= nums[c]:
                        c -= 1
                    res += c - b
                else:
                    c -= 1
                    while c > b and nums[c] == nums[c+1]:
                        c -= 1
                    res += c - b
                b += 1
                c = len(nums)-1
        return res


def main():
    s = Solution()
    print(s.triangleNumber([24,3,82,22,35,84,19]))


if __name__ == "__main__":
    main()