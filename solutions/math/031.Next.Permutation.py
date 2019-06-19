class Solution:
    def nextPermutation(self, nums):
        """
        Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

        If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

        The replacement must be in-place and use only constant extra memory.

        Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

        1,2,3 → 1,3,2
        3,2,1 → 1,2,3
        1,1,5 → 1,5,1
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        """
        1) From the right most position to find the first ADJACENT num[i-1] < nums[i] (greedy algorithm),
            i) swap nums[i-1] and with the lowest positioned from nums[i:len(nums)] that is higher than nums[i-1] to guarantee the least amount of increase,
            ii) sort nums[i+1:len(nums)] in ascending order to make the final number smaller possible,  
        2) otherwise, continue with the second most right digits
        """

        for r in range(len(nums)-1, -1, -1):
            # 1)
            if nums[r-1] < nums[r]:
                # 1.i)
                for i in range(len(nums)-1, r-1, -1):
                    if nums[i] > nums[r-1]:
                        nums[i], nums[r-1] = nums[r-1], nums[i]
                        nums[r:] = sorted(nums[r:])
                        return

        # 2) if all numbers are in non-ascending order, sort them reversely.
        nums.sort()
        return


def main():
    s = Solution()
    input1 = [2,1,4,3]
    s.nextPermutation(input1)
    print(input1)
    input2 = [5,4,3,1]
    s.nextPermutation(input2)
    print(input2)
    input3 = [1,4,6,3]
    s.nextPermutation(input3)
    print(input3)
    input4 = [3,6,2,1]
    s.nextPermutation(input4)
    print(input4)
    input5 = [5,4,7,5,3,2]
    s.nextPermutation(input5)
    print(input5)
    input6 = [4,2,0,2,3,2,0]
    s.nextPermutation(input6)
    print(input6)

if __name__ == "__main__":
    main()

### Follow up: find next largest number that is smaller than current one.
class VarationSolution:
    def prevPermutation(self, nums):
        if not nums:
            return []

        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i] < nums[i-1]:
                # flip nums[i] and nums[i-1] to guarantee the least increase.
                nums[i-1], nums[i] = nums[i], nums[i-1]
                # sort nums[i:] in descending order to guarantee next.
                nums[i:] = sorted(nums[i:], reverse=True)
                return nums

        nums.reverse()
        return nums

s = VarationSolution()
print(s.prevPermutation([2,1,4,2,5]))

