class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        """
        1) From the right most position to find the first ADJACENT num[i-1] < nums[i] (greedy algorithm),
            i) swap nums[i-1] and with the lowest positioned from nums[i:len(nums)] that is higher than nums[i-1] to guarantee
            the least amount of increase,
            ii) sort nums[i+1:len(nums)] in ascending order to make the final number smaller possible,  
        2) otherwise, continue with the second most right digits
        """
        for r in range(len(nums)-1, -1, -1):
            # 1)
            if nums[r-1] < nums[r]:
                # 1.i)
                for i in range(len(nums)-1, r-1, -1):
                    if nums[i] > nums[r-1]:
                        temp = nums[i]
                        nums[i] = nums[r-1]
                        nums[r-1] = temp
                        break
                # 1.ii)
                for i in range(r, len(nums)):
                    for j in range(i+1, len(nums)):
                        if nums[i] > nums[j]:
                            temp = nums[j]
                            nums[j] = nums[i]
                            nums[i] = temp
                return
        # 2)
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
