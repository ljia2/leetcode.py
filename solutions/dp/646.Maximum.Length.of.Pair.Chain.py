class Solution:
    def findLongestChain(self, pairs):
        """
        You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

        Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c.
        Chain of pairs can be formed in this fashion.

        Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs.
        You can select pairs in any order.

        Example 1:
        Input: [[1,2], [2,3], [3,4]]
        Output: 2
        Explanation: The longest chain is [1,2] -> [3,4]
        Note:
        The number of given pairs will be in the range [1, 1000].
        
        :type pairs: List[List[int]]
        :rtype: int
        """
        # sorted the pairs by the second element
        # for example. given [[1, 2], [5, 6], [3, 4]], after sorting by the second elements,
        # we can get the possible longest chain of [1, 2] -> [3, 4] -> [5, 6]
        # because longest chain must be in aseconding order of the second elements.
        spairs = sorted(pairs, key=lambda x:x[1])

        lc = [1] * len(spairs)

        for i in range(1, len(lc)):
            ml = 1
            for j in range(i):
                a, b = spairs[j]
                c, d = spairs[i]
                if b < c:
                    if ml < lc[j] + 1:
                        ml += 1
            lc[i] = ml
        return max(lc)

s = Solution()
print(s.findLongestChain([[1,2], [2,3], [3,4]]))

