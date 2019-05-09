class Solution:
    def productExceptSelf(self, nums):
        """
        Given an array nums of n integers where n > 1,
        return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

        Example:

        Input:  [1,2,3,4]
        Output: [24,12,8,6]
        Note: Please solve it without division and in O(n).

        Follow up:
        Could you solve it with constant space complexity?
        (The output array does not count as extra space for the purpose of space complexity analysis.)


        :type nums: List[int]
        :rtype: List[int]

        """
        if nums is None or len(nums) == 0:
            return []
        # output[i] is the product of nums[:i]
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]

        # output[i] now store the left product of nums[:i]
        right_prod = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            output[i] = output[i] * right_prod
            right_prod = right_prod * nums[i]
        return output


s = Solution()
print(s.productExceptSelf([1,2,3,4]))

### What if we can use divide and need to consider 0

class DivisionSolution:
    def productExceptSelf(self, nums):
        if not nums:
            return []

        zero = []
        prod = 1
        for i, num in enumerate(nums):
            if num == 0:
                zero.append(i)
            else:
                prod *= num

        if zero:
            if len(zero) > 1:
                return [0] * len(nums)
            else:
                ans = []
                for i in range(len(nums)):
                    if i in zero:
                        ans.append(prod)
                    else:
                        ans.append(0)
                return ans
        else:
            ans = []
            for num in nums:
                ans.append(prod // num)
            return ans


### What if we can use divide and need to consider 0