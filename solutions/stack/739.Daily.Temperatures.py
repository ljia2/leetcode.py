class Solution(object):
    def dailyTemperatures(self, T):
        """
        Given a list of daily temperatures T, return a list such that, for each day in the input,
        tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

        For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

        Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
        :type T: List[int]
        :rtype: List[int]

        iterate from tail to beginning:
           use a monotonic stack (increasing) to store the tuple of (temp, index).
        """

        mstack = []
        n = len(T)
        ans = []
        for i in range(n-1, -1, -1):
            # all element in mstack <= T[i] will not be answer for the days from 0 to i - 1.
            while mstack and T[mstack[-1]] <= T[i]:
                mstack.pop()
            if mstack:
                j = mstack[-1]
                ans.append(j-i)
            else:
                ans.append(0)
            mstack.append(i)
        ans.reverse()
        return ans

s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))