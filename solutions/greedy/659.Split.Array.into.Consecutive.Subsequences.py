import collections

class Solution(object):
    def isPossible(self, nums):
        """
        You are given an integer array sorted in ascending order (may contain duplicates),
        you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers.
        Return whether you can make such a split.

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

        Call a chain a sequence of 3 or more consecutive numbers.

        Considering numbers x from left to right, if x can be added to a current chain,
        it's at least as good to add x to that chain first, rather than to start a new chain.

        Why? If we started with numbers x and greater from the beginning,
        the shorter chains starting from x could be concatenated with the chains ending before x,
        possibly helping us if there was a "chain" from x that was only length 1 or 2.


        I used a greedy algorithm.
        freq is a hashmap, freq[i] counts the number of i that I haven't placed yet.
        seq_count is a hashmap, seq_count[i] counts the number of consecutive subsequences that ends at number i

        Then I tried to split the nums one by one.
        If I could neither add a number to the end of a existing consecutive subsequence nor find two following number in the left,
        I returned False
        """

        freq = collections.Counter(nums)
        seq_count = collections.Counter()
        for i in nums:
            if freq[i] == 0:
                continue

            # decrease i's frequency by 1
            freq[i] -= 1

            # first append i at the sequence j ending by i-1
            if seq_count[i - 1] > 0:
                # decreasing j's frequency by 1
                seq_count[i - 1] -= 1
                # increase the new sequence ending by 1 by 1
                seq_count[i] += 1
            # try form another i, i+1, i+2
            elif freq[i + 1] and freq[i + 2]:
                freq[i + 1] -= 1
                freq[i + 2] -= 1
                seq_count[i + 2] += 1
            else:
                # num can not form any consecutive subsequence, return False
                return False

        return True