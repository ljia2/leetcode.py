import collections

class Solution(object):
    def isPossible(self, nums):
        """
        You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

        Example 1:
        Input: [1,2,3,3,4,5]
        Output: True
        Explanation:
        You can split them into two consecutive subsequences :
        1, 2, 3
        3, 4, 5
        Example 2:
        Input: [1,2,3,3,4,4,5,5]
        Output: True
        Explanation:
        You can split them into two consecutive subsequences :
        1, 2, 3, 4, 5
        3, 4, 5
        Example 3:
        Input: [1,2,3,4,4,5]
        Output: False

        :type nums: List[int]
        :rtype: bool


        I used a greedy algorithm.
        left is a hashmap, left[i] counts the number of i that I haven't placed yet.
        end is a hashmap, end[i] counts the number of consecutive subsequences that ends at number i
        Then I tried to split the nums one by one.
        If I could neither add a number to the end of a existing consecutive subsequence nor find two following number in the left,
        I returned False
        """

        left = collections.Counter(nums)
        end = collections.Counter()
        for i in nums:
            if not left[i]:
                continue
            # decrease i's frequecy by 1
            left[i] -= 1
            # first append i at the sequence j ending by i-1
            # decreasing j's frequency by 1
            # increase the new sequence ending by 1 by 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            # try form another i, i+1, i+2
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True