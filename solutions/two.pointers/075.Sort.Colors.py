
class Solution:
    def sortColors(self, nums):
        """
        Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent,
        with the colors in the order red, white and blue.

        Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

        Note: You are not suppose to use the library's sort function for this problem.

        Example:

        Input: [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
        Follow up:

        A rather straight forward solution is a two-pass algorithm using counting sort.
        First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
        Could you come up with a one-pass algorithm using only constant space?

        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return

        # split the nums into four regions, red, white, unclassified, blue.
        # red is [0, r]
        # white is [r, w)
        # unclassified = [w, b]
        # blue = (b+1, len(nums)
        # initially, r = w = 0 and b = len(nums)-1, which means everything is unclassified.

        r, w, b = 0, 0, len(nums)-1
        # when w <= b, there are unclassified nums
        while w <= b:
            if nums[b] == 2:
                # leave this num into the blue region and retreat blue pointer
                b -= 1
            elif nums[b] == 1:
                # swap the nums[w] and nums[b], where nums[w] is the next white insert place
                nums[w], nums[b] = nums[b], nums[w]
                w += 1
            elif nums[b] == 0:
                # swap the nums[r] and nums[b], where nums[r] is the next red insert place
                nums[r], nums[b] = nums[b], nums[r]
                r += 1
                # when white is less than r, we need to move white as least equal to r.
                while w < r:
                    w += 1
        return

def main():
    s = Solution()
    print(s.sortColors([2,0,2,1,1,0]))

if __name__ == "__main__":
    main()