import bisect

class Solution:
    def subsetMinMaxK(self, nums, K):
        """
        return the number of subsets whose min + max = K
        :param nums:
        :param K:
        :return:
        """
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n-1):
            maxnum = K - nums[i]
            max_index = bisect.bisect_left(nums, maxnum)
            # we find the maxnum in the sorted nums.
            if max_index < n and nums[max_index] == maxnum:
                if max_index >= i + 1:
                    ans += 2**(max_index-i-1)
                elif max_index == i:
                    # one element subset whose min and max are the same number.
                    ans += 1
        return ans

## Follow up: what if min + max <= k.
class Solution:
    def subsetMinMaxK(self, nums, K):
        """
        return the number of subsets whose min + max = K
        :param nums:
        :param K:
        :return:
        """
        if not nums or len(nums) < 2:
            return 0

        n = len(nums)
        sumPow = [0] * n
        sumPow[0] = 1
        twoPow = 1
        for i in range(1, n):
            sumPow[i] = sumPow[i-1] + twoPow
            twoPow <<= 1

        for sumP in sumPow:
            print(sumP, )

        nums.sort()
        ans = 0
        for i in range(n-1):
            maxnum = K - nums[i]
            max_index = bisect.bisect_right(nums, maxnum)
            # we find the maxnum in the sorted nums it is max_index - 1 >= 0.
            if max_index > 0:
                if max_index - 1 >= i + 1:
                    ans += sumPow(max_index - 1) - sumPow(max_index - 1 - i - 1)
                elif max_index - 1 == i:
                    # one element subset whose min and max are the same number.
                    ans += sumPow(max_index) - sumPow(max_index - 1)
        return ans


