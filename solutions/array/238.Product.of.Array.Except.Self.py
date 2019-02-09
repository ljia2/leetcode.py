# class Solution:
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         Note: Please solve it without division and in O(n).
#         """
#         if nums is None or len(nums) == 0:
#             return []
#         left_prod = [1] * len(nums)
#         for i in range(1, len(nums)):
#             left_prod[i] = left_prod[i-1] * nums[i-1]
#         right_prod = [1] * len(nums)
#         for i in range(len(nums)-2, -1, -1):
#             right_prod[i] = right_prod[i+1] * nums[i+1]
#
#         output = [1] * len(nums)
#         for i in range(nums):
#             output[i] = left_prod[i] * right_prod[i]
#         return output



class Solution2:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Follow up:
        Could you solve it with constant space complexity?
        (The output array does not count as extra space for the purpose of space complexity analysis.)
        """
        if nums is None or len(nums) == 0:
            return []
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]
        right_prod = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            output[i] = output[i] * right_prod
            right_prod = right_prod * nums[i]
        return output


def main():
    s = Solution2()
    print(s.productExceptSelf([1,2,3,4]))


if __name__ == "__main__":
    main()