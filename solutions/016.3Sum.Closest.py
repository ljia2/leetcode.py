class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_diff = -1
        for left in range(len(nums)-2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid, right = left + 1, len(nums)-1
            while mid < right:
                sum = nums[left] + nums[mid] + nums[right]
                diff = nums[left] + nums[mid] + nums[right] - target
                if min_diff < 0 or abs(diff) < min_diff:
                    min_diff = abs(diff)
                    result = sum
                if diff == 0:
                    mid += 1
                    while mid < right and nums[mid] == nums[mid-1]:
                        mid += 1
                    right -= 1
                    while right > mid and nums[right] == nums[right+1]:
                        right -= 1
                elif diff < 0:
                    mid += 1
                    while mid < right and nums[mid] == nums[mid-1]:
                        mid += 1
                elif diff > 0:
                    right -= 1
                    while right > mid and nums[right] == nums[right+1]:
                        right -= 1
        return result


def main():
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4], 1))


if __name__ == "__main__":
    main()