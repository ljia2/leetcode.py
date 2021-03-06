class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        Given a list of non-negative numbers and a target integer k,
        write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k,
        that is, sums up to n*k where n is also an integer.

        Example 1:

        Input: [23, 2, 4, 6, 7],  k=6
        Output: True
        Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
        Example 2:

        Input: [23, 2, 6, 4, 7],  k=6
        Output: True
        Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.


        Note:

        The length of the array won't exceed 10,000.
        You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

        :type nums: List[int]
        :type k: int
        :rtype: bool

        calculate prefix sum and use sum % k as key, value is the smallest index i s.t. sum(nums[:i+1]) % k == key;
        special case: when k == 0, we are looking for subarray whose sum is 0

        """
        if not nums or len(nums) < 2 or k < 0:
            return False

        psum = 0
        psumdict = dict()

        # initialize 0, meaning zero sum of no numbers.
        # key is the mod of psum % k, value is the smallest position
        psumdict[0] = 0
        for i in range(len(nums)):
            pos = i + 1
            psum += nums[i]

            if k == 0:
                if psum not in psumdict.keys():
                    psumdict[psum] = i
                elif pos - psumdict[psum] >= 2:
                    return True
            else:
                r = psum % k
                if r not in psumdict.keys():
                    psumdict[r] = i
                elif pos - psumdict[r] >= 2:
                    return True

        return False

s = Solution()
print(s.checkSubarraySum([1, 2, 3], 5))

#### What if we have negative numbers in array or k is negative? Same solution.
# negative % positive = positive, negative % negative = negative, positive % negative = negatieve, positive % positive = positive.