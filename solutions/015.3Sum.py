class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or not nums or len(nums) < 3:
            return []
        # in-place sorting
        nums.sort()

        # output all 3-item tuples (a, b, c) summed to 0; the left as a and mid as b and right as c where a<=b<=c
        solutions = []
        for left in range(len(nums)-2):
            # skip all tuples starting with nums[left-1] has been processed and skip nums[left]
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid, right = left+1, len(nums)-1
            while mid < right:
                sum = nums[left] + nums[mid] + nums[right]
                if sum == 0:
                    solutions.append((nums[left], nums[mid], nums[right]))
                    # after a qualified tuple, need to change b and c at the same time
                    mid += 1
                    while mid < right and nums[mid] == nums[mid-1]:
                        mid += 1
                    right -= 1
                    while right > mid and nums[right] == nums[right+1]:
                        right -= 1
                elif sum > 0:
                    right -= 1
                    while right > mid and nums[right] == nums[right+1]:
                        right -= 1
                elif sum < 0:
                    mid += 1
                    while mid < right and nums[mid] == nums[mid-1]:
                        mid += 1
        return solutions


def main():
    s = Solution()
    print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
    print(s.threeSum([-1,0,1,2,-1,-4]))


if __name__ == "__main__":
    main()